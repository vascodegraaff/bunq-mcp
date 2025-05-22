# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.oauth_token_bunq import OauthTokenBunq  # noqa: F401
from openapi_server.models.oauth_token_bunq_create import OauthTokenBunqCreate  # noqa: F401


def test_c_reate_token_bunq(client: TestClient):
    """Test case for c_reate_token_bunq

    
    """
    oauth_token_bunq = {"code":"code","grant_type":"grant_type","redirect_uri":"redirect_uri","client_id":"client_id"}

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
    #    "/token-bunq",
    #    headers=headers,
    #    json=oauth_token_bunq,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

