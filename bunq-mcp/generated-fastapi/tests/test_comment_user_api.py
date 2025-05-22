# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_comment_user import AdminCommentUser  # noqa: F401
from openapi_server.models.admin_comment_user_create import AdminCommentUserCreate  # noqa: F401
from openapi_server.models.admin_comment_user_listing import AdminCommentUserListing  # noqa: F401
from openapi_server.models.admin_comment_user_update import AdminCommentUserUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_comment_user_for_user(client: TestClient):
    """Test case for c_reate_comment_user_for_user

    
    """
    admin_comment_user = {"visibility":"visibility","attachment_id":5,"text":"text","status":"status"}

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
    #    "/user/{userID}/comment-user".format(userID=56),
    #    headers=headers,
    #    json=admin_comment_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_comment_user_for_user(client: TestClient):
    """Test case for list_all_comment_user_for_user

    
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
    #    "/user/{userID}/comment-user".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_comment_user_for_user(client: TestClient):
    """Test case for u_pdate_comment_user_for_user

    
    """
    admin_comment_user = {"visibility":"visibility","attachment_id":5,"text":"text","status":"status"}

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
    #    "/user/{userID}/comment-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=admin_comment_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

