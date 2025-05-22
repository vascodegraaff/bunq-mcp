# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.token_qr_bunq_me_reassign_request import TokenQrBunqMeReassignRequest  # noqa: F401
from openapi_server.models.token_qr_bunq_me_reassign_request_create import TokenQrBunqMeReassignRequestCreate  # noqa: F401


def test_c_reate_token_qr_bunqme_reassign_request_for_user(client: TestClient):
    """Test case for c_reate_token_qr_bunqme_reassign_request_for_user

    
    """
    token_qr_bunq_me_reassign_request = {"token":"token"}

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
    #    "/user/{userID}/token-qr-bunqme-reassign-request".format(userID=56),
    #    headers=headers,
    #    json=token_qr_bunq_me_reassign_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

