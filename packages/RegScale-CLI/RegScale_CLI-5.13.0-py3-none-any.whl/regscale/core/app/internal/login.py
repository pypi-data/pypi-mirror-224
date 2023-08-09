#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Module to allow user to login to RegScale """


# standard python imports
import contextlib
import os
import sys
from datetime import datetime
from json import JSONDecodeError
from ssl import SSLCertVerificationError
from typing import Optional

import requests

from regscale.core.app.api import Api, normalize_url
from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger

logger = create_logger()


def login(
    str_user: Optional[str] = None,
    str_password: Optional[str] = None,
    host: Optional[str] = None,
    app: Optional[Application] = None,
    token: Optional[str] = None,
    mfa_token: Optional[str] = "",
) -> str:
    """
    Wrapper for Login to RegScale
    :param str str_user: username to log in, defaults to None
    :param str str_password: password of provided user, defaults to None
    :param str host: host to log into, defaults to None
    :param Application app: Application object, defaults to None
    :param str token: a valid JWT token to pass, defaults to None
    :param str mfa_token: a valid MFA token to pass, defaults to ""
    :raises: ValueError if no domain value found in init.yaml
    :raises: TypeError if token or user id doesn't match expected data type
    :raises: SSLCertVerificationError if unable to validate SSL certificate
    :return: JWT Token after authentication
    :rtype: str
    """
    from regscale.models.platform import (
        RegScaleAuth,
    )  # Adding the import here, to avoid a circular import with RegScaleAuth.get_token.

    config = app.config if app else None
    if config and token:
        if verify_token(Api(app), token):
            config["token"] = token
            app.save_config(conf=config)
            logger.info("RegScale Token has been saved in init.yaml")
            return token
        else:
            logger.error("Invalid token provided.")
            sys.exit(1)
    if str_user and str_password:
        if config and "REGSCALE_DOMAIN" not in os.environ and host is None:
            host = config["domain"]
        regscale_auth = RegScaleAuth.authenticate(
            username=str_user, password=str_password, domain=host
        )
    else:
        regscale_auth = RegScaleAuth.authenticate()
    if config and config["domain"] is None:
        raise ValueError("No domain set in the initialization file.")
    if config and config["domain"] == "":
        raise ValueError("The domain is blank in the initialization file.")

    # create object to authenticate
    auth = {
        "userName": regscale_auth.username,
        "password": regscale_auth.password.get_secret_value(),
        "oldPassword": "",
        "mfaToken": mfa_token,
    }
    if auth["password"]:
        try:
            # update init file from login
            if config:
                config["token"] = regscale_auth.token
                config["userId"] = regscale_auth.user_id
                # write the changes back to file
                app.save_config(config)
            # set variables
            logger.info("User ID: %s", regscale_auth.user_id)
            logger.info("New RegScale Token has been updated and saved in init.yaml")
            logger.debug("Token: %s", regscale_auth.token)
        except TypeError as ex:
            logger.error("TypeError: %s", ex)
        except SSLCertVerificationError as sslex:
            logger.error(
                "SSLError, python requests requires a valid ssl certificate.\n%s", sslex
            )
            sys.exit(1)
    return regscale_auth.token


def is_valid(host: Optional[str] = None, app: Optional[Application] = None) -> bool:
    """
    Quick endpoint to check login status
    :param str host: host to verify login, defaults to None
    :param Application app: Application object, defaults to None
    :raises: KeyError if token key not found in application config
    :raises: ConnectionError if unable to login user to RegScale
    :raises: JSONDecodeError if API response cannot be converted to a json object
    :return: Boolean if user is logged in or not
    :rtype: bool
    """
    config = app.config
    login_status = False
    api = Api(app=app)
    try:
        # Make sure url isn't default
        # login with token
        token = config["token"]
        headers = {"Authorization": token}
        if host is None:
            url_login = normalize_url(
                url=f'{config["domain"]}/api/logging/filterLogs/0/0'
            )
        else:
            url_login = normalize_url(url=f"{host}/api/logging/filterLogs/0/0")
        logger.debug("config: %s", config)
        logger.debug("is_valid url: %s", url_login)
        logger.debug("is_valid headers: %s", headers)
        if response := api.get(url=url_login, headers=headers):
            if response.status_code == 200:
                login_status = True
    except KeyError as ex:
        if str(ex).replace("'", "") == "token":
            logger.debug("Token is missing, we will generate this")
    except ConnectionError:
        logger.error(
            "ConnectionError: Unable to login user to RegScale, check the server domain."
        )
    except JSONDecodeError as decode_ex:
        logger.error(
            "Login Error: Unable to login user to RegScale instance:  %s.\n%s",
            config["domain"],
            decode_ex,
        )
    finally:
        logger.debug("login status: %s", login_status)
    return login_status


def is_licensed(app: Application) -> bool:
    """
    Verify if the application is licensed
    :param Application app: Application object
    :return: License status
    :rtype: bool
    """
    status = False
    api = Api(app=app)
    # TODO: Need to account for versions of the API with no license endpoint
    with contextlib.suppress(requests.RequestException):
        lic = app.get_regscale_license(appl=app, api=api).json()
        license_date = datetime.strptime(lic["expirationDate"], "%Y-%m-%d")
        if lic["licenseType"] == "Enterprise" and license_date > datetime.now():
            status = True
    return status


def verify_token(app: Application, token: str) -> bool:
    """
    Function to verify if the provided JWT for RegScale is valid
    :param Application app: Application object
    :param str token: the JWT to verify
    :return: Boolean if the token is valid or not
    :rtype: bool
    """
    api = Api(app=app)
    response = api.get(
        url=f"{app.config['domain']}/api/authentication/validateToken/{token}"
    )
    return response.status_code == 200
