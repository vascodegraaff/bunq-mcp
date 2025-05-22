# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_incident import AdminIncident  # noqa: F401
from openapi_server.models.admin_incident_create import AdminIncidentCreate  # noqa: F401
from openapi_server.models.admin_incident_listing import AdminIncidentListing  # noqa: F401
from openapi_server.models.admin_incident_read import AdminIncidentRead  # noqa: F401
from openapi_server.models.admin_incident_update import AdminIncidentUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_incident(client: TestClient):
    """Test case for c_reate_admin_incident

    
    """
    admin_incident = {"title_resolved":["title_resolved","title_resolved"],"title_ongoing":["title_ongoing","title_ongoing"],"all_display_location":["all_display_location","all_display_location"],"type":"type","description_resolved":["description_resolved","description_resolved"],"emoji_resolved":"emoji_resolved","url":"url","status":"status","description_ongoing":["description_ongoing","description_ongoing"]}

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
    #    "/admin-incident",
    #    headers=headers,
    #    json=admin_incident,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_incident(client: TestClient):
    """Test case for list_all_admin_incident

    
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
    #    "/admin-incident",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_incident(client: TestClient):
    """Test case for r_ead_admin_incident

    
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
    #    "/admin-incident/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_incident(client: TestClient):
    """Test case for u_pdate_admin_incident

    
    """
    admin_incident = {"title_resolved":["title_resolved","title_resolved"],"title_ongoing":["title_ongoing","title_ongoing"],"all_display_location":["all_display_location","all_display_location"],"type":"type","description_resolved":["description_resolved","description_resolved"],"emoji_resolved":"emoji_resolved","url":"url","status":"status","description_ongoing":["description_ongoing","description_ongoing"]}

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
    #    "/admin-incident/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_incident,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

