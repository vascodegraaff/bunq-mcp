# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_user_credential_password_ip import AdminUserCredentialPasswordIp  # noqa: F401
from openapi_server.models.admin_user_credential_password_ip_listing import AdminUserCredentialPasswordIpListing  # noqa: F401
from openapi_server.models.admin_user_credential_password_ip_read import AdminUserCredentialPasswordIpRead  # noqa: F401
from openapi_server.models.admin_user_credential_password_ip_update import AdminUserCredentialPasswordIpUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_list_all_admin_user_credential_password_ip_for_user(client: TestClient):
    """Test case for list_all_admin_user_credential_password_ip_for_user

    
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
    #    "/user/{userID}/admin-user-credential-password-ip".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_user_credential_password_ip_for_user(client: TestClient):
    """Test case for r_ead_admin_user_credential_password_ip_for_user

    
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
    #    "/user/{userID}/admin-user-credential-password-ip/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_user_credential_password_ip_for_user(client: TestClient):
    """Test case for u_pdate_admin_user_credential_password_ip_for_user

    
    """
    admin_user_credential_password_ip = {"status":"status"}

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
    #    "/user/{userID}/admin-user-credential-password-ip/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=admin_user_credential_password_ip,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

