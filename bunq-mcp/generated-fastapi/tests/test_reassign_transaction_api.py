# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.reassign_transaction import ReassignTransaction  # noqa: F401
from openapi_server.models.reassign_transaction_create import ReassignTransactionCreate  # noqa: F401


def test_c_reate_reassign_transaction_for_user_monetary_account_event(client: TestClient):
    """Test case for c_reate_reassign_transaction_for_user_monetary_account_event

    
    """
    reassign_transaction = {"monetary_account_target_id":0}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/event/{eventID}/reassign-transaction".format(userID=56, monetary-accountID=56, eventID=56),
    #    headers=headers,
    #    json=reassign_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

