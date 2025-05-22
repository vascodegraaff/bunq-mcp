# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.assistant_message_answer import AssistantMessageAnswer  # noqa: F401
from openapi_server.models.assistant_message_answer_create import AssistantMessageAnswerCreate  # noqa: F401
from openapi_server.models.assistant_message_answer_read import AssistantMessageAnswerRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_answer_for_user_assistant_conversation(client: TestClient):
    """Test case for c_reate_answer_for_user_assistant_conversation

    
    """
    assistant_message_answer = {"agent_name":"agent_name","answer":"answer","conversation_id":0,"text":"text","answer_translated":"answer_translated","agent_avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"question_id":6,"status":"status"}

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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/answer".format(userID=56, assistantID=56, conversationID=56),
    #    headers=headers,
    #    json=assistant_message_answer,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_answer_for_user_assistant_conversation(client: TestClient):
    """Test case for r_ead_answer_for_user_assistant_conversation

    
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
    #    "/user/{userID}/assistant/{assistantID}/conversation/{conversationID}/answer/{itemId}".format(userID=56, assistantID=56, conversationID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

