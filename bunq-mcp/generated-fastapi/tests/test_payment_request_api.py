# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.translink_payment_request import TranslinkPaymentRequest  # noqa: F401
from openapi_server.models.translink_payment_request_create import TranslinkPaymentRequestCreate  # noqa: F401


def test_c_reate_payment_request(client: TestClient):
    """Test case for c_reate_payment_request

    
    """
    translink_payment_request = {"account_id":"accountId","action_type":"actionType","request_reference_id":"requestReferenceId","description":"description","related_transaction_id":"relatedTransactionId","payment_date_time":"paymentDateTime","monetary_amount":{"amount":0,"currency":"currency"}}

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
    #    "/payment-request",
    #    headers=headers,
    #    json=translink_payment_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

