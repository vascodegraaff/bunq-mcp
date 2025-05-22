# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.assistant_message_question import AssistantMessageQuestion  # noqa: F401
from openapi_server.models.assistant_message_question_create import AssistantMessageQuestionCreate  # noqa: F401
from openapi_server.models.assistant_message_question_listing import AssistantMessageQuestionListing  # noqa: F401
from openapi_server.models.assistant_message_question_read import AssistantMessageQuestionRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_question_for_user_assistant_conversation(client: TestClient):
    """Test case for c_reate_question_for_user_assistant_conversation

    
    """
    assistant_message_question = {"reference_external":"reference_external","question":"question","conversation_id":0,"all_attachment":[{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"},{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"}],"context":[{"event_id":6,"app_location":"app_location","monetary_account_id":1,"monetary_account_type":"monetary_account_type","type":"type"},{"event_id":6,"app_location":"app_location","monetary_account_id":1,"monetary_account_type":"monetary_account_type","type":"type"}],"all_attachment_id":["all_attachment_id","all_attachment_id"],"question_translated":"question_translated","status":"status"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/question".format(userID=56, assistantID=56, conversationID=56),
    #    headers=headers,
    #    json=assistant_message_question,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_question_for_user_assistant_conversation(client: TestClient):
    """Test case for list_all_question_for_user_assistant_conversation

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/question".format(userID=56, assistantID=56, conversationID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_question_for_user_assistant_conversation(client: TestClient):
    """Test case for r_ead_question_for_user_assistant_conversation

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/question/{itemId}".format(userID=56, assistantID=56, conversationID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

