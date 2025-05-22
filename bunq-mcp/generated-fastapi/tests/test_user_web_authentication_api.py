# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_web_authentication import UserWebAuthentication  # noqa: F401
from openapi_server.models.user_web_authentication_create import UserWebAuthenticationCreate  # noqa: F401
from openapi_server.models.user_web_authentication_listing import UserWebAuthenticationListing  # noqa: F401
from openapi_server.models.user_web_authentication_read import UserWebAuthenticationRead  # noqa: F401
from openapi_server.models.user_web_authentication_update import UserWebAuthenticationUpdate  # noqa: F401


def test_c_reate_user_web_authentication(client: TestClient):
    """Test case for c_reate_user_web_authentication

    
    """
    user_web_authentication = {"attachment_uuid":"attachment_uuid","type":"type","redirect_url":"redirect_url","status":"status"}

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
    #    "/user-web-authentication",
    #    headers=headers,
    #    json=user_web_authentication,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_web_authentication(client: TestClient):
    """Test case for list_all_user_web_authentication

    
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
    #    "/user-web-authentication",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_user_web_authentication(client: TestClient):
    """Test case for r_ead_user_web_authentication

    
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
    #    "/user-web-authentication/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_web_authentication(client: TestClient):
    """Test case for u_pdate_user_web_authentication

    
    """
    user_web_authentication = {"attachment_uuid":"attachment_uuid","type":"type","redirect_url":"redirect_url","status":"status"}

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
    #    "PUT",
    #    "/user-web-authentication/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=user_web_authentication,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

