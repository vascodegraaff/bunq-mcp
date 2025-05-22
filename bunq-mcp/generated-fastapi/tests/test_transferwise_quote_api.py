# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transferwise_quote import TransferwiseQuote  # noqa: F401
from openapi_server.models.transferwise_quote_create import TransferwiseQuoteCreate  # noqa: F401
from openapi_server.models.transferwise_quote_read import TransferwiseQuoteRead  # noqa: F401


def test_c_reate_transferwise_quote_for_user(client: TestClient):
    """Test case for c_reate_transferwise_quote_for_user

    
    """
    transferwise_quote = {"amount_source":{"currency":"currency","value":"value"},"currency_source":"currency_source","rate":"rate","created":"created","time_expiry":"time_expiry","time_delivery_estimate":"time_delivery_estimate","currency_target":"currency_target","quote_id":"quote_id","amount_fee":{"currency":"currency","value":"value"},"amount_target":{"currency":"currency","value":"value"},"id":5,"updated":"updated"}

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
    #    "/user/{userID}/transferwise-quote".format(userID=56),
    #    headers=headers,
    #    json=transferwise_quote,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transferwise_quote_for_user(client: TestClient):
    """Test case for r_ead_transferwise_quote_for_user

    
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
    #    "/user/{userID}/transferwise-quote/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

