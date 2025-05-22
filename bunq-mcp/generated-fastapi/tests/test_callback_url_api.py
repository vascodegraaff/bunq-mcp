# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.oauth_callback_url import OauthCallbackUrl  # noqa: F401
from openapi_server.models.oauth_callback_url_create import OauthCallbackUrlCreate  # noqa: F401
from openapi_server.models.oauth_callback_url_listing import OauthCallbackUrlListing  # noqa: F401
from openapi_server.models.oauth_callback_url_read import OauthCallbackUrlRead  # noqa: F401
from openapi_server.models.oauth_callback_url_update import OauthCallbackUrlUpdate  # noqa: F401


def test_c_reate_callback_url_for_user_oauth_client(client: TestClient):
    """Test case for c_reate_callback_url_for_user_oauth_client

    
    """
    oauth_callback_url = {"url":"url"}

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
    #    "/user/{userID}/oauth-client/{oauth-clientID}/callback-url".format(userID=56, oauth-clientID=56),
    #    headers=headers,
    #    json=oauth_callback_url,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_callback_url_for_user_oauth_client(client: TestClient):
    """Test case for d_elete_callback_url_for_user_oauth_client

    
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
    #    "DELETE",
    #    "/user/{userID}/oauth-client/{oauth-clientID}/callback-url/{itemId}".format(userID=56, oauth-clientID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_callback_url_for_user_oauth_client(client: TestClient):
    """Test case for list_all_callback_url_for_user_oauth_client

    
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
    #    "/user/{userID}/oauth-client/{oauth-clientID}/callback-url".format(userID=56, oauth-clientID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_callback_url_for_user_oauth_client(client: TestClient):
    """Test case for r_ead_callback_url_for_user_oauth_client

    
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
    #    "/user/{userID}/oauth-client/{oauth-clientID}/callback-url/{itemId}".format(userID=56, oauth-clientID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_callback_url_for_user_oauth_client(client: TestClient):
    """Test case for u_pdate_callback_url_for_user_oauth_client

    
    """
    oauth_callback_url = {"url":"url"}

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
    #    "/user/{userID}/oauth-client/{oauth-clientID}/callback-url/{itemId}".format(userID=56, oauth-clientID=56, itemId=56),
    #    headers=headers,
    #    json=oauth_callback_url,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

