#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" standard python imports """
import dataclasses
import os
import re
from enum import Enum
from pathlib import PosixPath
from typing import Any

from requests import JSONDecodeError
from xmltodict import parse

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.models.regscale_models.checklist import Checklist
from regscale.models.regscale_models.components import Component
from regscale.models.regscale_models.implementation_objective import (
    ImplementationObjective,
)
from regscale.models.regscale_models.implementation_option import ImplementationOption


class Status(Enum):
    """
    Map STIG Status
    :param Enum: Enum
    """

    NOT_REVIEWED = "Not Reviewed"  # Create POAM
    OPEN = "Open"  # Create POAM
    NOTAFINDING = "Not A Finding"  # Pass
    NOT_APPLICABLE = "Not Applicable"  # Pass


class Severity(Enum):
    """
    Map STIG Severity to RegScale
    :param Enum: Enum
    """

    HIGH = "I - High - Significant Deficiency"
    MEDIUM = "II - Moderate - Reportable Condition"
    LOW = "III - Low - Other Weakness"


class STIG_FILE:
    """CKL File Processing to RegScale"""

    def __init__(
        self,
        file_path: PosixPath,
        ssp_id: int,
        mapping: dict,
        control_objectives: list,
        security_controls: list,
        assets: list = [],
        app: Application = None,
    ):
        logger = create_logger(propagate=True)
        self.logger = logger
        self.app = app
        self.api = Api(app, timeout=40)
        self.security_controls = security_controls
        self.existing_components = Component.get_components_from_ssp(
            app=self.app, ssp_id=ssp_id
        )
        self.existing_assets = assets
        self.update_assets = []
        self.insert_assets = []
        self.control_objectives = control_objectives
        self.assessed_controls = []
        self.parentids = set()
        self.impids = set()
        self.assets = []
        self.file_path = file_path
        self.mtime = os.path.getmtime(file_path)
        self.obj = self._parse_xml()
        metadata = self.obj["CHECKLIST"]["STIGS"]["iSTIG"]["STIG_INFO"]["SI_DATA"]
        self.metadata = metadata
        platform_objectives = []
        self.platform_objectives = platform_objectives
        self.ssp_id = ssp_id
        self.control_implementations = []
        self.implementation_options = []
        self.cci_mapping = mapping
        dict_data = self._to_dict()
        self.dict_data = dict_data
        self.issue_list = []
        self.existing_checklists = []
        self.update_checklists = []
        self.insert_checklists = []
        self._process_rules()

    def _parse_xml(self) -> dict:
        """
        Convert CKL to dict
        :return: A dictionary with the CKL data
        :rtype: dict
        """

        with open(self.file_path, encoding="utf-8") as file:
            obj = parse(file.read(), dict_constructor=dict)
        return obj

    def _to_dict(self) -> dict:
        """
        Convert xmltodict object to friendly dictionary
        :return: A dictionary with the CKL data
        :rtype: dict
        """

        def extract_value(key: str):
            data = ""
            try:
                dat = [name for name in self.metadata if name["SID_NAME"] == key][0]
                if "SID_DATA" in dat.keys():
                    data = dat["SID_DATA"]
                data = {k.replace('"', ""): v for k, v in dat.items()}
            except IndexError:
                return ""
            return data

        data = {}
        data["Title"] = extract_value("title")
        data["Description"] = extract_value("description")
        data["Version"] = extract_value("version")
        data["Release"] = extract_value("release")
        data["Notice"] = extract_value("notice")
        data["UUID"] = extract_value("uuid")
        data["Source"] = extract_value("source")
        data["Rules"] = self._parse_rules()
        data["StigID"] = extract_value("stigid")
        data["Classification"] = extract_value("classification")
        return data

    def _has_assets(self) -> bool:
        """
        Determine if the CKL has assets
        :return: Whether the CKL has assets
        :rtype: bool
        """
        data = self.obj["CHECKLIST"]["ASSET"]
        if isinstance(data, dict):
            if data["HOST_NAME"] is None:
                self.logger.warning(
                    "%s contains missing asset information, exiting..", self.file_path
                )
                return False
        return True

    def _format_type(self, key, rule) -> str:
        """
        Function to deal with list of str or strings
        :param key: Rule key
        :param rule: Rule dict
        :return: str
        :rtype: concatenated string
        """
        result = ""
        if isinstance(rule, list):
            res = ". ".join(rule)
        elif isinstance(rule, dict):
            res = rule[key]
        elif isinstance(rule, str):
            res = rule
        if isinstance(res, list) and res:
            result = ". ".join(res)
        return result

    def _get_component_id(self, asset_type: str) -> dict:
        """
        Return the component id for the asset type
        :param str asset_type: Asset type (e.g. hardware, software, etc)
        :return: component dictionary
        :rtype: dict
        """
        res = [
            cmp
            for cmp in self.existing_components
            if cmp["componentType"] == asset_type.lower()
        ]
        if res:
            return res[0]

    def _process_rule(self, rule: dict) -> None:
        """
        Process a single rule (from the CKL)
        :param dict rule: CKL rule
        :return: None
        """
        imp_id = None
        ccis = rule["CCI"]
        for cci_info in self._get_control_ids(ccis=ccis):
            control_id = cci_info["ctl_id_main"]
            # security_control_id = self.api.get(url=self.)
            # Match rules to regcale objectives
            if not control_id:
                return
            # Create Component Control if not exists
            if control_id:
                status = "Fail"
                obj_status = "Not Implemented"
                if rule["Status"].lower() == Status.NOTAFINDING.name.lower():
                    status = "Pass"
                    obj_status = "Fully Implemented"
                security_control = [
                    cntrl
                    for cntrl in self.security_controls
                    if cntrl["controlId"] == control_id.upper()
                ][0]
                implementations = self._get_control_implementations(
                    security_control=security_control
                )
                raw_asset = self.obj["CHECKLIST"]["ASSET"]
                assets = [
                    asset.dict()
                    for asset in self.existing_assets
                    if raw_asset["HOST_FQDN"] == asset["name"]
                    or raw_asset["TARGET_KEY"] == asset["otherTrackingNumber"]
                ]
                if not assets:
                    self.logger.warning(
                        "No assets found for %s or %s, skipping rule..",
                        raw_asset["HOST_FQDN"],
                        raw_asset["TARGET_KEY"],
                    )
                    return
                component_id = self._get_component_id(
                    asset_type=assets[0]["assetCategory"]
                )["id"]
                # grab the correct implementation based on asset type and component
                imps = [
                    imp for imp in implementations if imp["parentId"] == component_id
                ]

                if imps:  # and (status.lower() == Status.OPEN.value.lower()):
                    implementation = imps[0]
                    imp_id = implementation["id"]
                    # Assets are loaded, lets update checklists
                    color = (
                        "[#d60202]" if obj_status == "Not Implemented" else "[#02d653]"
                    )
                    self.logger.info(
                        "%s - status: %s%s",
                        ", ".join(ccis),
                        color,
                        obj_status,
                    )
                    # Select Option to update the Implementation Objective (required)
                    comments = self._format_type(rule=rule, key="Comments")
                    finding_details = self._format_type(rule=rule, key="FindingDetails")

                    if not finding_details and status == "Pass":
                        finding_details = "Not a finding"
                    if not finding_details and status == "Fail":
                        finding_details = "An Unknown Error leading to failed check. STIG contains no finding details"

                    for asset in assets:
                        assert asset["id"]
                        for _, cci in enumerate(ccis):
                            checklist = Checklist(
                                assetId=asset["id"],
                                status=status,
                                tool="STIGs",
                                vulnerabilityId=rule["VulnID"],
                                ruleId=rule["RuleID"],
                                cci=cci,
                                baseline=((self.file_path).name).split(".")[0],
                                check=(
                                    rule["RuleTitle"] + "\n" + rule["Check_Content"]
                                ),  # TODO: Where should i implement fix text?
                                results=finding_details,
                                comments=comments,
                            )
                            if checklist.__hash__() not in {
                                Checklist.from_dict(chk).__hash__()
                                for chk in self.existing_checklists
                            }:
                                # Post
                                self.insert_checklists.append(checklist)
                            else:
                                # Update
                                existing_checklist = {
                                    Checklist.from_dict(chk)
                                    for chk in self.existing_checklists
                                    if Checklist.from_dict(chk).__hash__()
                                    == checklist.__hash__()
                                }.pop()
                                checklist.id = existing_checklist.id
                                if checklist.status != existing_checklist.status:
                                    self.update_checklists.append(checklist)
                    self.impids.add(imp_id)

    # end default constructor
    # flake8: noqa: C901
    def _process_rules(self) -> None:
        """
        Convert Stig vulnerabilities/rules to RegScale objects
        :return: None
        """

        for component in self.existing_components:
            self.existing_checklists.extend(Checklist.get_checklists(component["id"]))

        if not self._has_assets():
            return
        self.logger.info("Processing %i rules", len(self.dict_data["Rules"]))
        for rule in self.dict_data["Rules"]:
            self._process_rule(rule)
        self._update_checklists()

    def _update_checklists(self) -> None:
        """
        Update or Insert checklists into RegScale
        :return: None
        """
        if self.update_checklists:
            self.api.post(
                url=self.app.config["domain"] + f"/api/securitychecklist/batchUpdate",
                json=[dataclasses.asdict(chk) for chk in self.update_checklists],
            )
        if self.insert_checklists:
            self.api.post(
                url=self.app.config["domain"] + f"/api/securitychecklist/batchCreate",
                json=[dataclasses.asdict(chk) for chk in self.insert_checklists],
            )

    def _get_saved_implementation_objectives(self, control_id: int) -> list[dict]:
        """
        Return implementation objectives for a given control
        :param control_id: The control id to lookup
        :return: list containing implementation objective matching the control id
        :rtype: list[dict]
        """
        return ImplementationObjective.fetch_implementation_objectives(
            self.app, control_id
        )

    def _control_id_lookup(self, control_name: str) -> int:
        """
        Lookup a control id from a friendly string id. (ex: AC-10)
        :param str control_name: The control name to lookup
        :return: control id
        :rtype: int
        """
        ids = []
        result = None
        try:
            ids = [
                control
                for control in [imp["control"] for imp in self.control_implementations]
                if control["controlId"].lower() == control_name.lower()
            ]
        except (AttributeError, TypeError) as aex:
            self.logger.warning(
                "Unable to find control id for %s\n%s", control_name, aex
            )
            return result
        if ids:
            result = ids[0]["id"]
        return result

    def _get_control_objectives(self, control_id: int) -> list[dict]:
        """
        Return control objectives for a given control ID
        :param int control_id: id to fetch objectives for
        :return: A list of control objectives
        :rtype: list[dict]
        """
        control_objectives = []
        try:
            response = self.api.get(
                self.app.config["domain"]
                + f"/api/controlObjectives/getByControl/{control_id}"
            )
            if not response.raise_for_status():
                control_objectives = response.json()
        except (JSONDecodeError, IndexError) as jex:
            self.logger.error(jex)
        return control_objectives

    def _get_control_ids(self, ccis: list) -> list[dict]:
        """
        Return friendly control id
        :param list ccis: A list of CCIs to lookup
        :return: A list of dict with control id and control name
        :rtype: list[dict]
        """
        # TODO:
        #         [5:07 PM] Greg Elin
        #         A single control in a catalog will have multiple CCIs. Each CCI identfies an explicit "chieck" or "detail" in a control since controls often referred to multiple activities a team needs to do.  Example, a control will say "Organization will define and disseminate access policy to users."  In this case two CCIs exist, one to reference "define access policy" and one to reference "disseminate access policy"
        #         like 1
        #  Example, a control will say "Organization will define and disseminate access policy to users."  In this case two CCIs exist, one to reference "define access policy" and one to reference "disseminate access policy"
        # Awareness training controls, organizational..

        # 99% of the cci-ref entries should be the following form of NIST SP 800-53:
        if ccis is None:
            ccis = {"CCI-000366"}
        return self.cci_mapping[ccis[0]]

    def _gen_notes(self, data: tuple[str, str, str, str, str]) -> str:
        """
        Generate notes section in a similar format to the STIGViewer
            (vuln_id, check_text, fix_text, discussion, rule_title)
        :param data: A tuple of strings
        :return: A formatted string
        :rtype: str
        """
        notes = f"""Vul ID: {data[0]}
                Rule Title: {data[4]}
                Discussion: {data[3]}
                Check Text: {data[1]}
                Fix Text: {data[2]}
                """

        return notes

    def _get_control_implementations(self, security_control: dict) -> list[dict]:
        """
        Lookup or create a control implementation for a given checklist rule
        :param dict security_control: Security Control as a dictionary from RegScale
        :return: List of a Control implementation
        :rtype: list[dict]
        """
        url = self.app.config["domain"] + "/api/controlimplementation"
        control_implementations = []
        component_ids = {asset["parentId"] for asset in self.existing_assets}
        for component_id in component_ids:
            existing_imps_response = self.api.get(
                url=url + f"/getAllByParent/{component_id}/components"
            )
            if existing_imps_response.status_code == 200:  # return 404 on empty
                imp = [
                    imp
                    for imp in existing_imps_response.json()
                    if imp["controlID"] == security_control["id"]
                ]
                if imp:
                    control_implementation = imp[0]
                    control_implementations.append(control_implementation)

        return control_implementations

    def _option_lookup(self, control_id: int) -> list[dict]:
        """
        Fetch implementation options by security control id
        :param int control_id: Security Control ID
        :return: A list of implementation options
        :rtype: list[dict]
        """
        return ImplementationOption.fetch_implementation_options(
            app=self.app, control_id=control_id
        )

    def _attribute_lookup(self, j_array: dict, key: str) -> list:
        """
        Attribute lookup
        :param dict j_array: json object of attributes for a STIG
        :param str key: key to filter STIG attributes
        :return: list of attributes
        :rtype: list
        """
        result = []
        try:
            result = [
                value
                for value in j_array
                if value["VULN_ATTRIBUTE"].lower() == key.lower()
            ]
        except AttributeError as aex:
            self.logger.error("Unable to pull attribute value\n%s", aex)
        return result

    def _process_stig_data(self, info: dict, key: str) -> Any:
        """
        Check data length, if valid return
        :param dict info: A dict of stig information
        :param str key: key to look up in the dictionary
        :return: A list or string with lookup data
        :rtype: Any
        """
        dat = info[key.upper()] if key.upper() in info else None
        try:
            if not dat:
                dat = self._attribute_lookup(info["STIG_DATA"], key)
                if len(dat) > 0:
                    if key == "cci_ref":
                        return [
                            data["ATTRIBUTE_DATA"]
                            for data in dat
                            if "CCI" in data["ATTRIBUTE_DATA"]
                        ]
                    if dat and "ATTRIBUTE_DATA" in dat[0]:
                        return dat[0]["ATTRIBUTE_DATA"]
        except TypeError as ex:
            self.logger.error("Unable to process %s\n%s", key, ex)
        return dat

    def _parse_rules(self) -> list:
        """
        Format the rule data to a simple list.
        :return: list of rules
        :rtype: list
        """
        stig_vulns = self.obj["CHECKLIST"]["STIGS"]["iSTIG"]["VULN"]
        result = []
        for info in stig_vulns:
            if isinstance(info, dict) and "STIG_DATA" in info:
                rule = {
                    "VulnID": "",
                    "RuleID": "",
                    "StigID": "",
                    "Severity": "",
                    "Cat": "",
                    "Classification": "",
                    "GroupTitle": "",
                    "RuleTitle": "",
                    "Description": "",
                    "VulnDiscussion": "",
                    "FalsePositives": "",
                    "FalseNegatives": "",
                    "Documentable": "",
                    "Mitigations": "",
                    "SeverityOverrideGuidance": "",
                    "PotentialImpacts": "",
                    "ThirdPartyTools": "",
                    "MitigationControl": "",
                    "Responsibility": "",
                    "IAControls": "",
                    "CheckText": "",
                    "FixText": "",
                    "CCI": "",
                }
                info["STATUS"].replace("_", " ") if "STATUS" in info else None
                finding_details = (
                    info["FINDING_DETAILS"] if info["FINDING_DETAILS"] else "N/A"
                )
                severity = (
                    self._process_stig_data(info, "severity").upper()
                    if self._process_stig_data(info, "severity")
                    else None
                )
                rule["GroupTitle"] = self._process_stig_data(info, "group_title")
                rule["Check_Content"] = self._process_stig_data(info, "check_content")
                rule["Description"] = self._process_stig_data(info, "description")
                rule["Documentable"] = self._process_stig_data(info, "documentable")
                rule["Mitigations"] = self._process_stig_data(info, "mitigatons")
                rule["PotentialImpacts"] = self._process_stig_data(
                    info, "potential_impact"
                )
                rule["FalsePositives"] = self._process_stig_data(
                    info, "false_positives"
                )
                rule["FalseNegatives"] = self._process_stig_data(
                    info, "false_negatives"
                )
                rule["ThirdPartyTools"] = self._process_stig_data(
                    info, "third_party_tools"
                )
                rule["MitigationControl"] = self._process_stig_data(
                    info, "mitigation_control"
                )
                rule["Responsibility"] = self._process_stig_data(info, "responsibility")
                rule["Status"] = self._process_stig_data(info, "status")
                rule["FindingDetails"] = self._process_stig_data(
                    info, "finding_details"
                )
                rule["Comments"] = self._process_stig_data(info, "comments")
                rule["SecurityOverride"] = self._process_stig_data(
                    info, "security_override"
                )
                rule["SecurityJustification"] = self._process_stig_data(
                    info, "security_justification"
                )
                rule["Severity"] = severity
                rule["VulnID"] = self._process_stig_data(info, "vuln_num")
                rule["RuleTitle"] = self._process_stig_data(info, "rule_title")
                rule["RuleID"] = self._process_stig_data(info, "rule_id")
                rule["IAControls"] = self._process_stig_data(info, "ia_controls")
                rule["StigID"] = self._process_stig_data(info, "stig_id")
                rule["FixText"] = self._process_stig_data(info, "fix_text")
                rule["CheckText"] = self._process_stig_data(info, "check_text")
                rule["CCI"] = self._process_stig_data(
                    info, "cci_ref"
                )  # TODO: handle multiple cci-refs
                rule["Weight"] = self._process_stig_data(info, "weight")
                rule["Classification"] = self._process_stig_data(info, "class")
                rule["SecurityOverrideGuidence"] = self._process_stig_data(
                    info, "security_override_Guidence"
                )
                rule["STIGRef"] = self._process_stig_data(info, "stigref")
                discussion = self._process_stig_data(info, "vuln_discuss")
                rule["VulnDiscussion"] = (
                    discussion if discussion is not None else rule["FixText"]
                )
                if rule["CCI"]:
                    result.append(rule)
        return result

    def oscalize_control_id(self, cl_id) -> Any:
        """
        Output an oscal standard control id from various common formats for control ids
        Source: https://github.com/RegScale/ComponentHub/blob/389347aa8a267aeed96b9b856c66e88c5c1127d9/muse/ComponentTools.py#L218
        :param cl_id: A standard control id
        :return: An oscal control id
        :rtype: str or tuple[str, str]
        """
        # Handle improperly formatted control id
        # Recognize only properly formmated control id:
        #   at-1, at-01, ac-2.3, ac-02.3, ac-2 (3), ac-02 (3), ac-2(3), ac-02 (3),
        # if self.verbose > 1:
        #     print(f" processing cl_id: {cl_id}")
        pattern = re.compile("^[A-Za-z][A-Za-z]-[0-9() .a-z]*$")
        if not pattern.match(cl_id):
            self.logger.error("Problem OSCAL-izing %s", cl_id)
            return "at.4"
        # Handle properly formatted existing id
        # Transform various patterns of control ids into OSCAL format
        # Fix leading zero in at-01, ac-02.3, ac-02 (3)
        cl_id = re.sub(r"^([A-Za-z][A-Za-z]-)0(.*)$", r"\1\2", cl_id)
        # Change paranthesis into a dot
        # Match: AU-3, AU-3 c, IA-5 (1), IA-5 (1) (c), IA-2 (12)
        # TODO: Match pattern: "AC-8 c 1"
        # match = re.match(r'^([A-Za-z][A-Za-z]-)([0-9]*)([ ]*)\(([0-9]*)\)( \(([a-z]*)\))?$', cl_id)
        match = re.match(
            r"^([A-Za-z][A-Za-z]-)([0-9]*)([ ]*[a-z]*)(\(([0-9][0-9]*)\))*( \(([a-z]*)\))?$",
            cl_id,
        )
        # TODO: Need to properly output: IA-5 (1) (c), AC-8 c 1
        cl_id = (
            "".join(filter(None, (match.group(1), match.group(2)))).lower().strip()
            + "."
            + "".join(filter(None, (match.group(4),))).lower().strip()
        )
        cl_pid = "".join(filter(None, (match.group(6),))).lower().strip()
        # Remove trailing space
        cl_id = cl_id.strip(" ").strip(".")
        # Remove paranthesis
        cl_id = re.sub(r"[()]", "", cl_id)
        cl_pid = re.sub(r"[()]", "", cl_pid)
        # Set to lowercase
        cl_id = cl_id.lower()
        return cl_id, cl_pid
