# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.assistant_action_suggestion import AssistantActionSuggestion  # noqa: F401
from openapi_server.models.assistant_action_suggestion_create import AssistantActionSuggestionCreate  # noqa: F401
from openapi_server.models.assistant_action_suggestion_listing import AssistantActionSuggestionListing  # noqa: F401
from openapi_server.models.assistant_action_suggestion_read import AssistantActionSuggestionRead  # noqa: F401
from openapi_server.models.assistant_action_suggestion_update import AssistantActionSuggestionUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_action_suggestion_for_user_assistant(client: TestClient):
    """Test case for c_reate_action_suggestion_for_user_assistant

    
    """
    assistant_action_suggestion = {"locations":["locations","locations"],"status":"status"}

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
    #    "/user/{userID}/assistant/{assistantID}/action-suggestion".format(userID=56, assistantID=56),
    #    headers=headers,
    #    json=assistant_action_suggestion,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_action_suggestion_for_user_assistant(client: TestClient):
    """Test case for list_all_action_suggestion_for_user_assistant

    
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
    #    "/user/{userID}/assistant/{assistantID}/action-suggestion".format(userID=56, assistantID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_action_suggestion_for_user_assistant(client: TestClient):
    """Test case for r_ead_action_suggestion_for_user_assistant

    
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
    #    "/user/{userID}/assistant/{assistantID}/action-suggestion/{itemId}".format(userID=56, assistantID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_action_suggestion_for_user_assistant(client: TestClient):
    """Test case for u_pdate_action_suggestion_for_user_assistant

    
    """
    assistant_action_suggestion = {"locations":["locations","locations"],"status":"status"}

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
    #    "/user/{userID}/assistant/{assistantID}/action-suggestion/{itemId}".format(userID=56, assistantID=56, itemId=56),
    #    headers=headers,
    #    json=assistant_action_suggestion,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

