# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.permitted_ip import PermittedIp  # noqa: F401
from openapi_server.models.permitted_ip_create import PermittedIpCreate  # noqa: F401
from openapi_server.models.permitted_ip_listing import PermittedIpListing  # noqa: F401
from openapi_server.models.permitted_ip_read import PermittedIpRead  # noqa: F401
from openapi_server.models.permitted_ip_update import PermittedIpUpdate  # noqa: F401


def test_c_reateip_for_user_credential_password_ip(client: TestClient):
    """Test case for c_reateip_for_user_credential_password_ip

    
    """
    permitted_ip = {"ip":"ip","status":"status"}

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
    #    "/user/{userID}/credential-password-ip/{credential-password-ipID}/ip".format(userID=56, credential-password-ipID=56),
    #    headers=headers,
    #    json=permitted_ip,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_ip_for_user_credential_password_ip(client: TestClient):
    """Test case for list_all_ip_for_user_credential_password_ip

    
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
    #    "/user/{userID}/credential-password-ip/{credential-password-ipID}/ip".format(userID=56, credential-password-ipID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_eadip_for_user_credential_password_ip(client: TestClient):
    """Test case for r_eadip_for_user_credential_password_ip

    
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
    #    "/user/{userID}/credential-password-ip/{credential-password-ipID}/ip/{itemId}".format(userID=56, credential-password-ipID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdateip_for_user_credential_password_ip(client: TestClient):
    """Test case for u_pdateip_for_user_credential_password_ip

    
    """
    permitted_ip = {"ip":"ip","status":"status"}

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
    #    "/user/{userID}/credential-password-ip/{credential-password-ipID}/ip/{itemId}".format(userID=56, credential-password-ipID=56, itemId=56),
    #    headers=headers,
    #    json=permitted_ip,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

