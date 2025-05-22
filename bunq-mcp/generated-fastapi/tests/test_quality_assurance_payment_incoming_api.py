# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.quality_assurance_payment_incoming import QualityAssurancePaymentIncoming  # noqa: F401
from openapi_server.models.quality_assurance_payment_incoming_create import QualityAssurancePaymentIncomingCreate  # noqa: F401


def test_c_reate_quality_assurance_payment_incoming(client: TestClient):
    """Test case for c_reate_quality_assurance_payment_incoming

    
    """
    quality_assurance_payment_incoming = {"pointer_sender":{"service":"service","name":"name","type":"type","value":"value"},"amount":{"currency":"currency","value":"value"},"pointer_receiver":{"service":"service","name":"name","type":"type","value":"value"},"description":"description"}

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
    #    "/quality-assurance-payment-incoming",
    #    headers=headers,
    #    json=quality_assurance_payment_incoming,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

