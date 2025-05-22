# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.point_challenge_promotion import PointChallengePromotion  # noqa: F401
from openapi_server.models.point_challenge_promotion_create import PointChallengePromotionCreate  # noqa: F401
from openapi_server.models.point_challenge_promotion_listing import PointChallengePromotionListing  # noqa: F401
from openapi_server.models.point_challenge_promotion_update import PointChallengePromotionUpdate  # noqa: F401


def test_c_reate_point_challenge_promotion_for_user(client: TestClient):
    """Test case for c_reate_point_challenge_promotion_for_user

    
    """
    point_challenge_promotion = {"notification_body":["notification_body","notification_body"],"description_short":["description_short","description_short"],"challenge_id":0,"time_start":"time_start","number_of_point_promotion":6,"description_long":["description_long","description_long"],"notification_title":["notification_title","notification_title"],"event_title":["event_title","event_title"],"time_end":"time_end","all_country_available":["all_country_available","all_country_available"]}

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
    #    "/user/{userID}/point-challenge-promotion".format(userID=56),
    #    headers=headers,
    #    json=point_challenge_promotion,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_point_challenge_promotion_for_user(client: TestClient):
    """Test case for list_all_point_challenge_promotion_for_user

    
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
    #    "/user/{userID}/point-challenge-promotion".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_point_challenge_promotion_for_user(client: TestClient):
    """Test case for u_pdate_point_challenge_promotion_for_user

    
    """
    point_challenge_promotion = {"notification_body":["notification_body","notification_body"],"description_short":["description_short","description_short"],"challenge_id":0,"time_start":"time_start","number_of_point_promotion":6,"description_long":["description_long","description_long"],"notification_title":["notification_title","notification_title"],"event_title":["event_title","event_title"],"time_end":"time_end","all_country_available":["all_country_available","all_country_available"]}

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
    #    "/user/{userID}/point-challenge-promotion/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=point_challenge_promotion,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

