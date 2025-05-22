# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.oauth_request import OauthRequest  # noqa: F401
from openapi_server.models.oauth_request_create import OauthRequestCreate  # noqa: F401
from openapi_server.models.oauth_request_read import OauthRequestRead  # noqa: F401
from openapi_server.models.oauth_request_update import OauthRequestUpdate  # noqa: F401
from openapi_server.models.oauth_request_user import OauthRequestUser  # noqa: F401
from openapi_server.models.oauth_request_user_listing import OauthRequestUserListing  # noqa: F401
from openapi_server.models.oauth_request_user_read import OauthRequestUserRead  # noqa: F401
from openapi_server.models.oauth_request_user_update import OauthRequestUserUpdate  # noqa: F401


def test_c_reate_oauth_request(client: TestClient):
    """Test case for c_reate_oauth_request

    
    """
    oauth_request = {"callback_url":"callback_url","response_type":"response_type","state":"state","client_id":"client_id","status":"status"}

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
    #    "/oauth-request",
    #    headers=headers,
    #    json=oauth_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_oauth_request_for_user(client: TestClient):
    """Test case for list_all_oauth_request_for_user

    
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
    #    "/user/{userID}/oauth-request".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_oauth_request(client: TestClient):
    """Test case for r_ead_oauth_request

    
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
    #    "/oauth-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_oauth_request_for_user(client: TestClient):
    """Test case for r_ead_oauth_request_for_user

    
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
    #    "/user/{userID}/oauth-request/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_oauth_request(client: TestClient):
    """Test case for u_pdate_oauth_request

    
    """
    oauth_request = {"callback_url":"callback_url","response_type":"response_type","state":"state","client_id":"client_id","status":"status"}

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
    #    "/oauth-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=oauth_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_oauth_request_for_user(client: TestClient):
    """Test case for u_pdate_oauth_request_for_user

    
    """
    oauth_request_user = {"payment_service_provider_draft_payments":[{"payment_service_provider_draft_payment_id":6},{"payment_service_provider_draft_payment_id":6}],"monetary_accounts":[{"monetary_account_id":0},{"monetary_account_id":0}],"status":"status"}

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
    #    "/user/{userID}/oauth-request/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=oauth_request_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

