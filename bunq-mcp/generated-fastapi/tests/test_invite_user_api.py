# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.invite_user import InviteUser  # noqa: F401
from openapi_server.models.invite_user_create import InviteUserCreate  # noqa: F401
from openapi_server.models.invite_user_listing import InviteUserListing  # noqa: F401
from openapi_server.models.invite_user_read import InviteUserRead  # noqa: F401
from openapi_server.models.invite_user_update import InviteUserUpdate  # noqa: F401


def test_c_reate_invite_user_for_user(client: TestClient):
    """Test case for c_reate_invite_user_for_user

    
    """
    invite_user = {"sender_label":"sender_label","receiver_label":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"invite_sent_count":6,"receiver_pointer":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","status":"status"}

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
    #    "/user/{userID}/invite-user".format(userID=56),
    #    headers=headers,
    #    json=invite_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_invite_user_for_user(client: TestClient):
    """Test case for list_all_invite_user_for_user

    
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
    #    "/user/{userID}/invite-user".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_invite_user_for_user(client: TestClient):
    """Test case for r_ead_invite_user_for_user

    
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
    #    "/user/{userID}/invite-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_invite_user_for_user(client: TestClient):
    """Test case for u_pdate_invite_user_for_user

    
    """
    invite_user = {"sender_label":"sender_label","receiver_label":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"invite_sent_count":6,"receiver_pointer":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","status":"status"}

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
    #    "/user/{userID}/invite-user/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=invite_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

