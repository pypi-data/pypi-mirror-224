#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Add functionality to upgrade application catalog information via API."""

# pylint: disable=line-too-long
# pylint: disable=global-statement
# pylint: disable=global-at-module-level
# pylint: disable=abstract-class-instantiated
# pylint: disable=too-many-lines

# Standard Imports
import operator
import sys
from typing import Tuple

import click  # type: ignore
import requests  # type: ignore
import pandas as pd  # type: ignore
from requests import JSONDecodeError  # type: ignore

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.models.app_models.catalog_compare import CatalogCompare
from regscale.core.app.utils.app_utils import create_progress_object, error_and_exit

# create logger function to log to the console
logger = create_logger()
# create progress object
job_progress = create_progress_object()

DOWNLOAD_URL: str = ""
CAT_UUID: str = ""
SECURITY_CONTROL_ID_KEY: list = []


def display_menu() -> None:
    """
    Start the process of comparing two catalogs, one from the master catalog list
    and one from the user's RegScale instance
    :return: None
    """
    # set system environment variables
    app = Application()
    api = Api(app)
    api.timeout = 180

    # start menu build process
    menu_counter: list = []
    # import master catalog list
    data = CatalogCompare.get_master_catalogs(api=api)
    # sort master catalogue list
    catalogues = data["catalogues"]
    catalogues.sort(key=operator.itemgetter("id"))
    for i, catalog in enumerate(catalogues):
        # print each catalog in the master catalog list
        print(f'{catalog["id"]}: {catalog["value"]}')
        menu_counter.append(i)
    # set status to False to run loop
    status: bool = False
    while status is False:
        # select catalog to run diagnostic
        value = click.prompt(
            "Please enter the number of the catalog you would like to run diagnostics on",
            type=int,
        )
        # check if value exist that is selected
        if value < min(menu_counter) or value > max(menu_counter):
            print("That is not a valid selection, please try again")
        else:
            status = True
        # choose catalog to run diagnostics on
        for i, catalog in enumerate(catalogues):
            if catalog["id"] == value:
                global CAT_UUID
                CAT_UUID = catalog["metadata"]["uuid"]
                if catalog["download"] is True and catalog["paid"] is False:
                    global DOWNLOAD_URL
                    DOWNLOAD_URL = catalog["link"]
                if catalog["download"] is True and catalog["paid"] is True:
                    logger.warning(
                        "This is a paid catalog, please contact RegScale customer support."
                    )
                    sys.exit()
                break
    compare_and_update_catalog_elements(api=api)


def compare_and_update_catalog_elements(api: Api) -> None:
    """
    Function to compare and update elements between catalogs
    :param Api api: Api object
    :return: None
    """
    new_catalog_elements = parse_new_catalog()
    old_catalog_elements = parse_old_catalog(api=api)
    update_security_controls(
        new_security_controls=new_catalog_elements[0],
        old_security_controls=old_catalog_elements[0],
        api=api,
    )
    update_ccis(
        new_ccis=new_catalog_elements[1],
        old_ccis=old_catalog_elements[1],
        api=api,
    )
    update_objectives(
        new_objectives=new_catalog_elements[2],
        old_objectives=old_catalog_elements[2],
        api=api,
    )
    update_parameters(
        new_parameters=new_catalog_elements[3],
        old_parameters=old_catalog_elements[3],
        api=api,
    )
    update_tests(
        new_tests=new_catalog_elements[4],
        old_tests=old_catalog_elements[4],
        api=api,
    )


