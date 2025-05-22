# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.support_access_request_monetary_account import SupportAccessRequestMonetaryAccount  # noqa: F401
from openapi_server.models.support_access_request_monetary_account_create import SupportAccessRequestMonetaryAccountCreate  # noqa: F401
from openapi_server.models.support_access_request_monetary_account_listing import SupportAccessRequestMonetaryAccountListing  # noqa: F401
from openapi_server.models.support_access_request_monetary_account_read import SupportAccessRequestMonetaryAccountRead  # noqa: F401


def test_c_reate_support_access_request_monetary_account_for_user_ticket(client: TestClient):
    """Test case for c_reate_support_access_request_monetary_account_for_user_ticket

    
    """
    support_access_request_monetary_account = {"duration_seconds":6,"access":"access","counterparty_alias":{"service":"service","name":"name","type":"type","value":"value"},"monetary_account_id":0}

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
    #    "/user/{userID}/ticket/{ticketID}/support-access-request-monetary-account".format(userID=56, ticketID=56),
    #    headers=headers,
    #    json=support_access_request_monetary_account,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_support_access_request_monetary_account_for_user_ticket(client: TestClient):
    """Test case for d_elete_support_access_request_monetary_account_for_user_ticket

    
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
    #    "/user/{userID}/ticket/{ticketID}/support-access-request-monetary-account/{itemId}".format(userID=56, ticketID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_support_access_request_monetary_account_for_user_ticket(client: TestClient):
    """Test case for list_all_support_access_request_monetary_account_for_user_ticket

    
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
    #    "/user/{userID}/ticket/{ticketID}/support-access-request-monetary-account".format(userID=56, ticketID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_support_access_request_monetary_account_for_user_ticket(client: TestClient):
    """Test case for r_ead_support_access_request_monetary_account_for_user_ticket

    
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
    #    "/user/{userID}/ticket/{ticketID}/support-access-request-monetary-account/{itemId}".format(userID=56, ticketID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

