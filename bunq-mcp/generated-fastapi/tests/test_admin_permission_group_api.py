# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_permission_group import AdminPermissionGroup  # noqa: F401
from openapi_server.models.admin_permission_group_create import AdminPermissionGroupCreate  # noqa: F401
from openapi_server.models.admin_permission_group_listing import AdminPermissionGroupListing  # noqa: F401
from openapi_server.models.admin_permission_group_read import AdminPermissionGroupRead  # noqa: F401
from openapi_server.models.admin_permission_group_update import AdminPermissionGroupUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_permission_group_for_user_admin_group(client: TestClient):
    """Test case for c_reate_admin_permission_group_for_user_admin_group

    
    """
    admin_permission_group = {"object_name":"object_name","action":"action","api":"api","status":"status"}

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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-group".format(userID=56, admin-groupID=56),
    #    headers=headers,
    #    json=admin_permission_group,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_admin_permission_group_for_user_admin_group(client: TestClient):
    """Test case for d_elete_admin_permission_group_for_user_admin_group

    
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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-group/{itemId}".format(userID=56, admin-groupID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_permission_group_for_user_admin_group(client: TestClient):
    """Test case for list_all_admin_permission_group_for_user_admin_group

    
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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-group".format(userID=56, admin-groupID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_permission_group_for_user_admin_group(client: TestClient):
    """Test case for r_ead_admin_permission_group_for_user_admin_group

    
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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-group/{itemId}".format(userID=56, admin-groupID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_permission_group_for_user_admin_group(client: TestClient):
    """Test case for u_pdate_admin_permission_group_for_user_admin_group

    
    """
    admin_permission_group = {"object_name":"object_name","action":"action","api":"api","status":"status"}

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
    #    "/user/{userID}/admin-group/{admin-groupID}/admin-permission-group/{itemId}".format(userID=56, admin-groupID=56, itemId=56),
    #    headers=headers,
    #    json=admin_permission_group,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

