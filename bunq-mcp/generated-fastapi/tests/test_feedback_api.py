# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.assistant_feedback_conversation import AssistantFeedbackConversation  # noqa: F401
from openapi_server.models.assistant_feedback_conversation_create import AssistantFeedbackConversationCreate  # noqa: F401
from openapi_server.models.assistant_feedback_conversation_listing import AssistantFeedbackConversationListing  # noqa: F401
from openapi_server.models.assistant_feedback_message import AssistantFeedbackMessage  # noqa: F401
from openapi_server.models.assistant_feedback_message_create import AssistantFeedbackMessageCreate  # noqa: F401
from openapi_server.models.assistant_feedback_message_listing import AssistantFeedbackMessageListing  # noqa: F401
from openapi_server.models.billing_contract_feedback import BillingContractFeedback  # noqa: F401
from openapi_server.models.billing_contract_feedback_create import BillingContractFeedbackCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.support_message_feedback import SupportMessageFeedback  # noqa: F401
from openapi_server.models.support_message_feedback_create import SupportMessageFeedbackCreate  # noqa: F401


def test_c_reate_feedback_for_user_assistant_conversation(client: TestClient):
    """Test case for c_reate_feedback_for_user_assistant_conversation

    
    """
    assistant_feedback_conversation = {"rating":"rating","comment":"comment","category":"category"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/feedback".format(userID=56, assistantID=56, conversationID=56),
    #    headers=headers,
    #    json=assistant_feedback_conversation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_feedback_for_user_assistant_conversation_message(client: TestClient):
    """Test case for c_reate_feedback_for_user_assistant_conversation_message

    
    """
    assistant_feedback_message = {"rating":"rating","comment":"comment","category":"category"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/message/{messageID}/feedback".format(userID=56, assistantID=56, conversationID=56, messageID=56),
    #    headers=headers,
    #    json=assistant_feedback_message,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_feedback_for_user_billing_contract_subscription(client: TestClient):
    """Test case for c_reate_feedback_for_user_billing_contract_subscription

    
    """
    billing_contract_feedback = {"comment":"comment","category":"category"}

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
    #    "/user/{userID}/billing-contract-subscription/{billing-contract-subscriptionID}/feedback".format(userID=56, billing-contract-subscriptionID=56),
    #    headers=headers,
    #    json=billing_contract_feedback,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_feedback_for_user_chat_conversation_message(client: TestClient):
    """Test case for c_reate_feedback_for_user_chat_conversation_message

    
    """
    support_message_feedback = {"text":"text"}

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
    #    "/user/{userID}/chat-conversation/{chat-conversationID}/message/{messageID}/feedback".format(userID=56, chat-conversationID=56, messageID=56),
    #    headers=headers,
    #    json=support_message_feedback,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_feedback_for_user_chat_conversation_message(client: TestClient):
    """Test case for d_elete_feedback_for_user_chat_conversation_message

    
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
    #    "DELETE",
    #    "/user/{userID}/chat-conversation/{chat-conversationID}/message/{messageID}/feedback/{itemId}".format(userID=56, chat-conversationID=56, messageID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_feedback_for_user_assistant_conversation(client: TestClient):
    """Test case for list_all_feedback_for_user_assistant_conversation

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/feedback".format(userID=56, assistantID=56, conversationID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_feedback_for_user_assistant_conversation_message(client: TestClient):
    """Test case for list_all_feedback_for_user_assistant_conversation_message

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/message/{messageID}/feedback".format(userID=56, assistantID=56, conversationID=56, messageID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

