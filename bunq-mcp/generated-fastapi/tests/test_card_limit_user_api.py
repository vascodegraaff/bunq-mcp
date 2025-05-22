# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_limit_user import CardLimitUser  # noqa: F401
from openapi_server.models.card_limit_user_create import CardLimitUserCreate  # noqa: F401
from openapi_server.models.card_limit_user_listing import CardLimitUserListing  # noqa: F401
from openapi_server.models.card_limit_user_update import CardLimitUserUpdate  # noqa: F401


def test_c_reate_card_limit_user_for_user(client: TestClient):
    """Test case for c_reate_card_limit_user_for_user

    
    """
    card_limit_user = {"card_limit":{"currency":"currency","value":"value"}}

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
    #    "/user/{userID}/card-limit-user".format(userID=56),
    #    headers=headers,
    #    json=card_limit_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_card_limit_user_for_user(client: TestClient):
    """Test case for list_all_card_limit_user_for_user

    
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
    #    "/user/{userID}/card-limit-user".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_card_limit_user_for_user(client: TestClient):
    """Test case for u_pdate_card_limit_user_for_user

    
    """
    card_limit_user = {"card_limit":{"currency":"currency","value":"value"}}

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
    #    "/user/{userID}/card-limit-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=card_limit_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

