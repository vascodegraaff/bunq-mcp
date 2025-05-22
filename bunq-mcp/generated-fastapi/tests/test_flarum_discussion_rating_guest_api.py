# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.flarum_discussion_rating_public_guest import FlarumDiscussionRatingPublicGuest  # noqa: F401
from openapi_server.models.flarum_discussion_rating_public_guest_create import FlarumDiscussionRatingPublicGuestCreate  # noqa: F401
from openapi_server.models.flarum_discussion_rating_public_guest_listing import FlarumDiscussionRatingPublicGuestListing  # noqa: F401
from openapi_server.models.flarum_discussion_rating_public_guest_update import FlarumDiscussionRatingPublicGuestUpdate  # noqa: F401


def test_c_reate_flarum_discussion_rating_guest(client: TestClient):
    """Test case for c_reate_flarum_discussion_rating_guest

    
    """
    flarum_discussion_rating_public_guest = {"flarum_discussion_id":0,"reason":"reason","pointer":{"service":"service","name":"name","type":"type","value":"value"},"rating":"rating","comment":"comment"}

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
    #    "/flarum-discussion-rating-guest",
    #    headers=headers,
    #    json=flarum_discussion_rating_public_guest,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_flarum_discussion_rating_guest(client: TestClient):
    """Test case for list_all_flarum_discussion_rating_guest

    
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
    #    "/flarum-discussion-rating-guest",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_flarum_discussion_rating_guest(client: TestClient):
    """Test case for u_pdate_flarum_discussion_rating_guest

    
    """
    flarum_discussion_rating_public_guest = {"flarum_discussion_id":0,"reason":"reason","pointer":{"service":"service","name":"name","type":"type","value":"value"},"rating":"rating","comment":"comment"}

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
    #    "/flarum-discussion-rating-guest/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=flarum_discussion_rating_public_guest,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

