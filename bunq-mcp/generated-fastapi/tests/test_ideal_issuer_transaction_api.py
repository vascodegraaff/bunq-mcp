# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ideal_issuer_transaction_app import IdealIssuerTransactionApp  # noqa: F401
from openapi_server.models.ideal_issuer_transaction_app_create import IdealIssuerTransactionAppCreate  # noqa: F401
from openapi_server.models.ideal_issuer_transaction_web import IdealIssuerTransactionWeb  # noqa: F401
from openapi_server.models.ideal_issuer_transaction_web_create import IdealIssuerTransactionWebCreate  # noqa: F401
from openapi_server.models.ideal_issuer_transaction_web_read import IdealIssuerTransactionWebRead  # noqa: F401
from openapi_server.models.ideal_issuer_transaction_web_update import IdealIssuerTransactionWebUpdate  # noqa: F401


def test_c_reate_ideal_issuer_transaction(client: TestClient):
    """Test case for c_reate_ideal_issuer_transaction

    
    """
    ideal_issuer_transaction_web = {"signature":"signature","payload_uri":"payload_uri","status":"status"}

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
    #    "/ideal-issuer-transaction",
    #    headers=headers,
    #    json=ideal_issuer_transaction_web,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_ideal_issuer_transaction_for_user(client: TestClient):
    """Test case for c_reate_ideal_issuer_transaction_for_user

    
    """
    ideal_issuer_transaction_app = {"signature":"signature","payload_uri":"payload_uri","source":"source"}

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
    #    "/user/{userID}/ideal-issuer-transaction".format(userID=56),
    #    headers=headers,
    #    json=ideal_issuer_transaction_app,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_ideal_issuer_transaction(client: TestClient):
    """Test case for r_ead_ideal_issuer_transaction

    
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
    #    "/ideal-issuer-transaction/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_ideal_issuer_transaction(client: TestClient):
    """Test case for u_pdate_ideal_issuer_transaction

    
    """
    ideal_issuer_transaction_web = {"signature":"signature","payload_uri":"payload_uri","status":"status"}

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
    #    "/ideal-issuer-transaction/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=ideal_issuer_transaction_web,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

