# Copyright 2021-2023 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
import base64
import hashlib
import json
import logging
import os
import urllib
from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Optional

import tornado
from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
from oauthlib.oauth2 import WebApplicationClient
from requests_oauthlib import OAuth2Session
from tornado import escape
from tornado import httpclient
from tornado.auth import OAuth2Mixin
from tornado.httputil import url_concat
from tornado.web import RequestHandler
from vdk.plugin.control_api_auth.auth_request_values import AuthRequestValues
from vdk.plugin.control_api_auth.authentication import Authentication
from vdk.plugin.control_api_auth.autorization_code_auth import generate_pkce_codes
from vdk.plugin.control_api_auth.autorization_code_auth import RedirectAuthentication

from .job_data import JobDataLoader
from .vdk_options.vdk_options import VdkOption
from .vdk_ui import VdkUI

log = logging.getLogger(__name__)


class LoadJobDataHandler(APIHandler):
    """
    Class responsible for handling POST request for retrieving data(full path, job's name and team)
     about job of directory
     Response: return a json formatted str providing the data about the job
    """

    @tornado.web.authenticated
    def post(self):
        working_directory = json.loads(self.get_json_body())[VdkOption.PATH.value]
        try:
            data = JobDataLoader(working_directory)
            self.finish(
                json.dumps(
                    {
                        VdkOption.PATH.value: data.get_job_path(),
                        VdkOption.NAME.value: data.get_job_name(),
                        VdkOption.TEAM.value: data.get_team_name(),
                    }
                )
            )
        except Exception as e:
            log.debug(
                f"Failed to load job information from config.ini with error: {e}."
            )
            self.finish(
                json.dumps(
                    {
                        VdkOption.PATH.value: "",
                        VdkOption.NAME.value: "",
                        VdkOption.TEAM.value: "",
                    }
                )
            )


class RunJobHandler(APIHandler):
    """
    Class responsible for handling POST request for running a Data Job given its path and arguments to run with
    Response: return a json formatted str including:
     ::error field with error message if an error exists
     ::message field with status of the VDK operation
    """

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        run_result = VdkUI.run_job(
            input_data[VdkOption.PATH.value],
            input_data[VdkOption.ARGUMENTS.value],
        )
        self.finish(json.dumps(run_result))


class DeleteJobHandler(APIHandler):
    """
    Class responsible for handling POST request for deleting a Data Job given its name, team and Rest API URL
    Response: return a json formatted str including:
        ::error field with error message if an error exists
        ::message field with status of the Vdk operation
    """

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        try:
            status = VdkUI.delete_job(
                input_data[VdkOption.NAME.value], input_data[VdkOption.TEAM.value]
            )
            self.finish(json.dumps({"message": f"{status}", "error": ""}))
        except Exception as e:
            self.finish(json.dumps({"message": f"{e}", "error": "true"}))


class DownloadJobHandler(APIHandler):
    """
    Class responsible for handling POST request for downloading a Data Job given its name, team,
    Rest API URL, and the path to where the job will be downloaded
    Response: return a json formatted str including:
        ::error field with error message if an error exists
        ::message field with status of the Vdk operation
    """

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        try:
            status = VdkUI.download_job(
                input_data[VdkOption.NAME.value],
                input_data[VdkOption.TEAM.value],
                input_data[VdkOption.PATH.value],
            )
            self.finish(json.dumps({"message": f"{status}", "error": ""}))
        except Exception as e:
            self.finish(json.dumps({"message": f"{e}", "error": "true"}))


class ConvertJobHandler(APIHandler):
    """
    Class responsible for handling POST request for transforming a directory type Data job(with .py and .sql files)
    to a notebook type data job
    """

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        try:
            message = json.dumps(VdkUI.convert_job(input_data[VdkOption.PATH.value]))
            self.finish(json.dumps({"message": f"{message}", "error": ""}))
        except Exception as e:
            self.finish(json.dumps({"message": f"{e}", "error": "true"}))


class CreateJobHandler(APIHandler):
    """
    Class responsible for handling POST request for creating a Data Job given its name, team,
    flags whether it will be created locally or in the cloud, path to where job will be created (if local),
    Rest API URL (if cloud)
    Response: return a json formatted str including:
        ::error field with error message if an error exists
        ::message field with status of the Vdk operation
    """

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        try:
            status = VdkUI.create_job(
                input_data[VdkOption.NAME.value],
                input_data[VdkOption.TEAM.value],
                input_data[VdkOption.PATH.value],
            )
            self.finish(json.dumps({"message": f"{status}", "error": ""}))
        except Exception as e:
            self.finish(json.dumps({"message": f"{e}", "error": "true"}))


