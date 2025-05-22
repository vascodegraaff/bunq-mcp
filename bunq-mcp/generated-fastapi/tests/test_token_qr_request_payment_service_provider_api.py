# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.token_qr_request_payment_service_provider import TokenQrRequestPaymentServiceProvider  # noqa: F401
from openapi_server.models.token_qr_request_payment_service_provider_create import TokenQrRequestPaymentServiceProviderCreate  # noqa: F401


def test_c_reate_token_qr_request_payment_service_provider_for_user(client: TestClient):
    """Test case for c_reate_token_qr_request_payment_service_provider_for_user

    
    """
    token_qr_request_payment_service_provider = {"token":"token"}

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
    #    "/user/{userID}/token-qr-request-payment-service-provider".format(userID=56),
    #    headers=headers,
    #    json=token_qr_request_payment_service_provider,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

