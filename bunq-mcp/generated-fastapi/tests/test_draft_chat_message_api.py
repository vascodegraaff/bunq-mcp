# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.draft_chat_message_listing import DraftChatMessageListing  # noqa: F401
from openapi_server.models.draft_chat_message_user import DraftChatMessageUser  # noqa: F401
from openapi_server.models.draft_chat_message_user_create import DraftChatMessageUserCreate  # noqa: F401
from openapi_server.models.draft_chat_message_user_listing import DraftChatMessageUserListing  # noqa: F401
from openapi_server.models.draft_chat_message_user_read import DraftChatMessageUserRead  # noqa: F401
from openapi_server.models.draft_chat_message_user_update import DraftChatMessageUserUpdate  # noqa: F401


def test_c_reate_draft_chat_message_for_user_chat_conversation(client: TestClient):
    """Test case for c_reate_draft_chat_message_for_user_chat_conversation

    
    """
    draft_chat_message_user = {"feedback":"feedback","text":"text","status":"status"}

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
    #    "/user/{userID}/chat-conversation/{chat-conversationID}/draft-chat-message".format(userID=56, chat-conversationID=56),
    #    headers=headers,
    #    json=draft_chat_message_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_draft_chat_message(client: TestClient):
    """Test case for list_all_draft_chat_message

    
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
    #    "/draft-chat-message",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_draft_chat_message_for_user_chat_conversation(client: TestClient):
    """Test case for list_all_draft_chat_message_for_user_chat_conversation

    
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
    #    "/user/{userID}/chat-conversation/{chat-conversationID}/draft-chat-message".format(userID=56, chat-conversationID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_draft_chat_message_for_user_chat_conversation(client: TestClient):
    """Test case for r_ead_draft_chat_message_for_user_chat_conversation

    
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
    #    "/user/{userID}/chat-conversation/{chat-conversationID}/draft-chat-message/{itemId}".format(userID=56, chat-conversationID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_draft_chat_message_for_user_chat_conversation(client: TestClient):
    """Test case for u_pdate_draft_chat_message_for_user_chat_conversation

    
    """
    draft_chat_message_user = {"feedback":"feedback","text":"text","status":"status"}

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
    #    "/user/{userID}/chat-conversation/{chat-conversationID}/draft-chat-message/{itemId}".format(userID=56, chat-conversationID=56, itemId=56),
    #    headers=headers,
    #    json=draft_chat_message_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

