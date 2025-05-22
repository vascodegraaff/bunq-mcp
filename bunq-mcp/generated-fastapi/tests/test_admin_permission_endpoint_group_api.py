# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_permission_endpoint_group import AdminPermissionEndpointGroup  # noqa: F401
from openapi_server.models.admin_permission_endpoint_group_create import AdminPermissionEndpointGroupCreate  # noqa: F401
from openapi_server.models.admin_permission_endpoint_group_listing import AdminPermissionEndpointGroupListing  # noqa: F401
from openapi_server.models.admin_permission_endpoint_group_read import AdminPermissionEndpointGroupRead  # noqa: F401
from openapi_server.models.admin_permission_endpoint_group_update import AdminPermissionEndpointGroupUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_permission_endpoint_group_for_user_admin_group(client: TestClient):
    """Test case for c_reate_admin_permission_endpoint_group_for_user_admin_group

    
    """
    admin_permission_endpoint_group = {"method":"method","api_type":"api_type","endpoint_name":"endpoint_name","status":"status"}

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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-endpoint-group".format(userID=56, admin-groupID=56),
    #    headers=headers,
    #    json=admin_permission_endpoint_group,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_admin_permission_endpoint_group_for_user_admin_group(client: TestClient):
    """Test case for d_elete_admin_permission_endpoint_group_for_user_admin_group

    
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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-endpoint-group/{itemId}".format(userID=56, admin-groupID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_permission_endpoint_group_for_user_admin_group(client: TestClient):
    """Test case for list_all_admin_permission_endpoint_group_for_user_admin_group

    
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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-endpoint-group".format(userID=56, admin-groupID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_permission_endpoint_group_for_user_admin_group(client: TestClient):
    """Test case for r_ead_admin_permission_endpoint_group_for_user_admin_group

    
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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-endpoint-group/{itemId}".format(userID=56, admin-groupID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_permission_endpoint_group_for_user_admin_group(client: TestClient):
    """Test case for u_pdate_admin_permission_endpoint_group_for_user_admin_group

    
    """
    admin_permission_endpoint_group = {"method":"method","api_type":"api_type","endpoint_name":"endpoint_name","status":"status"}

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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-endpoint-group/{itemId}".format(userID=56, admin-groupID=56, itemId=56),
    #    headers=headers,
    #    json=admin_permission_endpoint_group,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

