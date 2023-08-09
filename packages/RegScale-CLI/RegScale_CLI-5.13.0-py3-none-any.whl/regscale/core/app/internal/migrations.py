#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Performs data processing for bulk processing"""

# standard python imports
from pathlib import Path
from typing import Tuple

import click
import requests

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.core.app.utils.app_utils import (
    check_file_path,
    create_progress_object,
    error_and_exit,
    save_data_to,
)
from regscale.core.app.utils.regscale_utils import get_all_from_module
from regscale.core.app.utils.threadhandler import create_threads, thread_assignment

job_progress = create_progress_object()
process_counter = []


@click.group()
def migrations():
    """Performs data processing for legacy data to migrate data formats or perform bulk processing."""


@migrations.command(name="inheritance_converter")
def inheritance_converter():
    """
    Migrates all data from legacy one to one system to the new one to many system.
    """
    convert_inheritance()


@migrations.command(name="issue_linker")
def issue_linker():
    """
    Provides linkage to the lineage of the issue (deep links to parent records in the tree).
    """
    link_issues()


@migrations.command(name="assessment_linker")
def assessment_linker():
    """
    Provides linkage to the lineage of the assessment (deep links to parent records in the tree).
    """
    link_assessments()


@migrations.command(name="risk_linker")
def risk_linker():
    """
    Provides linkage to the lineage of the risk (deep links to parent records in the tree).
    """
    link_risks()


def convert_inheritance() -> None:
    """
    Migrates all data from legacy one to one system to the new one to many system
    :return: None
    """
    app = Application()
    config = app.config
    api = Api(app)

    logger = create_logger()
    # retrieve all inherited controls
    try:
        logger.info("Retrieving all existing inherited controls.")
        inherited_controls = api.get(
            url=config["domain"] + "/api/inheritance/getAllInheritedControls"
        ).json()
        logger.info(
            "%i inherited controls retrieved from RegScale.", len(inherited_controls)
        )
    except requests.exceptions.RequestException as ex:
        logger.error("Unable to retrieve inherited controls\n%s", ex)

    # output inherited controls list
    save_data_to(
        file=Path("./artifacts/inheritedControls.json"),
        data=inherited_controls,
    )
    # loop through each inherited control
    new_inherited_controls = []
    for inherited_control in inherited_controls:
        # create new control and map to new schema
        new_control = {
            "id": 0,
            "isPublic": inherited_control["isPublic"] is True,
            "parentId": int(inherited_control["parentId"]),
            "parentModule": inherited_control["parentModule"],
            "baseControlId": int(inherited_control["id"]),
            "inheritedControlId": int(inherited_control["inheritedControlId"]),
        }
        new_inherited_controls.append(new_control)

    # output the new control list
    save_data_to(
        file=Path("./artifacts/inheritedControlMappings.json"),
        data=new_inherited_controls,
    )
    logger.info(
        "%i controls remapped to new inheritance engine", len(new_inherited_controls)
    )

    # loop through and create each controls
    new_inheritance = []
    logger.info("Beginning the process to upload and create new Inherited controls")
    url_inheritance = f'{config["domain"]}/api/inheritedControls'
    for n in new_inherited_controls:
        try:
            print(n)
            response = api.post(url_inheritance, json=n)
            created_control = response.json()
            logger.info("New inherited control mapping: %s", created_control["id"])
            new_inheritance.append(created_control)
        except requests.exceptions.RequestException as ex:
            error_and_exit(f"Unable to save new inherited control.\n{ex}")

    # output the new control list
    save_data_to(
        file=Path("./artifacts/newInheritedControlMappings.json"),
        data=new_inheritance,
    )
    logger.info("%i controls saved to the new inheritance system", len(new_inheritance))


