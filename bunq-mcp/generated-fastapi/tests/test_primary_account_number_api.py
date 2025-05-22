# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_primary_account_number import CardPrimaryAccountNumber  # noqa: F401
from openapi_server.models.card_primary_account_number_create import CardPrimaryAccountNumberCreate  # noqa: F401


def test_c_reate_primary_account_number_for_user_card(client: TestClient):
    """Test case for c_reate_primary_account_number_for_user_card

    
    """
    card_primary_account_number = {"monetary_account_id":1,"description":"description","four_digit":"four_digit","id":6,"type":"type","uuid":"uuid","status":"status"}

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
    #    "/user/{userID}/card/{cardID}/primary-account-number".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=card_primary_account_number,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

