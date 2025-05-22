# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.payment_service_provider_credential import PaymentServiceProviderCredential  # noqa: F401
from openapi_server.models.payment_service_provider_credential_create import PaymentServiceProviderCredentialCreate  # noqa: F401
from openapi_server.models.payment_service_provider_credential_read import PaymentServiceProviderCredentialRead  # noqa: F401


def test_c_reate_payment_service_provider_credential(client: TestClient):
    """Test case for c_reate_payment_service_provider_credential

    
    """
    payment_service_provider_credential = {"client_payment_service_provider_certificate_chain":"client_payment_service_provider_certificate_chain","client_payment_service_provider_certificate":"client_payment_service_provider_certificate","client_public_key_signature":"client_public_key_signature"}

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
    #    "/payment-service-provider-credential",
    #    headers=headers,
    #    json=payment_service_provider_credential,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_payment_service_provider_credential(client: TestClient):
    """Test case for r_ead_payment_service_provider_credential

    
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
    #    "/payment-service-provider-credential/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

