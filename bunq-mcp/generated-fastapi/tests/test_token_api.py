# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_wallet_token import MasterCardWalletToken  # noqa: F401
from openapi_server.models.master_card_wallet_token_create import MasterCardWalletTokenCreate  # noqa: F401
from openapi_server.models.master_card_wallet_token_listing import MasterCardWalletTokenListing  # noqa: F401
from openapi_server.models.master_card_wallet_token_read import MasterCardWalletTokenRead  # noqa: F401
from openapi_server.models.master_card_wallet_token_update import MasterCardWalletTokenUpdate  # noqa: F401
from openapi_server.models.oauth_token_create import OauthTokenCreate  # noqa: F401
from openapi_server.models.token_listing import TokenListing  # noqa: F401


def test_c_reate_token(client: TestClient):
    """Test case for c_reate_token

    
    """
    body = None

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
    #    "/token",
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_token_for_user_wallet(client: TestClient):
    """Test case for c_reate_token_for_user_wallet

    
    """
    master_card_wallet_token = {"terms_and_conditions_accepted_timestamp":"terms_and_conditions_accepted_timestamp","activation_code":"activation_code","token_authentication_value":"token_authentication_value","status":"status"}

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
    #    "/user/{userID}/wallet/{walletID}/token".format(userID=56, walletID=56),
    #    headers=headers,
    #    json=master_card_wallet_token,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_token_for_user_card(client: TestClient):
    """Test case for list_all_token_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/token".format(userID=56, cardID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_token_for_user_wallet(client: TestClient):
    """Test case for list_all_token_for_user_wallet

    
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
    #    "/user/{userID}/wallet/{walletID}/token".format(userID=56, walletID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_token_for_user_wallet(client: TestClient):
    """Test case for r_ead_token_for_user_wallet

    
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
    #    "/user/{userID}/wallet/{walletID}/token/{itemId}".format(userID=56, walletID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_token_for_user_wallet(client: TestClient):
    """Test case for u_pdate_token_for_user_wallet

    
    """
    master_card_wallet_token = {"terms_and_conditions_accepted_timestamp":"terms_and_conditions_accepted_timestamp","activation_code":"activation_code","token_authentication_value":"token_authentication_value","status":"status"}

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
    #    "PUT",
    #    "/user/{userID}/wallet/{walletID}/token/{itemId}".format(userID=56, walletID=56, itemId=56),
    #    headers=headers,
    #    json=master_card_wallet_token,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

