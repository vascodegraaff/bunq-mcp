# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.assistant_conversation import AssistantConversation  # noqa: F401
from openapi_server.models.assistant_conversation_create import AssistantConversationCreate  # noqa: F401
from openapi_server.models.assistant_conversation_listing import AssistantConversationListing  # noqa: F401
from openapi_server.models.assistant_conversation_read import AssistantConversationRead  # noqa: F401
from openapi_server.models.assistant_conversation_update import AssistantConversationUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_conversation_for_user_assistant(client: TestClient):
    """Test case for c_reate_conversation_for_user_assistant

    
    """
    assistant_conversation = {"message_read_last_id":0,"context":[{"event_id":6,"app_location":"app_location","monetary_account_id":1,"monetary_account_type":"monetary_account_type","type":"type"},{"event_id":6,"app_location":"app_location","monetary_account_id":1,"monetary_account_type":"monetary_account_type","type":"type"}],"type":"type"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation".format(userID=56, assistantID=56),
    #    headers=headers,
    #    json=assistant_conversation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_conversation_for_user_assistant(client: TestClient):
    """Test case for list_all_conversation_for_user_assistant

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation".format(userID=56, assistantID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_conversation_for_user_assistant(client: TestClient):
    """Test case for r_ead_conversation_for_user_assistant

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{itemId}".format(userID=56, assistantID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_conversation_for_user_assistant(client: TestClient):
    """Test case for u_pdate_conversation_for_user_assistant

    
    """
    assistant_conversation = {"message_read_last_id":0,"context":[{"event_id":6,"app_location":"app_location","monetary_account_id":1,"monetary_account_type":"monetary_account_type","type":"type"},{"event_id":6,"app_location":"app_location","monetary_account_id":1,"monetary_account_type":"monetary_account_type","type":"type"}],"type":"type"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{itemId}".format(userID=56, assistantID=56, itemId=56),
    #    headers=headers,
    #    json=assistant_conversation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

