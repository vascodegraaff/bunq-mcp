# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_admin_status_daily import UserAdminStatusDaily  # noqa: F401
from openapi_server.models.user_admin_status_daily_create import UserAdminStatusDailyCreate  # noqa: F401
from openapi_server.models.user_admin_status_daily_listing import UserAdminStatusDailyListing  # noqa: F401
from openapi_server.models.user_admin_status_daily_read import UserAdminStatusDailyRead  # noqa: F401
from openapi_server.models.user_admin_status_daily_update import UserAdminStatusDailyUpdate  # noqa: F401


def test_c_reate_status_daily_for_user_admin(client: TestClient):
    """Test case for c_reate_status_daily_for_user_admin

    
    """
    user_admin_status_daily = {"recipient":[{"recipient_id":1},{"recipient_id":1}],"content":"content","status":"status"}

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
    #    "/user-admin/{user-adminID}/status-daily".format(user-adminID=56),
    #    headers=headers,
    #    json=user_admin_status_daily,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_status_daily_for_user_admin(client: TestClient):
    """Test case for list_all_status_daily_for_user_admin

    
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
    #    "/user-admin/{user-adminID}/status-daily".format(user-adminID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_status_daily_for_user_admin(client: TestClient):
    """Test case for r_ead_status_daily_for_user_admin

    
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
    #    "/user-admin/{user-adminID}/status-daily/{itemId}".format(user-adminID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_status_daily_for_user_admin(client: TestClient):
    """Test case for u_pdate_status_daily_for_user_admin

    
    """
    user_admin_status_daily = {"recipient":[{"recipient_id":1},{"recipient_id":1}],"content":"content","status":"status"}

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
    #    "/user-admin/{user-adminID}/status-daily/{itemId}".format(user-adminID=56, itemId=56),
    #    headers=headers,
    #    json=user_admin_status_daily,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