def update_security_controls(
    new_security_controls: dict, old_security_controls: dict, api: Api
) -> None:
    """
    Function to compare and update security controls
    :param dict new_security_controls: security controls from new catalog
    :param dict old_security_controls: security controls from old catalog
    :param Api api: api object
    :return: None
    """
    archived_list = []
    updated_list = []
    created_list = []
    element_exists = False
    for new_security_control in new_security_controls:
        for old_security_control in old_security_controls:
            if new_security_control.get("controlId") == old_security_control.get(
                "controlId"
            ):
                key_dict = {"old_sc_id": 0, "new_sc_id": 0}
                key_dict["old_sc_id"] = old_security_control["id"]
                key_dict["new_sc_id"] = new_security_control["id"]
                SECURITY_CONTROL_ID_KEY.append(key_dict)
                element_exists = True
                if new_security_control["archived"] is True:
                    old_security_control["archived"] = True
                    archived_list.append(old_security_control)
                    break
                for key in old_security_control:
                    if key != "id" or key != "catalogueID":
                        old_security_control[key] = new_security_control[key]
                    else:
                        continue
                update = api.put(
                    url=api.config["domain"]
                    + f"/api/SecurityControls/{old_security_control['id']}",
                    json=old_security_control,
                )
                update.raise_for_status()
                if update.ok:
                    logger.info(
                        "Updated Security Control for Control ID: %i",
                        old_security_control["id"],
                    )
                    updated_list.append(old_security_control)
        if element_exists is False:
            new_security_control["catalogueID"] = old_security_controls[0][
                "catalogueID"
            ]
            create = api.post(
                url=api.config["domain"] + "/api/SecurityControls",
                json=new_security_control,
            )
            create.raise_for_status()
            if create.ok:
                logger.info(
                    "Created Security Control for Control ID: %i",
                    new_security_control["id"],
                )
                created_list.append(new_security_control)
    security_controls_report(
        archived=archived_list, updated=updated_list, created=created_list
    )


def security_controls_report(archived: list, updated: list, created: list) -> None:
    """
    Function to create changed security controls report
    :param list archived: archived data elements
    :param list updated: updated data elements
    :param list created: created data elements
    :return: None
    """
    archived_sc = pd.DataFrame.from_dict(archived)
    updated_sc = pd.DataFrame.from_dict(updated)
    created_sc = pd.DataFrame.from_dict(created)
    with pd.ExcelWriter("security_controls.xlsx") as writer:
        archived_sc.to_excel(writer, sheet_name="Archived", index=False)
        updated_sc.to_excel(writer, sheet_name="Updated", index=False)
        created_sc.to_excel(writer, sheet_name="Created", index=False)


def update_ccis(new_ccis: dict, old_ccis: dict, api: Api) -> None:
    """
    Function to compare and update ccis
    :param dict new_ccis: ccis from new catalog
    :param dict old_ccis: ccis from old catalog
    :param Api api: api object
    :return: None
    """
    archived_list = []
    updated_list = []
    created_list = []
    element_exists = False
    for new_cci in new_ccis:
        for old_cci in old_ccis:
            if new_cci["name"] == old_cci["name"]:
                element_exists = True
                if new_cci["archived"] is True:
                    old_cci["archived"] = True
                    archived_list.append(old_cci)
                    break
                for key in old_cci:
                    if key == "isPublic":
                        old_cci["isPublic"] = False
                    elif key != "id" or key != "securityControlId":
                        old_cci[key] = new_cci[key]
                    else:
                        continue
                key_set = next(
                    (
                        item
                        for item in SECURITY_CONTROL_ID_KEY
                        if item["new_sc_id"] == new_cci["securityControlId"]
                    ),
                    None,
                )
                old_sc_id = key_set.get("old_sc_id")
                old_cci["securityControlId"] = old_sc_id
                update = api.put(
                    url=api.config["domain"] + f"/api/cci/{old_cci['id']}",
                    json=old_cci,
                )
                update.raise_for_status()
                if update.ok:
                    logger.info(
                        "Updated CCI for CCI ID: %i",
                        old_cci["id"],
                    )
                    updated_list.append(old_cci)
        if element_exists is False:
            key_set = next(
                (
                    item
                    for item in SECURITY_CONTROL_ID_KEY
                    if item["new_sc_id"] == new_cci["securityControlId"]
                ),
                None,
            )
            old_sc_id = key_set.get("old_sc_id")
            new_cci["securityControlId"] = old_sc_id
            create = api.post(
                url=api.config["domain"] + "/api/cci",
                json=new_cci,
            )
            create.raise_for_status()
            if create.ok:
                logger.info(
                    "Created CCI for CCI ID: %i",
                    new_cci["id"],
                )
                created_list.append(new_cci)
    ccis_report(archived=archived_list, updated=updated_list, created=created_list)


