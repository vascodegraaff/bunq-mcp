# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.marketing_communication import MarketingCommunication  # noqa: F401
from openapi_server.models.marketing_communication_create import MarketingCommunicationCreate  # noqa: F401
from openapi_server.models.marketing_communication_update import MarketingCommunicationUpdate  # noqa: F401


def test_c_reate_marketing_communication_for_user(client: TestClient):
    """Test case for c_reate_marketing_communication_for_user

    
    """
    marketing_communication = {"event_body":"event_body","color":"color","button_text_primary":"button_text_primary","icon":"icon","event_title":"event_title","secret":"secret","uuid":"uuid","button_url_primary":"button_url_primary","button_url_secondary":"button_url_secondary","template_project_id":"template_project_id","notification_body":"notification_body","notification_title":"notification_title","button_text_secondary":"button_text_secondary","status":"status"}

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
    #    "/user/{userID}/marketing-communication".format(userID=56),
    #    headers=headers,
    #    json=marketing_communication,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_marketing_communication_for_user(client: TestClient):
    """Test case for u_pdate_marketing_communication_for_user

    
    """
    marketing_communication = {"event_body":"event_body","color":"color","button_text_primary":"button_text_primary","icon":"icon","event_title":"event_title","secret":"secret","uuid":"uuid","button_url_primary":"button_url_primary","button_url_secondary":"button_url_secondary","template_project_id":"template_project_id","notification_body":"notification_body","notification_title":"notification_title","button_text_secondary":"button_text_secondary","status":"status"}

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
    #    "/user/{userID}/marketing-communication/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=marketing_communication,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

