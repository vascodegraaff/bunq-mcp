# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.whitelist_sdd_recurring import WhitelistSddRecurring  # noqa: F401
from openapi_server.models.whitelist_sdd_recurring_create import WhitelistSddRecurringCreate  # noqa: F401
from openapi_server.models.whitelist_sdd_recurring_listing import WhitelistSddRecurringListing  # noqa: F401
from openapi_server.models.whitelist_sdd_recurring_read import WhitelistSddRecurringRead  # noqa: F401
from openapi_server.models.whitelist_sdd_recurring_update import WhitelistSddRecurringUpdate  # noqa: F401


def test_c_reate_whitelist_sdd_recurring_for_user(client: TestClient):
    """Test case for c_reate_whitelist_sdd_recurring_for_user

    
    """
    whitelist_sdd_recurring = {"maximum_amount_per_payment":{"currency":"currency","value":"value"},"routing_type":"routing_type","maximum_amount_per_month":{"currency":"currency","value":"value"},"monetary_account_paying_id":0,"request_id":6}

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
    #    "/user/{userID}/whitelist-sdd-recurring".format(userID=56),
    #    headers=headers,
    #    json=whitelist_sdd_recurring,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_whitelist_sdd_recurring_for_user(client: TestClient):
    """Test case for d_elete_whitelist_sdd_recurring_for_user

    
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
    #    "/user/{userID}/whitelist-sdd-recurring/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_whitelist_sdd_recurring_for_user(client: TestClient):
    """Test case for list_all_whitelist_sdd_recurring_for_user

    
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
    #    "/user/{userID}/whitelist-sdd-recurring".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_whitelist_sdd_recurring_for_user(client: TestClient):
    """Test case for r_ead_whitelist_sdd_recurring_for_user

    
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
    #    "/user/{userID}/whitelist-sdd-recurring/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_whitelist_sdd_recurring_for_user(client: TestClient):
    """Test case for u_pdate_whitelist_sdd_recurring_for_user

    
    """
    whitelist_sdd_recurring = {"maximum_amount_per_payment":{"currency":"currency","value":"value"},"routing_type":"routing_type","maximum_amount_per_month":{"currency":"currency","value":"value"},"monetary_account_paying_id":0,"request_id":6}

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
    #    "/user/{userID}/whitelist-sdd-recurring/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=whitelist_sdd_recurring,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

