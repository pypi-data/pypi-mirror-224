#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RegScale Dependabot Integration"""

# standard python imports
from datetime import datetime  # type: ignore
from dateutil import relativedelta  # type: ignore
import pandas as pd  # type: ignore
import requests  # type: ignore
import click
from rich.console import Console  # type: ignore

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.utils.app_utils import (
    days_between,
    get_current_datetime,
)
from regscale.core.app.utils.regscale_utils import create_regscale_assessment
from regscale.models.regscale_models.assessment import Assessment
from regscale.models.regscale_models.issue import Issue
from regscale.models import regscale_id, regscale_module


def get_github_dependabot_alerts(api: Api) -> str:
    """
    Retrieve GitHub Dependabot Alerts from the GitHub Dependabot Alert API
    :param api: RegScale API object
    :return: json response date from API GET request
    :rtype: str
    """
    url = f"https://{api.config['githubDomain']}/repos/{api.config['dependabotOwner']}/{api.config['dependabotRepo']}/dependabot/alerts"
    user = api.config["dependabotId"]
    token = api.config["dependabotToken"]
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(url, headers=headers, auth=(user, token))
    return r.json()


def build_data(api: Api) -> list[dict]:
    """
    Build vulnerability alert data list
    :param api: RegScale API object
    :return: vulnerability data list
    :rtype: list[dict]
    """
    # execute GET request
    data = get_github_dependabot_alerts(api=api)
    return [
        {
            "number": [i["number"]],
            "state": [i["state"]],
            "summary": [i["security_advisory"]["summary"]],
            "ecosystem": [i["security_vulnerability"]["package"]["ecosystem"]],
            "name": [i["security_vulnerability"]["package"]["name"]],
            "severity": [i["security_vulnerability"]["severity"]],
            "published": [i["security_advisory"]["published_at"]],
            "days_elapsed": [
                days_between(vuln_time=i["security_advisory"]["published_at"])
            ],
        }
        for i in data
        if i["state"] == "open"
    ]


def build_dataframes(api: Api) -> str:
    """
    Build pandas dataframes from vulnerability alert data list
    :param api: RegScale API object
    :return: dataframe as an HTML table
    :rtype: str (html)
    """
    # create vulnerability data list
    vuln_data_list = build_data(api=api)
    # create empty list to hold dataframes
    dfs = []

    for vulnerability in vuln_data_list:
        df = pd.DataFrame.from_dict(vulnerability)
        dfs.append(df)

    result = pd.concat(dfs, ignore_index=True)
    return result.to_html(header=True, index=False, justify="center", border=1)


def create_alert_assessment(
    api: Api, parent_module: str = "assessments", parent_id: int = 1
) -> int:
    """
    Create Assessment containing GitHub Dependabot alerts
    :return: New Assessment ID
    :rtype: int
    """
    # create the assessment report HTML table
    df_output = build_dataframes(api=api)
    # build assessment model data
    assessment_data = Assessment(
        leadAssessorId=api.config["userId"],
        title="Dependabot Vulnerability Results Assessment",
        assessmentType="Control Testing",
        plannedStart=get_current_datetime(),
        plannedFinish=get_current_datetime(),
        assessmentReport=df_output,
        assessmentPlan="Complete the child issues created by the github dependabot alerts that were retrieved by the API. The assessment will fail if any high severity vulnerabilities has a days_elapsed value greater than or equal to 10 days.",
        createdById=api.config["userId"],
        dateCreated=get_current_datetime(),
        lastUpdatedById=api.config["userId"],
        dateLastUpdated=get_current_datetime(),
        parentModule=parent_module,
        parentId=parent_id,
        status="In Progress",
    )
    # create vulnerability data list
    vuln_data_list = build_data(api=api)
    # if assessmentResult is changed to Pass / Fail then status has to be changed to complete and a completion date has to be passed
    for vulnerability in vuln_data_list:
        if (
            vulnerability["severity"][0] == "high"
            and vulnerability["days_elapsed"][0] >= 10
        ):
            assessment_data.status = "Complete"
            assessment_data.actualFinish = get_current_datetime()
            assessment_data.assessmentResult = "Fail"

    return create_regscale_assessment(
        url=f"{api.config['domain']}/api/assessments",
        new_assessment=assessment_data.dict(),
        api=api,
    )


def create_alert_issues(
    api: Api, parent_module: str = "assessments", parent_id: int = 1
) -> None:
    """
    Create child issues from the alert assessment
    :param api: RegScale API object
    :param parent_module: Parent module of the assessment
    :param parent_id: Parent ID of the assessment
    :return: None
    """
    # execute POST request and return new assessment ID
    assessment_id = create_alert_assessment(
        api=api, parent_module=parent_module, parent_id=parent_id
    )
    # create vulnerability data list
    vuln_data_list = build_data(api=api)
    # loop through each vulnerability alert in the list
    for vulnerability in vuln_data_list:
        issue_data = Issue(
            title="Dependabot Alert",  # Required
            dateCreated=get_current_datetime("%Y-%m-%dT%H:%M:%S"),
            description=vulnerability["summary"][0],
            severityLevel=Issue.assign_severity(
                vulnerability["severity"][0]
            ),  # Required
            issueOwnerId=api.config["userId"],  # Required
            dueDate=get_current_datetime(),
            identification="Vulnerability assessment",
            status="Open",
            assessmentId=assessment_id,
            createdBy=api.config["userId"],
            lastUpdatedById=api.config["userId"],
            dateLastUpdated=get_current_datetime(),
            parentId=assessment_id,
            parentModule="assessments",
        )
        api.post(
            f'{api.config["domain"]}/api/issues',
            json=issue_data.dict(),
        )


def get_and_create_dependabot_alerts(
    regscale_id_: int,
    regscale_module_: str = "assessments",
) -> None:
    """
    Get and create child issues from the alert assessment
    :param regscale_id_: RegScale ID
    :param regscale_module_: RegScale Module
    :return: None
    """
    app = Application()
    api = Api(app)
    create_alert_issues(api=api, parent_module=regscale_module_, parent_id=regscale_id_)


@click.group()
def dependabot() -> None:
    """
    RegScale Dependabot Integration
    """
    pass


@dependabot.command()
@regscale_id()
@regscale_module(default="assessments")
def create_alerts(regscale_id_: int, regscale_module_: str = "assessments") -> None:
    """
    Create child issues from the alert assessment
    :param regscale_id_: RegScale ID
    :param regscale_module_: RegScale Module
    :return: None
    """
    get_and_create_dependabot_alerts(regscale_id_, regscale_module_)
