# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ideal_issuer_provider_transaction_notify import IdealIssuerProviderTransactionNotify  # noqa: F401
from openapi_server.models.ideal_issuer_provider_transaction_notify_create import IdealIssuerProviderTransactionNotifyCreate  # noqa: F401


def test_c_reate_transactions_notify(client: TestClient):
    """Test case for c_reate_transactions_notify

    
    """
    ideal_issuer_provider_transaction_notify = {"payload_uri":"payloadUri","amount":{"amount":0,"maximum":6,"currency":"currency","type":"type","minimum":1},"debtor":{"user_agent":"userAgent"},"expiry_date_timestamp":"expiryDateTimestamp","description":"description","creditor":{"payment_beneficiary_name":"paymentBeneficiaryName"}}

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
    #    "/transactions/notify",
    #    headers=headers,
    #    json=ideal_issuer_provider_transaction_notify,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

