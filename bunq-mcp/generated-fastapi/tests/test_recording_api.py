# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_recording import UserRecording  # noqa: F401
from openapi_server.models.user_recording_create import UserRecordingCreate  # noqa: F401
from openapi_server.models.user_recording_listing import UserRecordingListing  # noqa: F401
from openapi_server.models.user_recording_read import UserRecordingRead  # noqa: F401
from openapi_server.models.user_recording_update import UserRecordingUpdate  # noqa: F401
from openapi_server.models.vonage_call_incoming_recording import VonageCallIncomingRecording  # noqa: F401
from openapi_server.models.vonage_call_incoming_recording_create import VonageCallIncomingRecordingCreate  # noqa: F401


def test_c_reate_recording_for_user(client: TestClient):
    """Test case for c_reate_recording_for_user

    
    """
    user_recording = {"attachment_id":0,"audio_type":"audio_type","video_type":"video_type","status":"status"}

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
    #    "/user/{userID}/recording".format(userID=56),
    #    headers=headers,
    #    json=user_recording,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_recording_for_vonage_call_incoming(client: TestClient):
    """Test case for c_reate_recording_for_vonage_call_incoming

    
    """
    vonage_call_incoming_recording = {"start_time":"start_time","recording_url":"recording_url","size":0,"recording_uuid":"recording_uuid","end_time":"end_time","conversation_uuid":"conversation_uuid","timestamp":"timestamp"}

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
    #    "/vonage-call-incoming/{vonage-call-incomingID}/recording".format(vonage-call-incomingID=56),
    #    headers=headers,
    #    json=vonage_call_incoming_recording,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_recording_for_user(client: TestClient):
    """Test case for list_all_recording_for_user

    
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
    #    "/user/{userID}/recording".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_recording_for_user(client: TestClient):
    """Test case for r_ead_recording_for_user

    
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
    #    "/user/{userID}/recording/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_recording_for_user(client: TestClient):
    """Test case for u_pdate_recording_for_user

    
    """
    user_recording = {"attachment_id":0,"audio_type":"audio_type","video_type":"video_type","status":"status"}

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
    #    "/user/{userID}/recording/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=user_recording,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

