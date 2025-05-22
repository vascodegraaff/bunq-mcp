# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ideal_issuer_profile import IdealIssuerProfile  # noqa: F401
from openapi_server.models.ideal_issuer_profile_create import IdealIssuerProfileCreate  # noqa: F401
from openapi_server.models.ideal_issuer_profile_listing import IdealIssuerProfileListing  # noqa: F401
from openapi_server.models.ideal_issuer_profile_read import IdealIssuerProfileRead  # noqa: F401
from openapi_server.models.ideal_issuer_profile_update import IdealIssuerProfileUpdate  # noqa: F401


def test_c_reate_ideal_issuer_profile_for_user(client: TestClient):
    """Test case for c_reate_ideal_issuer_profile_for_user

    
    """
    ideal_issuer_profile = {"all_monetary_account_id":[{"monetary_account_id":0},{"monetary_account_id":0}],"request_response_id":0}

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
    #    "/user/{userID}/ideal-issuer-profile".format(userID=56),
    #    headers=headers,
    #    json=ideal_issuer_profile,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_ideal_issuer_profile_for_user(client: TestClient):
    """Test case for list_all_ideal_issuer_profile_for_user

    
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
    #    "/user/{userID}/ideal-issuer-profile".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_ideal_issuer_profile_for_user(client: TestClient):
    """Test case for r_ead_ideal_issuer_profile_for_user

    
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
    #    "/user/{userID}/ideal-issuer-profile/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_ideal_issuer_profile_for_user(client: TestClient):
    """Test case for u_pdate_ideal_issuer_profile_for_user

    
    """
    ideal_issuer_profile = {"all_monetary_account_id":[{"monetary_account_id":0},{"monetary_account_id":0}],"request_response_id":0}

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
    #    "/user/{userID}/ideal-issuer-profile/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=ideal_issuer_profile,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

