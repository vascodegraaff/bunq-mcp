# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.paysafecash_transaction_confirmation import PaysafecashTransactionConfirmation  # noqa: F401
from openapi_server.models.paysafecash_transaction_confirmation_create import PaysafecashTransactionConfirmationCreate  # noqa: F401


def test_c_reate_paysafecash_transaction_webhook(client: TestClient):
    """Test case for c_reate_paysafecash_transaction_webhook

    
    """
    paysafecash_transaction_confirmation = {"data":{"mtid":"mtid","mid":"mid"},"event_type":"eventType","version":"version","timestamp":0}

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
    #    "/paysafecash-transaction-webhook",
    #    headers=headers,
    #    json=paysafecash_transaction_confirmation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

