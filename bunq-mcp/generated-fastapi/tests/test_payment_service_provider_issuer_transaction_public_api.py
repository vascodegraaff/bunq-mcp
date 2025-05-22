# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.payment_service_provider_issuer_transaction_public import PaymentServiceProviderIssuerTransactionPublic  # noqa: F401
from openapi_server.models.payment_service_provider_issuer_transaction_public_read import PaymentServiceProviderIssuerTransactionPublicRead  # noqa: F401
from openapi_server.models.payment_service_provider_issuer_transaction_public_update import PaymentServiceProviderIssuerTransactionPublicUpdate  # noqa: F401


def test_r_ead_payment_service_provider_issuer_transaction_public(client: TestClient):
    """Test case for r_ead_payment_service_provider_issuer_transaction_public

    
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
    #    "/payment-service-provider-issuer-transaction-public/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_payment_service_provider_issuer_transaction_public(client: TestClient):
    """Test case for u_pdate_payment_service_provider_issuer_transaction_public

    
    """
    payment_service_provider_issuer_transaction_public = {"status":"status"}

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
    #    "/payment-service-provider-issuer-transaction-public/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=payment_service_provider_issuer_transaction_public,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

