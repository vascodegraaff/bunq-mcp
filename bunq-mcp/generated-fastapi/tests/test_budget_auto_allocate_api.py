# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.monetary_account_budget_auto_allocate import MonetaryAccountBudgetAutoAllocate  # noqa: F401
from openapi_server.models.monetary_account_budget_auto_allocate_create import MonetaryAccountBudgetAutoAllocateCreate  # noqa: F401
from openapi_server.models.monetary_account_budget_auto_allocate_listing import MonetaryAccountBudgetAutoAllocateListing  # noqa: F401
from openapi_server.models.monetary_account_budget_auto_allocate_read import MonetaryAccountBudgetAutoAllocateRead  # noqa: F401
from openapi_server.models.monetary_account_budget_auto_allocate_update import MonetaryAccountBudgetAutoAllocateUpdate  # noqa: F401


def test_c_reate_budget_auto_allocate_for_user_monetary_account(client: TestClient):
    """Test case for c_reate_budget_auto_allocate_for_user_monetary_account

    
    """
    monetary_account_budget_auto_allocate = {"all_category":["all_category","all_category"],"amount":{"currency":"currency","value":"value"},"payment_id":6,"monetary_account_remainder_id":0}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-auto-allocate".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #    json=monetary_account_budget_auto_allocate,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_budget_auto_allocate_for_user_monetary_account(client: TestClient):
    """Test case for d_elete_budget_auto_allocate_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-auto-allocate/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_budget_auto_allocate_for_user_monetary_account(client: TestClient):
    """Test case for list_all_budget_auto_allocate_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-auto-allocate".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_budget_auto_allocate_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_budget_auto_allocate_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-auto-allocate/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_budget_auto_allocate_for_user_monetary_account(client: TestClient):
    """Test case for u_pdate_budget_auto_allocate_for_user_monetary_account

    
    """
    monetary_account_budget_auto_allocate = {"all_category":["all_category","all_category"],"amount":{"currency":"currency","value":"value"},"payment_id":6,"monetary_account_remainder_id":0}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-auto-allocate/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #    json=monetary_account_budget_auto_allocate,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