def ccis_report(archived: list, updated: list, created: list) -> None:
    """
    Function to create changed ccis report
    :param list archived: archived data elements
    :param list updated: updated data elements
    :param list created: created data elements
    :return: None
    """
    archived_cci = pd.DataFrame.from_dict(archived)
    updated_cci = pd.DataFrame.from_dict(updated)
    created_cci = pd.DataFrame.from_dict(created)
    with pd.ExcelWriter("ccis.xlsx") as writer:
        archived_cci.to_excel(writer, sheet_name="Archived", index=False)
        updated_cci.to_excel(writer, sheet_name="Updated", index=False)
        created_cci.to_excel(writer, sheet_name="Created", index=False)


def update_objectives(new_objectives: dict, old_objectives: dict, api: Api) -> None:
    """
    Function to compare and update objectives
    :param dict new_objectives: objectives from new catalog
    :param dict old_objectives: objectives from old catalog
    :param Api api: Api object
    :return: None
    """
    archived_list = []
    updated_list = []
    created_list = []
    element_exists = False
    for new_objective in new_objectives:
        for old_objective in old_objectives:
            if new_objective["name"] == old_objective["name"]:
                element_exists = True
                if new_objective["archived"] is True:
                    old_objective["archived"] = True
                    archived_list.append(old_objective)
                    break
                for key in old_objective["objective"]:
                    if key == "isPublic":
                        old_objective["isPublic"] = False
                    elif key not in ["id", "securityControlId", "tenantsId"]:
                        old_objective["objective"][key] = new_objective[key]
                    else:
                        continue
                key_set = next(
                    (
                        item
                        for item in SECURITY_CONTROL_ID_KEY
                        if item["new_sc_id"] == new_objective["securityControlId"]
                    ),
                    None,
                )
                old_sc_id = key_set.get("old_sc_id")
                old_objective["objective"]["securityControlId"] = old_sc_id
                if old_objective["objective"].get("tenantsId") is not None:
                    del old_objective["objective"]["tenantsId"]
                update = api.put(
                    url=api.config["domain"]
                    + f"/api/controlObjectives/{old_objective['id']}",
                    json=old_objective["objective"],
                )
                update.raise_for_status()
                if update.ok:
                    logger.info(
                        "Updated Objective for Objective ID: %i",
                        old_objective["id"],
                    )
                    updated_list.append(old_objective)
        if element_exists is False:
            key_set = next(
                (
                    item
                    for item in SECURITY_CONTROL_ID_KEY
                    if item["new_sc_id"] == new_objective["securityControlId"]
                ),
                None,
            )
            old_sc_id = key_set.get("old_sc_id")
            new_objective["securityControlId"] = old_sc_id
            create = api.post(
                url=api.config["domain"] + "/api/controlObjectives",
                json=new_objective,
            )
            create.raise_for_status()
            if create.ok:
                logger.info(
                    "Created Objective for Objective ID: %i",
                    new_objective["id"],
                )
                created_list.append(new_objective)
    objectives_report(
        archived=archived_list, updated=updated_list, created=created_list
    )


def objectives_report(archived: list, updated: list, created: list) -> None:
    """
    Function to create changed objectives report
    :param list archived: archived data elements
    :param list updated: updated data elements
    :param list created: created data elements
    :return: None
    """
    archived_objective = pd.DataFrame.from_dict(archived)
    updated_objective = pd.DataFrame.from_dict(updated)
    created_objective = pd.DataFrame.from_dict(created)
    with pd.ExcelWriter("objectives.xlsx") as writer:
        archived_objective.to_excel(writer, sheet_name="Archived", index=False)
        updated_objective.to_excel(writer, sheet_name="Updated", index=False)
        created_objective.to_excel(writer, sheet_name="Created", index=False)


def parse_parameters(data: dict) -> dict:
    """
    Function to parse keys from the provided dictionary
    :param dict data: parameters from catalog
    :return: dict
    """
    for key in data:
        if key == "isPublic":
            data["isPublic"] = False
        elif key == "default":
            data["default"] = None
        elif key == "dataType":
            data["dataType"] = None
        elif key != "id" or key != "securityControlId":
            continue
    return data


