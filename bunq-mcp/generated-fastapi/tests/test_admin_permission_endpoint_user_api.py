# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_permission_endpoint_user import AdminPermissionEndpointUser  # noqa: F401
from openapi_server.models.admin_permission_endpoint_user_create import AdminPermissionEndpointUserCreate  # noqa: F401
from openapi_server.models.admin_permission_endpoint_user_listing import AdminPermissionEndpointUserListing  # noqa: F401
from openapi_server.models.admin_permission_endpoint_user_read import AdminPermissionEndpointUserRead  # noqa: F401
from openapi_server.models.admin_permission_endpoint_user_update import AdminPermissionEndpointUserUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_permission_endpoint_user_for_user(client: TestClient):
    """Test case for c_reate_admin_permission_endpoint_user_for_user

    
    """
    admin_permission_endpoint_user = {"alias_user_owner":{"service":"service","name":"name","type":"type","value":"value"},"method":"method","api_type":"api_type","endpoint_name":"endpoint_name","status":"status"}

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
    #    "/user/{userID}/admin-permission-endpoint-user".format(userID=56),
    #    headers=headers,
    #    json=admin_permission_endpoint_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_admin_permission_endpoint_user_for_user(client: TestClient):
    """Test case for d_elete_admin_permission_endpoint_user_for_user

    
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
    #    "/user/{userID}/admin-permission-endpoint-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_permission_endpoint_user_for_user(client: TestClient):
    """Test case for list_all_admin_permission_endpoint_user_for_user

    
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
    #    "/user/{userID}/admin-permission-endpoint-user".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_permission_endpoint_user_for_user(client: TestClient):
    """Test case for r_ead_admin_permission_endpoint_user_for_user

    
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
    #    "/user/{userID}/admin-permission-endpoint-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_permission_endpoint_user_for_user(client: TestClient):
    """Test case for u_pdate_admin_permission_endpoint_user_for_user

    
    """
    admin_permission_endpoint_user = {"alias_user_owner":{"service":"service","name":"name","type":"type","value":"value"},"method":"method","api_type":"api_type","endpoint_name":"endpoint_name","status":"status"}

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
    #    "/user/{userID}/admin-permission-endpoint-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=admin_permission_endpoint_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

