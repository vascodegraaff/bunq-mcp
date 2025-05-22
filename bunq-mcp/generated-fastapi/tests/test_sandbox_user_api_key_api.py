# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.sandbox_user_api_key import SandboxUserApiKey  # noqa: F401
from openapi_server.models.sandbox_user_api_key_create import SandboxUserApiKeyCreate  # noqa: F401
from openapi_server.models.sandbox_user_api_key_listing import SandboxUserApiKeyListing  # noqa: F401


def test_c_reate_sandbox_user_api_key_for_user_developer_portal_user_profile(client: TestClient):
    """Test case for c_reate_sandbox_user_api_key_for_user_developer_portal_user_profile

    
    """
    sandbox_user_api_key = {"type":"type"}

    headers = {
        "cache_control": 'cache_control_example',
        "user_agent": 'user_agent_example',
        "x_bunq_language": 'x_bunq_language_example',
        "x_bunq_region": 'x_bunq_region_example',
        "x_bunq_client_request_id": 'x_bunq_client_request_id_example',
        "x_bunq_geolocation": 'x_bunq_geolocation_example',
        "x_bunq_client_authentication": 'x_bunq_client_authentication_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/user/{userID}/developer-portal-user-profile/{developer-portal-user-profileID}/sandbox-user-api-key".format(userID=56, developer-portal-user-profileID=56),
    #    headers=headers,
    #    json=sandbox_user_api_key,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_sandbox_user_api_key_for_user_developer_portal_user_profile(client: TestClient):
    """Test case for d_elete_sandbox_user_api_key_for_user_developer_portal_user_profile

    
    """

    headers = {
        "cache_control": 'cache_control_example',
        "user_agent": 'user_agent_example',
        "x_bunq_language": 'x_bunq_language_example',
        "x_bunq_region": 'x_bunq_region_example',
        "x_bunq_client_request_id": 'x_bunq_client_request_id_example',
        "x_bunq_geolocation": 'x_bunq_geolocation_example',
        "x_bunq_client_authentication": 'x_bunq_client_authentication_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/user/{userID}/developer-portal-user-profile/{developer-portal-user-profileID}/sandbox-user-api-key/{itemId}".format(userID=56, developer-portal-user-profileID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_sandbox_user_api_key_for_user_developer_portal_user_profile(client: TestClient):
    """Test case for list_all_sandbox_user_api_key_for_user_developer_portal_user_profile

    
    """

    headers = {
        "cache_control": 'cache_control_example',
        "user_agent": 'user_agent_example',
        "x_bunq_language": 'x_bunq_language_example',
        "x_bunq_region": 'x_bunq_region_example',
        "x_bunq_client_request_id": 'x_bunq_client_request_id_example',
        "x_bunq_geolocation": 'x_bunq_geolocation_example',
        "x_bunq_client_authentication": 'x_bunq_client_authentication_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/user/{userID}/developer-portal-user-profile/{developer-portal-user-profileID}/sandbox-user-api-key".format(userID=56, developer-portal-user-profileID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

