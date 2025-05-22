# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.assistant_function_callback_escalation import AssistantFunctionCallbackEscalation  # noqa: F401
from openapi_server.models.assistant_function_callback_escalation_conversation import AssistantFunctionCallbackEscalationConversation  # noqa: F401
from openapi_server.models.assistant_function_callback_escalation_conversation_create import AssistantFunctionCallbackEscalationConversationCreate  # noqa: F401
from openapi_server.models.assistant_function_callback_escalation_listing import AssistantFunctionCallbackEscalationListing  # noqa: F401
from openapi_server.models.assistant_function_callback_escalation_read import AssistantFunctionCallbackEscalationRead  # noqa: F401
from openapi_server.models.assistant_function_callback_escalation_update import AssistantFunctionCallbackEscalationUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_assistant_function_callback_escalation_for_user_assistant_conversation(client: TestClient):
    """Test case for c_reate_assistant_function_callback_escalation_for_user_assistant_conversation

    
    """
    assistant_function_callback_escalation_conversation = {"expertise":"expertise","priority":"priority"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/assistant-function-callback-escalation".format(userID=56, assistantID=56, conversationID=56),
    #    headers=headers,
    #    json=assistant_function_callback_escalation_conversation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_assistant_function_callback_escalation_for_user(client: TestClient):
    """Test case for list_all_assistant_function_callback_escalation_for_user

    
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
    #    "/user/{userID}/assistant-function-callback-escalation".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_assistant_function_callback_escalation_for_user(client: TestClient):
    """Test case for r_ead_assistant_function_callback_escalation_for_user

    
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
    #    "/user/{userID}/assistant-function-callback-escalation/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_assistant_function_callback_escalation_for_user(client: TestClient):
    """Test case for u_pdate_assistant_function_callback_escalation_for_user

    
    """
    assistant_function_callback_escalation = {"expertise":"expertise","status":"status"}

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
    #    "/user/{userID}/assistant-function-callback-escalation/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=assistant_function_callback_escalation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