def update_parameters(new_parameters: dict, old_parameters: dict, api: Api) -> None:
    """
    Function to compare and update parameters
    :param dict new_parameters: parameters from new catalog
    :param dict old_parameters: parameters from old catalog
    :param Api api: Api object
    :return: None
    """
    archived_list = []
    updated_list = []
    created_list = []
    element_exists = False
    for new_parameter in new_parameters:
        for old_parameter in old_parameters:
            if new_parameter["parameterId"] == old_parameter["parameterId"]:
                element_exists = True
                if new_parameter["archived"] is True:
                    old_parameter["archived"] = True
                    archived_list.append(old_parameter)
                    break
                old_parameter = parse_parameters(old_parameter)
                key_set = next(
                    (
                        item
                        for item in SECURITY_CONTROL_ID_KEY
                        if item["new_sc_id"] == new_parameter["securityControlId"]
                    ),
                    None,
                )
                old_sc_id = key_set.get("old_sc_id")
                old_parameter["securityControlId"] = old_sc_id
                update = api.put(
                    url=api.config["domain"]
                    + f"/api/controlParameters/{old_parameter['id']}",
                    json=old_parameter,
                )
                update.raise_for_status()
                if update.ok:
                    logger.info(
                        "Updated Parameter for Parameter ID: %i",
                        old_parameter["id"],
                    )
                    updated_list.append(old_parameter)
        if element_exists is False:
            key_set = next(
                (
                    item
                    for item in SECURITY_CONTROL_ID_KEY
                    if item["new_sc_id"] == new_parameter["securityControlId"]
                ),
                None,
            )
            old_sc_id = key_set.get("old_sc_id")
            new_parameter["securityControlId"] = old_sc_id
            create = api.post(
                url=api.config["domain"] + "/api/controlParameters",
                json=new_parameter,
            )
            create.raise_for_status()
            if create.ok:
                logger.info(
                    "Created Parameter for Parameter ID: %i",
                    new_parameter["id"],
                )
                created_list.append(new_parameter)
    parameters_report(
        archived=archived_list, updated=updated_list, created=created_list
    )


def parameters_report(archived: list, updated: list, created: list) -> None:
    """
    Function to create changed parameters report
    :param list archived: archived data elements
    :param list updated: updated data elements
    :param list created: created data elements
    :return: None
    """
    archived_parameter = pd.DataFrame.from_dict(archived)
    updated_parameter = pd.DataFrame.from_dict(updated)
    created_parameter = pd.DataFrame.from_dict(created)
    with pd.ExcelWriter("parameters.xlsx") as writer:
        archived_parameter.to_excel(writer, sheet_name="Archived", index=False)
        updated_parameter.to_excel(writer, sheet_name="Updated", index=False)
        created_parameter.to_excel(writer, sheet_name="Created", index=False)


def update_tests(new_tests: dict, old_tests: dict, api: Api) -> None:
    """
    Function to compare and update tests
    :param dict new_tests: tests from new catalog
    :param dict old_tests: tests from old catalog
    :param Api api: API Object
    :return: None
    """
    archived_list = []
    updated_list = []
    created_list = []
    element_exists = False
    for new_test in new_tests:
        for old_test in old_tests:
            if new_test["testId"] == old_test["testId"]:
                element_exists = True
                if new_test["archived"] is True:
                    old_test["archived"] = True
                    archived_list.append(old_test)
                    break
                for key in old_test:
                    if key == "isPublic":
                        old_test["isPublic"] = False
                    elif key != "id" or key != "securityControlId":
                        old_test[key] = new_test[key]
                    else:
                        continue
                key_set = next(
                    (
                        item
                        for item in SECURITY_CONTROL_ID_KEY
                        if item["new_sc_id"] == new_test["securityControlId"]
                    ),
                    None,
                )
                old_sc_id = key_set.get("old_sc_id")
                old_test["securityControlId"] = old_sc_id
                update = api.put(
                    url=api.config["domain"] + f"/api/test/{old_test['id']}",
                    json=old_test,
                )
                update.raise_for_status()
                if update.ok:
                    logger.info(
                        "Updated test for test ID: %i",
                        old_test["id"],
                    )
                    updated_list.append(old_test)
        if element_exists is False:
            key_set = next(
                (
                    item
                    for item in SECURITY_CONTROL_ID_KEY
                    if item["new_sc_id"] == new_test["securityControlId"]
                ),
                None,
            )
            old_sc_id = key_set.get("old_sc_id")
            new_test["securityControlId"] = old_sc_id
            create = api.post(
                url=api.config["domain"] + "/api/test",
                json=new_test,
            )
            create.raise_for_status()
            if create.ok:
                logger.info(
                    "Created test for test ID: %i",
                    new_test["id"],
                )
                created_list.append(new_test)
    tests_report(archived=archived_list, updated=updated_list, created=created_list)


