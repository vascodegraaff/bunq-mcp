# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_token_connect_provision import MasterCardTokenConnectProvision  # noqa: F401
from openapi_server.models.master_card_token_connect_provision_create import MasterCardTokenConnectProvisionCreate  # noqa: F401
from openapi_server.models.master_card_token_connect_provision_read import MasterCardTokenConnectProvisionRead  # noqa: F401


def test_c_reate_mastercard_token_connect_provision_for_user_card(client: TestClient):
    """Test case for c_reate_mastercard_token_connect_provision_for_user_card

    
    """
    master_card_token_connect_provision = {"token_requestor":"token_requestor"}

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
    #    "/user/{userID}/card/{cardID}/mastercard-token-connect-provision".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=master_card_token_connect_provision,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_mastercard_token_connect_provision_for_user_card(client: TestClient):
    """Test case for r_ead_mastercard_token_connect_provision_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/mastercard-token-connect-provision/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

