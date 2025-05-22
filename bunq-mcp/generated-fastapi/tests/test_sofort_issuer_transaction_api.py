# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.sofort_issuer_transaction import SofortIssuerTransaction  # noqa: F401
from openapi_server.models.sofort_issuer_transaction_create import SofortIssuerTransactionCreate  # noqa: F401
from openapi_server.models.sofort_issuer_transaction_read import SofortIssuerTransactionRead  # noqa: F401
from openapi_server.models.sofort_issuer_transaction_update import SofortIssuerTransactionUpdate  # noqa: F401


def test_c_reate_sofort_issuer_transaction(client: TestClient):
    """Test case for c_reate_sofort_issuer_transaction

    
    """
    sofort_issuer_transaction = {"counterparty_name":"counterparty_name","counterparty_iban":"counterparty_iban","amount_requested":{"currency":"currency","value":"value"},"expiration_time":"expiration_time","description":"description","return_url":"return_url","language":"language","status":"status"}

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
    #    "/sofort-issuer-transaction",
    #    headers=headers,
    #    json=sofort_issuer_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_sofort_issuer_transaction(client: TestClient):
    """Test case for r_ead_sofort_issuer_transaction

    
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
    #    "/sofort-issuer-transaction/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_sofort_issuer_transaction(client: TestClient):
    """Test case for u_pdate_sofort_issuer_transaction

    
    """
    sofort_issuer_transaction = {"counterparty_name":"counterparty_name","counterparty_iban":"counterparty_iban","amount_requested":{"currency":"currency","value":"value"},"expiration_time":"expiration_time","description":"description","return_url":"return_url","language":"language","status":"status"}

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
    #    "/sofort-issuer-transaction/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=sofort_issuer_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