def tests_report(archived: list, updated: list, created: list) -> None:
    """
    Function to create changed tests report
    :param list archived: archived data elements
    :param list updated: updated data elements
    :param list created: created data elements
    :return: None
    """
    archived_test = pd.DataFrame.from_dict(archived)
    updated_test = pd.DataFrame.from_dict(updated)
    created_test = pd.DataFrame.from_dict(created)
    with pd.ExcelWriter("tests.xlsx") as writer:
        archived_test.to_excel(writer, sheet_name="Archived", index=False)
        updated_test.to_excel(writer, sheet_name="Updated", index=False)
        created_test.to_excel(writer, sheet_name="Created", index=False)


def parse_new_catalog() -> Tuple[list, list, list, list, list]:
    """
    Function to parse elements from the new catalog
    :return: Tuple containing lists of new catalog data elements
    :rtype: Tuple
    """
    with job_progress:
        # add task for retrieving new catalog
        retrieving_new_catalog = job_progress.add_task(
            "[#f8b737]Retrieving selected catalog from RegScale.com/regulations.",
            total=6,
        )
        # retrieve new catalog to run diagnostics on
        new_catalog = get_new_catalog(url=DOWNLOAD_URL)
        # update the task as complete
        job_progress.update(retrieving_new_catalog, advance=1)
        # retrieve new catalog security controls
        new_security_controls = get_new_security_controls(ncatalog=new_catalog)
        # update the task as complete
        job_progress.update(retrieving_new_catalog, advance=1)
        # retrieve new catalog ccis
        new_ccis = get_new_ccis(ncatalog=new_catalog)
        # update the task as complete
        job_progress.update(retrieving_new_catalog, advance=1)
        # retrieve new catalog objectives
        new_objectives = get_new_objectives(ncatalog=new_catalog)
        # update the task as complete
        job_progress.update(retrieving_new_catalog, advance=1)
        # retrieve new catalog parameters
        new_parameters = get_new_parameters(ncatalog=new_catalog)
        # update the task as complete
        job_progress.update(retrieving_new_catalog, advance=1)
        # retrieve new catalog tests
        new_tests = get_new_tests(ncatalog=new_catalog)
        # update the task as complete
        job_progress.update(retrieving_new_catalog, completed=6)
    return new_security_controls, new_ccis, new_objectives, new_parameters, new_tests


def parse_old_catalog(api: Api) -> Tuple[list, list, list, list, list]:
    """
    Function to parse elements from the old catalog
    :param Api api: RegScale API object
    :return: Tuple containing lists of old catalog elements
    :rtype: Tuple
    """
    with job_progress:
        # add task for retrieving old catalog
        retrieving_old_catalog = job_progress.add_task(
            "[#ef5d23]Retrieving selected catalog from RegScale application instance.",
            total=5,
        )
        # retrieve old catalog security controls
        security_controls = get_old_security_controls(uuid_value=CAT_UUID, api=api)
        old_security_controls = security_controls[0]
        # update the task as complete
        job_progress.update(retrieving_old_catalog, advance=1)
        # retrive old catalog ccis
        old_ccis = security_controls[4]
        # update the task as complete
        job_progress.update(retrieving_old_catalog, advance=1)
        # retrieve old catalog objectives
        old_objectives = security_controls[2]
        # update the task as complete
        job_progress.update(retrieving_old_catalog, advance=1)
        # retrieve old catalog parameters
        old_parameters = security_controls[1]
        # update the task as complete
        job_progress.update(retrieving_old_catalog, advance=1)
        # retrieve old catalog tests
        old_tests = security_controls[3]
        # update the task as complete
        job_progress.update(retrieving_old_catalog, advance=1)

    return old_security_controls, old_ccis, old_objectives, old_parameters, old_tests


def get_new_catalog(url: str) -> list:
    """
    Function to download the catalog from the provided URL
    :param str url: URL to download the catalog from
    :return: dictionary of a catalog
    :rtype: list
    """
    # call curl command to download the catalog
    response = requests.get(url, timeout=60)
    # parse into a dictionary
    new_catalog = response.json()
    # return from the function
    return new_catalog


