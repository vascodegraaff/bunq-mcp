# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.open_banking_authentication_request import OpenBankingAuthenticationRequest  # noqa: F401
from openapi_server.models.open_banking_authentication_request_create import OpenBankingAuthenticationRequestCreate  # noqa: F401
from openapi_server.models.open_banking_authentication_request_read import OpenBankingAuthenticationRequestRead  # noqa: F401


def test_c_reate_open_banking_authentication_request_for_user(client: TestClient):
    """Test case for c_reate_open_banking_authentication_request_for_user

    
    """
    open_banking_authentication_request = {"provider_bank_id":0,"sync_type":"sync_type","url_issuer_authentication":"url_issuer_authentication","status":"status"}

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
    #    "/user/{userID}/open-banking-authentication-request".format(userID=56),
    #    headers=headers,
    #    json=open_banking_authentication_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_open_banking_authentication_request_for_user(client: TestClient):
    """Test case for r_ead_open_banking_authentication_request_for_user

    
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
    #    "/user/{userID}/open-banking-authentication-request/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

