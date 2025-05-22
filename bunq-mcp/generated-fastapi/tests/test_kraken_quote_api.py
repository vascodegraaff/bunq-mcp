# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.kraken_quote import KrakenQuote  # noqa: F401
from openapi_server.models.kraken_quote_create import KrakenQuoteCreate  # noqa: F401
from openapi_server.models.kraken_quote_read import KrakenQuoteRead  # noqa: F401
from openapi_server.models.kraken_quote_update import KrakenQuoteUpdate  # noqa: F401


def test_c_reate_kraken_quote_for_user_kraken_account(client: TestClient):
    """Test case for c_reate_kraken_quote_for_user_kraken_account

    
    """
    kraken_quote = {"unit_target":{"unit":"unit","type":"type"},"amount":{"unit":"unit","type":"type","value":"value"},"unit_source":{"unit":"unit","type":"type"},"side_fixed":"side_fixed","alias":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"}

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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-quote".format(userID=56, kraken-accountID=56),
    #    headers=headers,
    #    json=kraken_quote,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_kraken_quote_for_user_kraken_account(client: TestClient):
    """Test case for r_ead_kraken_quote_for_user_kraken_account

    
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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-quote/{itemId}".format(userID=56, kraken-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_kraken_quote_for_user_kraken_account(client: TestClient):
    """Test case for u_pdate_kraken_quote_for_user_kraken_account

    
    """
    kraken_quote = {"unit_target":{"unit":"unit","type":"type"},"amount":{"unit":"unit","type":"type","value":"value"},"unit_source":{"unit":"unit","type":"type"},"side_fixed":"side_fixed","alias":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"}

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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-quote/{itemId}".format(userID=56, kraken-accountID=56, itemId=56),
    #    headers=headers,
    #    json=kraken_quote,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

