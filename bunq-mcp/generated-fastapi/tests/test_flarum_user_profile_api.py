# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.flarum_user_profile import FlarumUserProfile  # noqa: F401
from openapi_server.models.flarum_user_profile_listing import FlarumUserProfileListing  # noqa: F401
from openapi_server.models.flarum_user_profile_update import FlarumUserProfileUpdate  # noqa: F401


def test_list_all_flarum_user_profile_for_user(client: TestClient):
    """Test case for list_all_flarum_user_profile_for_user

    
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
    #    "/user/{userID}/flarum-user-profile".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_flarum_user_profile_for_user(client: TestClient):
    """Test case for u_pdate_flarum_user_profile_for_user

    
    """
    flarum_user_profile = {"status":"status"}

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
    #    "/user/{userID}/flarum-user-profile/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=flarum_user_profile,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

