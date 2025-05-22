# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_review_check import UserReviewCheck  # noqa: F401
from openapi_server.models.user_review_check_create import UserReviewCheckCreate  # noqa: F401
from openapi_server.models.user_review_check_listing import UserReviewCheckListing  # noqa: F401
from openapi_server.models.user_review_check_read import UserReviewCheckRead  # noqa: F401
from openapi_server.models.user_review_check_update import UserReviewCheckUpdate  # noqa: F401


def test_c_reate_check_for_user_review(client: TestClient):
    """Test case for c_reate_check_for_user_review

    
    """
    user_review_check = {"review_id":6,"request_type":"request_type","action_type":"action_type","all_value":[{"created":"created","id":5,"updated":"updated","status":"status"},{"created":"created","id":5,"updated":"updated","status":"status"}],"created":"created","review_sub_type":"review_sub_type","description":"description","type":"type","announcement_text":"announcement_text","review_type":"review_type","sub_type":"sub_type","instruction":"instruction","review_status":"review_status","id":0,"fail_reason":"fail_reason","skip_reason":"skip_reason","updated":"updated","review_check_previous_id":1,"instruction_url":"instruction_url","status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check".format(userID=56, reviewID=56),
    #    headers=headers,
    #    json=user_review_check,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_check_for_user_review(client: TestClient):
    """Test case for list_all_check_for_user_review

    
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
    #    "/user/{userID}/review/{reviewID}/check".format(userID=56, reviewID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_check_for_user_review(client: TestClient):
    """Test case for r_ead_check_for_user_review

    
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
    #    "/user/{userID}/review/{reviewID}/check/{itemId}".format(userID=56, reviewID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_check_for_user_review(client: TestClient):
    """Test case for u_pdate_check_for_user_review

    
    """
    user_review_check = {"review_id":6,"request_type":"request_type","action_type":"action_type","all_value":[{"created":"created","id":5,"updated":"updated","status":"status"},{"created":"created","id":5,"updated":"updated","status":"status"}],"created":"created","review_sub_type":"review_sub_type","description":"description","type":"type","announcement_text":"announcement_text","review_type":"review_type","sub_type":"sub_type","instruction":"instruction","review_status":"review_status","id":0,"fail_reason":"fail_reason","skip_reason":"skip_reason","updated":"updated","review_check_previous_id":1,"instruction_url":"instruction_url","status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check/{itemId}".format(userID=56, reviewID=56, itemId=56),
    #    headers=headers,
    #    json=user_review_check,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