class CreateDeploymentHandler(APIHandler):
    """
    Class responsible for handling POST request for creating a deployment of  Data Job given its name, team, path,
    Rest API URL, deployment reason and flag whether it is enabled (that will basically un-pause the job)
    Response: return a json formatted str including:
        ::error field with error message if an error exists
        ::message field with status of the Vdk operation
    """

    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        try:
            status = VdkUI.create_deployment(
                input_data[VdkOption.NAME.value],
                input_data[VdkOption.TEAM.value],
                input_data[VdkOption.PATH.value],
                input_data[VdkOption.DEPLOYMENT_REASON.value],
            )
            self.finish(json.dumps({"message": f"{status}", "error": ""}))
        except Exception as e:
            self.finish(json.dumps({"message": f"{e}", "error": "true"}))


class GetNotebookInfoHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        notebook_info = VdkUI.get_notebook_info(
            input_data["cellId"], input_data[VdkOption.PATH.value]
        )
        self.finish(json.dumps(notebook_info))


class GetVdkCellIndicesHandler(APIHandler):
    @tornado.web.authenticated
    def post(self):
        input_data = self.get_json_body()
        vdk_indices = VdkUI.get_vdk_tagged_cell_indices(input_data["nbPath"])
        self.finish(json.dumps(vdk_indices))


class GetServerPathHandler(APIHandler):
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps(os.getcwd()))


class OAuth2Handler(APIHandler, OAuth2Mixin):
    _OAUTH_AUTHORIZE_URL = "https://authserver.io/uas/oauth2/authorization"
    _OAUTH_ACCESS_TOKEN_URL = "https://authserver.io/uas/oauth2/token"

    @tornado.web.authenticated
    def get(self):
        self.finish(
            json.dumps(
                {
                    "message": {str(k): str(v) for k, v in os.environ.items()},
                    "error": "",
                }
            )
        )


class GoogleOAuth2LoginHandler(APIHandler):
    def _oauth_request_token_url(
        self,
        redirect_uri: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        code: Optional[str] = None,
        extra_params: Optional[Dict[str, Any]] = None,
    ) -> str:
        url = self._OAUTH_ACCESS_TOKEN_URL  # type: ignore
        args = {}  # type: Dict[str, str]
        if redirect_uri is not None:
            args["redirect_uri"] = redirect_uri
        if code is not None:
            args["code"] = code
        if client_id is not None:
            args["client_id"] = client_id
        if client_secret is not None:
            args["client_secret"] = client_secret
        if extra_params:
            args.update(extra_params)
        return url_concat(url, args)

    def get_auth_http_client(self) -> httpclient.AsyncHTTPClient:
        """Returns the `.AsyncHTTPClient` instance to be used for auth requests.

        May be overridden by subclasses to use an HTTP client other than
        the default.

        .. versionadded:: 4.3
        """
        return httpclient.AsyncHTTPClient()

    def get(self):
        redirect_uri = self.request.full_url()
        log.info(f"redirect uri is {redirect_uri}")
        redirect_uri = "http://127.0.0.1:8888/vdk-jupyterlab-extension/login"

        if self.get_argument("code", None):
            # user = await self.get_authenticated_user(
            #     redirect_uri=redirect_uri,
            #     code=self.get_argument('code'))
            # # Save the user with e.g. set_signed_cookie
            # log.debug(user)
            log.info("Received authorization code: %s" % self.get_argument("code"))
            log.info(self.request)
            initial_url = self.get_argument("state", "")
            if initial_url:
                self.redirect(initial_url, permanent=True)
        else:
            client_id = "r5FW5u5QVsbowS4kVaGtA0BZZc2xIk8hquf"
            oauth2_discovery_url = (
                "https://console.cloud.vmware.com/csp/gateway/discovery"
            )
            oauth2_exchange_url = (
                "https://console.cloud.vmware.com/csp/gateway/am/api/auth/authorize"
            )

            (
                code_verifier,
                code_challenge,
                code_challenge_method,
            ) = generate_pkce_codes()

            self.set_secure_cookie("code_verifier", code_verifier)

            oauth = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
            authorization_url = oauth.authorization_url(
                oauth2_discovery_url,
                state=self.get_argument("initial_url", ""),
                prompt=AuthRequestValues.LOGIN_PROMPT.value,
                code_challenge=code_challenge,
                code_challenge_method=code_challenge_method,
            )[0]

            self.finish(authorization_url)


def setup_handlers(web_app):
    host_pattern = ".*$"
    base_url = web_app.settings["base_url"]

    def add_handler(handler, endpoint):
        job_route_pattern = url_path_join(
            base_url, "vdk-jupyterlab-extension", endpoint
        )
        job_handlers = [(job_route_pattern, handler)]
        web_app.add_handlers(host_pattern, job_handlers)

    add_handler(GoogleOAuth2LoginHandler, "login")
    add_handler(RunJobHandler, "run")
    add_handler(DeleteJobHandler, "delete")
    add_handler(DownloadJobHandler, "download")
    add_handler(ConvertJobHandler, "convertJobToNotebook")
    add_handler(CreateJobHandler, "create")
    add_handler(LoadJobDataHandler, "job")
    add_handler(CreateDeploymentHandler, "deploy")
    add_handler(GetNotebookInfoHandler, "notebook")
    add_handler(GetVdkCellIndicesHandler, "vdkCellIndices")
    add_handler(GetServerPathHandler, "serverPath")
