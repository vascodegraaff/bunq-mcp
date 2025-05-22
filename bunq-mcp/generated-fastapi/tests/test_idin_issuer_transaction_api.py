# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.idin_issuer_transaction import IdinIssuerTransaction  # noqa: F401
from openapi_server.models.idin_issuer_transaction_listing import IdinIssuerTransactionListing  # noqa: F401
from openapi_server.models.idin_issuer_transaction_update import IdinIssuerTransactionUpdate  # noqa: F401


def test_list_all_idin_issuer_transaction(client: TestClient):
    """Test case for list_all_idin_issuer_transaction

    
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
    #    "/idin-issuer-transaction",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_idin_issuer_transaction(client: TestClient):
    """Test case for u_pdate_idin_issuer_transaction

    
    """
    idin_issuer_transaction = {"status":"status"}

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
    #    "/idin-issuer-transaction/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=idin_issuer_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

