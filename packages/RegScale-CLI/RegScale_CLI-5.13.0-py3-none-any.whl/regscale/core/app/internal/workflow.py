"""Functions for creating, starting, and fetching workflows from RegScale."""
from typing import Optional, Dict

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.core.app.utils.app_utils import (
    error_and_exit,
    get_current_datetime,
)
from regscale.models.regscale_models.workflow import Workflow

logger = create_logger()


def create_regscale_workflow_from_template(
    new_assessment_id: int, template_id: int
) -> int:
    """Create a RegScale workflow from a template.
    :param int new_assessment_id: RegScale assessment ID
    :param int template_id: RegScale template ID
    :raises Exception: If the workflow template cannot be retrieved
    :raises Exception: If the workflow cannot be created
    :return: RegScale workflow ID
    :rtype: int
    """
    app = Application()
    workflow = Workflow(
        name="Placeholder",  # just a placeholder its overriden below by the template
        status="Active",
        startDate=get_current_datetime(),
        endDate=None,
        currentStep=0,
        comments="",
        createdById=app.config["userId"],
        dateCreated=get_current_datetime(),
        lastUpdatedById=app.config["userId"],
        isPublic=True,
        dateLastUpdated=get_current_datetime(),
        ownerId=app.config["userId"],
        atlasModule="assessments",
        parentId=new_assessment_id,
        workflowInstanceSteps=[],
    )

    template = get_workflow_template(app, template_id)
    if template:
        logger.debug(template)
        workflow.name = template.get("name")
        workflow.workflowInstanceSteps = template["workflowTemplateSteps"]
    else:
        error_and_exit(f"Failed to get workflow template with id #{template_id}.")

    if new_workflow_id := workflow.insert_workflow(app, template_id).id:
        logger.info(f"Workflow created with id {new_workflow_id}")
        if submit_workflow_instance(app, workflow.dict(), new_workflow_id):
            return new_workflow_id
    error_and_exit(
        f"Failed to create RegScale workflow from template with id #{template_id}."
    )


def create_workflow(app, workflow_data: dict, template_id: int) -> Optional[Dict]:
    """Create a RegScale workflow from a template.
    :param Application app: Regscale application
    :param dict workflow_data: Workflow data
    :param int template_id: RegScale template ID
    :return: RegScale workflow or None
    :rtype: object | None
    """
    api = Api(app)
    create_workflow_instance_from_template_url = (
        f"{app.config['domain']}/api/workflowInstances/createFromTemplate/{template_id}"
    )
    workflow_res = api.post(
        url=create_workflow_instance_from_template_url, json=workflow_data
    )
    logger.debug(workflow_res.status_code)
    if not workflow_res.ok:
        logger.error(
            f"Failed to create RegScale workflow from template with id {template_id}."
        )
        return None
    return workflow_res.json()


def get_workflow_template(app: Application, template_id: int) -> Optional[Dict]:
    """Get a RegScale workflow template.
    :param Application app: Regscale application
    :param int template_id: RegScale template ID
    :return: RegScale workflow template
    :rtype: Optional[Dict]
    """
    api = Api(app)
    workflow_template_url = (
        f"{app.config['domain']}/api/workflowTemplates/{template_id}"
    )
    get_template_rep = api.get(url=workflow_template_url)
    return get_template_rep.json() if get_template_rep.ok else None


def submit_workflow_instance(
    app: Application, workflow_data: dict, workflow_id: int
) -> bool:
    """Submit a RegScale workflow instance.
    :param Application app: Regscale application
    :param dict workflow_data: Workflow data
    :param int workflow_id: RegScale workflow ID
    :return: True if successful else False
    :rtype: bool
    """
    api = Api(app)
    submit_workflow_url = (
        f"{app.config['domain']}/api/workflowInstances/submit/{app.config['userId']}"
    )
    submit_resp = api.put(url=submit_workflow_url, json=workflow_data)
    if submit_resp.ok:
        logger.info(f"Workflow with id: {workflow_id} started.")
        return True
    return False
