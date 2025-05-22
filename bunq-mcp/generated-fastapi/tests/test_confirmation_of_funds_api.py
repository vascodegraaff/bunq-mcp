# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.confirmation_of_funds import ConfirmationOfFunds  # noqa: F401
from openapi_server.models.confirmation_of_funds_create import ConfirmationOfFundsCreate  # noqa: F401


def test_c_reate_confirmation_of_funds_for_user(client: TestClient):
    """Test case for c_reate_confirmation_of_funds_for_user

    
    """
    confirmation_of_funds = {"amount":{"currency":"currency","value":"value"},"pointer_iban":{"service":"service","name":"name","type":"type","value":"value"}}

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
    #    "/user/{userID}/confirmation-of-funds".format(userID=56),
    #    headers=headers,
    #    json=confirmation_of_funds,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

