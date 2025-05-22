# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_property_permission import AdminPropertyPermission  # noqa: F401
from openapi_server.models.admin_property_permission_create import AdminPropertyPermissionCreate  # noqa: F401
from openapi_server.models.admin_property_permission_listing import AdminPropertyPermissionListing  # noqa: F401
from openapi_server.models.admin_property_permission_read import AdminPropertyPermissionRead  # noqa: F401
from openapi_server.models.admin_property_permission_update import AdminPropertyPermissionUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_property_permission_for_user_admin_permission(client: TestClient):
    """Test case for c_reate_property_permission_for_user_admin_permission

    
    """
    admin_property_permission = {"access_level":"access_level","property_path":"property_path","status":"status"}

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
    #    "/user/{userID}/admin-permission/{admin-permissionID}/property-permission".format(userID=56, admin-permissionID=56),
    #    headers=headers,
    #    json=admin_property_permission,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_property_permission_for_user_admin_permission(client: TestClient):
    """Test case for d_elete_property_permission_for_user_admin_permission

    
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
    #    "/user/{userID}/admin-permission/{admin-permissionID}/property-permission/{itemId}".format(userID=56, admin-permissionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_property_permission_for_user_admin_permission(client: TestClient):
    """Test case for list_all_property_permission_for_user_admin_permission

    
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
    #    "/user/{userID}/admin-permission/{admin-permissionID}/property-permission".format(userID=56, admin-permissionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_property_permission_for_user_admin_permission(client: TestClient):
    """Test case for r_ead_property_permission_for_user_admin_permission

    
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
    #    "/user/{userID}/admin-permission/{admin-permissionID}/property-permission/{itemId}".format(userID=56, admin-permissionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_property_permission_for_user_admin_permission(client: TestClient):
    """Test case for u_pdate_property_permission_for_user_admin_permission

    
    """
    admin_property_permission = {"access_level":"access_level","property_path":"property_path","status":"status"}

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
    #    "/user/{userID}/admin-permission/{admin-permissionID}/property-permission/{itemId}".format(userID=56, admin-permissionID=56, itemId=56),
    #    headers=headers,
    #    json=admin_property_permission,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