def link_issues() -> None:
    """
    Provides linkage to the lineage of the issue (deep links to parent records in the tree).
    :return: None
    """
    logger = create_logger()
    module = "issues"

    api, regscale_issues = initialize_and_fetch_data(module)

    with job_progress:
        # create task to process issues
        processing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(regscale_issues)} RegScale issue(s)...",
            total=len(regscale_issues),
        )

        # create threads to process the issues
        create_threads(
            process=process_data,
            args=(api, regscale_issues, module, processing_issues),
            thread_count=len(regscale_issues),
        )

        # notify user of outcome
        logger.info(
            "%s/%s %s processed from RegScale.",
            len(process_counter),
            len(regscale_issues),
            module.title(),
        )


def link_assessments() -> None:
    """
    Provides linkage to the lineage of the assessment (deep links to parent records in the tree).
    :return: None
    """
    logger = create_logger()
    module = "assessments"

    api, regscale_assessments = initialize_and_fetch_data(module)

    with job_progress:
        # create task to process issues
        processing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(regscale_assessments)} RegScale issue(s)...",
            total=len(regscale_assessments),
        )

        # create threads to process the issues
        create_threads(
            process=process_data,
            args=(api, regscale_assessments, module, processing_issues),
            thread_count=len(regscale_assessments),
        )

        # notify user of outcome
        logger.info(
            "%s/%s %s processed from RegScale.",
            len(process_counter),
            len(regscale_assessments),
            module.title(),
        )


def link_risks() -> None:
    """
    Provides linkage to the lineage of the risk (deep links to parent records in the tree).
    :return: None
    """
    logger = create_logger()
    module = "risks"

    api, regscale_risks = initialize_and_fetch_data(module)

    with job_progress:
        # create task to process issues
        processing_issues = job_progress.add_task(
            f"[#f8b737]Analyzing {len(regscale_risks)} RegScale issue(s)...",
            total=len(regscale_risks),
        )

        # create threads to process the issues
        create_threads(
            process=process_data,
            args=(api, regscale_risks, module, processing_issues),
            thread_count=len(regscale_risks),
        )

        # notify user of outcome
        logger.info(
            "%i/%i %s processed from RegScale.",
            len(process_counter),
            len(regscale_risks),
            module.title(),
        )


def initialize_and_fetch_data(module: str) -> Tuple[Api, list[dict]]:
    """
    Function to start application, api, and fetches all records for the provided module
    from RegScale via API and saves the output to a .json file
    :param str module: python module
    :return: Tuple[Api object, list of data of provided module from RegScale API]
    :rtype: Tuple[Api, list[dict]]
    """
    # load the config from YAML
    app = Application()
    api = Api(app)
    logger = create_logger()

    # get the data of provided module from RegScale via API
    regscale_data = get_all_from_module(api=api, module=module)

    # verify artifacts folder exists
    check_file_path("artifacts")

    # write out risks data to file
    save_data_to(
        file=Path(f"./artifacts/RegScale{module.title()}.json"),
        data=regscale_data,
    )
    logger.info(
        "Writing out RegScale risk list to the artifacts folder (see RegScale%sList.json).",
        module.title(),
    )
    logger.info(
        "%i %s retrieved for processing from RegScale.", len(regscale_data), module
    )
    return api, regscale_data


def process_data(args: Tuple, thread: int) -> None:
    """
    Function to utilize threading and process the data from RegScale
    :param Tuple args: Tuple of args to use during the process
    :param int thread: Thread number of current thread
    :raises: General error if unable to retrieve data from RegScale API
    :return: None
    """
    # set up local variables from args passed
    logger = create_logger()
    api, regscale_data, module, task = args

    # find which records should be executed by the current thread
    threads = thread_assignment(thread=thread, total_items=len(regscale_data))
    # iterate through the thread assignment items and process them
    for i in range(len(threads)):
        # set the recommendation for the thread for later use in the function
        item = regscale_data[threads[i]]

        url_processor = (
            f'{api.config["domain"]}/api/{module}/processLineage{item["id"]}'
        )
        try:
            process_result = api.get(url_processor)
            logger.info(
                "Processing %s #: %s Result: %s",
                module[:-1].title(),
                item["id"],
                process_result.text,
            )
            process_counter.append(item)
        except Exception:
            logger.error("Unable to process Issue # %i.", item["id"])
        job_progress.update(task, advance=1)
