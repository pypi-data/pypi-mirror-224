#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Dataclass for a RegScale Component """

# standard python imports
from dataclasses import dataclass

from regscale.core.app.api import Api
from regscale.core.app.application import Application


@dataclass
class Component:
    """Component Model"""

    title: str
    description: str
    componentType: str
    componentOwnerId: str
    purpose: str = None
    securityPlansId: int = None
    cmmcAssetType: str = None
    createdBy: str = None
    createdById: str = None
    dateCreated: str = None
    lastUpdatedBy: str = None
    lastUpdatedById: str = None
    dateLastUpdated: str = None
    status: str = "Active"
    uuid: str = None
    componentOwner: str = None
    cmmcExclusion: str = False
    id: int = None
    isPublic: str = True

    def __getitem__(self, key: any) -> any:
        """
        Get attribute from Pipeline
        :param any key:
        :return: value of provided key
        :rtype: any
        """
        if getattr(self, key) == "None":
            return None
        return getattr(self, key)

    def __setitem__(self, key: any, value: any) -> None:
        """
        Set attribute in Pipeline with provided key
        :param any key: Key to change to provided value
        :param any value: New value for provided Key
        :return: None
        """
        return setattr(self, key, value)

    @staticmethod
    def get_components_from_ssp(app: Application, ssp_id: int) -> list[dict]:
        """Get all components for a given SSP

        :param app: Application instance
        :param ssp_id: RegScale SSP
        :return: List of component dictionaries
        """
        api = Api(app)
        existing_res = api.get(
            app.config["domain"] + f"/api/components/getAllByParent/{ssp_id}"
        )
        if not existing_res.raise_for_status():
            return existing_res.json()
