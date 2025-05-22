# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.vonage_call_incoming_phone_support_emergency_agent import VonageCallIncomingPhoneSupportEmergencyAgent  # noqa: F401
from openapi_server.models.vonage_call_incoming_phone_support_emergency_agent_listing import VonageCallIncomingPhoneSupportEmergencyAgentListing  # noqa: F401
from openapi_server.models.vonage_call_incoming_phone_support_emergency_agent_read import VonageCallIncomingPhoneSupportEmergencyAgentRead  # noqa: F401
from openapi_server.models.vonage_call_incoming_phone_support_emergency_agent_update import VonageCallIncomingPhoneSupportEmergencyAgentUpdate  # noqa: F401


def test_list_all_vonage_phone_support_emergency_agent_call(client: TestClient):
    """Test case for list_all_vonage_phone_support_emergency_agent_call

    
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
    #    "/vonage-phone-support-emergency-agent-call",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_vonage_phone_support_emergency_agent_call(client: TestClient):
    """Test case for r_ead_vonage_phone_support_emergency_agent_call

    
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
    #    "/vonage-phone-support-emergency-agent-call/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_vonage_phone_support_emergency_agent_call(client: TestClient):
    """Test case for u_pdate_vonage_phone_support_emergency_agent_call

    
    """
    vonage_call_incoming_phone_support_emergency_agent = {"language":"language","translation_status":"translation_status"}

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
    #    "/vonage-phone-support-emergency-agent-call/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=vonage_call_incoming_phone_support_emergency_agent,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

