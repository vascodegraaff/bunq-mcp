# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.monetary_account_budget_schedule import MonetaryAccountBudgetSchedule  # noqa: F401
from openapi_server.models.monetary_account_budget_schedule_create import MonetaryAccountBudgetScheduleCreate  # noqa: F401
from openapi_server.models.monetary_account_budget_schedule_listing import MonetaryAccountBudgetScheduleListing  # noqa: F401
from openapi_server.models.monetary_account_budget_schedule_read import MonetaryAccountBudgetScheduleRead  # noqa: F401
from openapi_server.models.monetary_account_budget_schedule_update import MonetaryAccountBudgetScheduleUpdate  # noqa: F401


def test_c_reate_budget_schedule_for_user_monetary_account(client: TestClient):
    """Test case for c_reate_budget_schedule_for_user_monetary_account

    
    """
    monetary_account_budget_schedule = {"monetary_account_source_funding_id":6,"all_category":["all_category","all_category"],"amount":{"currency":"currency","value":"value"},"payment_day_of_month":1,"recurrence_type":"recurrence_type","monetary_account_remainder_id":0}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-schedule".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #    json=monetary_account_budget_schedule,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_budget_schedule_for_user_monetary_account(client: TestClient):
    """Test case for d_elete_budget_schedule_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-schedule/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_budget_schedule_for_user_monetary_account(client: TestClient):
    """Test case for list_all_budget_schedule_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-schedule".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_budget_schedule_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_budget_schedule_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-schedule/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_budget_schedule_for_user_monetary_account(client: TestClient):
    """Test case for u_pdate_budget_schedule_for_user_monetary_account

    
    """
    monetary_account_budget_schedule = {"monetary_account_source_funding_id":6,"all_category":["all_category","all_category"],"amount":{"currency":"currency","value":"value"},"payment_day_of_month":1,"recurrence_type":"recurrence_type","monetary_account_remainder_id":0}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/budget-schedule/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #    json=monetary_account_budget_schedule,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

