# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.monetary_account_card import MonetaryAccountCard  # noqa: F401
from openapi_server.models.monetary_account_card_listing import MonetaryAccountCardListing  # noqa: F401
from openapi_server.models.monetary_account_card_read import MonetaryAccountCardRead  # noqa: F401
from openapi_server.models.monetary_account_card_update import MonetaryAccountCardUpdate  # noqa: F401


def test_list_all_monetary_account_card_for_user(client: TestClient):
    """Test case for list_all_monetary_account_card_for_user

    
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
    #    "/user/{userID}/monetary-account-card".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_monetary_account_card_for_user(client: TestClient):
    """Test case for r_ead_monetary_account_card_for_user

    
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
    #    "/user/{userID}/monetary-account-card/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_monetary_account_card_for_user(client: TestClient):
    """Test case for u_pdate_monetary_account_card_for_user

    
    """
    monetary_account_card = {"overdraft_limit":{"currency":"currency","value":"value"},"sub_status":"sub_status","created":"created","balance_real":{"currency":"currency","value":"value"},"description":"description","public_uuid":"public_uuid","balance":{"currency":"currency","value":"value"},"user_id":0,"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"currency":"currency","id":3,"updated":"updated","daily_limit":{"currency":"currency","value":"value"},"status":"status"}

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
    #    "/user/{userID}/monetary-account-card/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=monetary_account_card,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

