# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request import MasterCardIdentityCheckChallengeRequest  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_read import MasterCardIdentityCheckChallengeRequestRead  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_update import MasterCardIdentityCheckChallengeRequestUpdate  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_user import MasterCardIdentityCheckChallengeRequestUser  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_user_listing import MasterCardIdentityCheckChallengeRequestUserListing  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_user_read import MasterCardIdentityCheckChallengeRequestUserRead  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_user_update import MasterCardIdentityCheckChallengeRequestUserUpdate  # noqa: F401


def test_list_all_challenge_request_for_user(client: TestClient):
    """Test case for list_all_challenge_request_for_user

    
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
    #    "/user/{userID}/challenge-request".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_challenge_request(client: TestClient):
    """Test case for r_ead_challenge_request

    
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
    #    "/challenge-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_challenge_request_for_user(client: TestClient):
    """Test case for r_ead_challenge_request_for_user

    
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
    #    "/user/{userID}/challenge-request/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_challenge_request(client: TestClient):
    """Test case for u_pdate_challenge_request

    
    """
    master_card_identity_check_challenge_request = {"status":"status"}

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
    #    "/challenge-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=master_card_identity_check_challenge_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_challenge_request_for_user(client: TestClient):
    """Test case for u_pdate_challenge_request_for_user

    
    """
    master_card_identity_check_challenge_request_user = {"status":"status"}

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
    #    "/user/{userID}/challenge-request/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=master_card_identity_check_challenge_request_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

