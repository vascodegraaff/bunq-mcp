# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_user_review_value import AdminUserReviewValue  # noqa: F401
from openapi_server.models.admin_user_review_value_listing import AdminUserReviewValueListing  # noqa: F401
from openapi_server.models.admin_user_review_value_update import AdminUserReviewValueUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_list_all_admin_value_for_user_review_check(client: TestClient):
    """Test case for list_all_admin_value_for_user_review_check

    
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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/admin-value".format(userID=56, reviewID=56, checkID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_value_for_user_review_check(client: TestClient):
    """Test case for u_pdate_admin_value_for_user_review_check

    
    """
    admin_user_review_value = {"deny_reason":"deny_reason","status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/admin-value/{itemId}".format(userID=56, reviewID=56, checkID=56, itemId=56),
    #    headers=headers,
    #    json=admin_user_review_value,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