def get_new_security_controls(ncatalog: dict) -> list:
    """
    Function to parse the downloaded catalog security controls
    :param dict ncatalog: downloaded catalog
    :return: parsed list of new catalog security controls
    :rtype: list
    """
    control_list = []
    for child_control in ncatalog["catalogue"]["securityControls"]:
        control_list.append(child_control)
    for control in control_list:
        del control["tenantsId"]
    return control_list


def get_new_ccis(ncatalog: dict) -> list:
    """
    Function to parse the downloaded catalog ccis
    :param dict ncatalog: downloaded catalog
    :return: parsed list of new catalog ccis
    :rtype: list
    """
    cci_list = []
    for child_cci in ncatalog["catalogue"]["ccis"]:
        cci_list.append(child_cci)
    return cci_list


def get_new_objectives(ncatalog: dict) -> list:
    """
    Function to parse the downloaded catalog objectives
    :param dict ncatalog: downloaded catalog
    :return: parsed list of new catalog objectives
    :rtype: list
    """
    objective_list = []
    for child_objective in ncatalog["catalogue"]["objectives"]:
        objective_list.append(child_objective)
    return objective_list


def get_new_parameters(ncatalog: dict) -> list:
    """
    Function to parse the downloaded catalog parameters
    :param dict ncatalog: downloaded catalog
    :return: parsed list of new catalog parameters
    :rtype: list
    """
    parameter_list = []
    for child_parameter in ncatalog["catalogue"]["parameters"]:
        parameter_list.append(child_parameter)
    return parameter_list


def get_new_tests(ncatalog: dict) -> list:
    """
    Function to parse the downloaded catalog parameters
    :param dict ncatalog: downloaded catalog
    :return: parsed list of new catalog tests
    :rtype: list
    """
    test_list = []
    for child_test in ncatalog["catalogue"]["tests"]:
        test_list.append(child_test)
    return test_list


def get_old_security_controls(
    uuid_value: str, api: Api
) -> Tuple[list, list, list, list, list]:
    """
    Function to retrieve the old catalog security controls from a RegScale instance via API & GraphQL
    :param str uuid_value: UUID of the catalog to retrieve
    :param Api api: RegScale API object
    :return: tuple containing a list for each catalog data element
    :rtype: Tuple[list, list, list, list, list]
    """
    body = """
                query {
                    catalogues(
                        skip: 0
                        take: 50
                        where: { uuid: { eq: "uuid_value" } }
                    ) {
                        items {
                        id
                        }
                        pageInfo {
                        hasNextPage
                        }
                        totalCount
                    }
                    }""".replace(
        "uuid_value", uuid_value
    )
    try:
        catalogue_id = api.graph(query=body)["catalogues"]["items"][0]["id"]
    except (IndexError, KeyError):
        error_and_exit(
            f"Catalog with UUID: {uuid_value} not found in RegScale instance."
        )
    try:
        old_security_controls = api.get(
            url=api.config["domain"]
            + f"/api/SecurityControls/getAllByCatalogWithDetails/{catalogue_id}"
        ).json()
    except JSONDecodeError as ex:
        error_and_exit(f"Unable to retrieve control objectives from RegScale.\n{ex}")
    except TimeoutError:
        error_and_exit(
            "The selected catalog is too large to update, please contact RegScale customer service."
        )
    old_parameters = []
    for control in old_security_controls:
        for parameter in control["parameters"]:
            old_parameters.append(parameter)
    old_objectives = []
    for control in old_security_controls:
        for objective in control["objectives"]:
            old_objectives.append(objective)
    old_tests = []
    for control in old_security_controls:
        for test in control["tests"]:
            old_tests.append(test)
    old_ccis = []
    for control in old_security_controls:
        id_number = control["control"]["id"]
        try:
            ccis = api.get(
                url=api.config["domain"] + f"/api/cci/getByControl/{id_number}"
            ).json()
            if ccis:
                old_ccis.append(ccis)
        except JSONDecodeError as ex:
            error_and_exit(
                f"Unable to retrieve control objectives from RegScale.\n{ex}"
            )

    return old_security_controls, old_parameters, old_objectives, old_tests, old_ccis
