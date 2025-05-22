# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.travel_assistant_recommendation import TravelAssistantRecommendation  # noqa: F401
from openapi_server.models.travel_assistant_recommendation_create import TravelAssistantRecommendationCreate  # noqa: F401
from openapi_server.models.travel_assistant_recommendation_update import TravelAssistantRecommendationUpdate  # noqa: F401


def test_c_reate_recommendation_for_user_travel_assistant_country(client: TestClient):
    """Test case for c_reate_recommendation_for_user_travel_assistant_country

    
    """
    travel_assistant_recommendation = {"color":"color","icon":"icon","description":["description","description"],"title":["title","title"],"order":"order"}

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
    #    "/user/{userID}/travel-assistant-country/{travel-assistant-countryID}/recommendation".format(userID=56, travel-assistant-countryID=56),
    #    headers=headers,
    #    json=travel_assistant_recommendation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_recommendation_for_user_travel_assistant_country(client: TestClient):
    """Test case for d_elete_recommendation_for_user_travel_assistant_country

    
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
    #    "/user/{userID}/travel-assistant-country/{travel-assistant-countryID}/recommendation/{itemId}".format(userID=56, travel-assistant-countryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_recommendation_for_user_travel_assistant_country(client: TestClient):
    """Test case for u_pdate_recommendation_for_user_travel_assistant_country

    
    """
    travel_assistant_recommendation = {"color":"color","icon":"icon","description":["description","description"],"title":["title","title"],"order":"order"}

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
    #    "/user/{userID}/travel-assistant-country/{travel-assistant-countryID}/recommendation/{itemId}".format(userID=56, travel-assistant-countryID=56, itemId=56),
    #    headers=headers,
    #    json=travel_assistant_recommendation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

