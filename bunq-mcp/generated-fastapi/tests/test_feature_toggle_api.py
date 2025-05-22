# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.feature_toggle import FeatureToggle  # noqa: F401
from openapi_server.models.feature_toggle_create import FeatureToggleCreate  # noqa: F401
from openapi_server.models.feature_toggle_listing import FeatureToggleListing  # noqa: F401
from openapi_server.models.feature_toggle_read import FeatureToggleRead  # noqa: F401
from openapi_server.models.feature_toggle_update import FeatureToggleUpdate  # noqa: F401


def test_c_reate_feature_toggle_for_user(client: TestClient):
    """Test case for c_reate_feature_toggle_for_user

    
    """
    feature_toggle = {"time_start":"time_start","restrictions":[{"country":"country","ip":"ip","tag_user":"tag_user","operating_system_name":"operating_system_name"},{"country":"country","ip":"ip","tag_user":"tag_user","operating_system_name":"operating_system_name"}],"comment":"comment","time_end":"time_end","type":"type","status":"status"}

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
    #    "/user/{userID}/feature-toggle".format(userID=56),
    #    headers=headers,
    #    json=feature_toggle,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_feature_toggle_for_user(client: TestClient):
    """Test case for list_all_feature_toggle_for_user

    
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
    #    "/user/{userID}/feature-toggle".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_feature_toggle_for_user(client: TestClient):
    """Test case for r_ead_feature_toggle_for_user

    
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
    #    "/user/{userID}/feature-toggle/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_feature_toggle_for_user(client: TestClient):
    """Test case for u_pdate_feature_toggle_for_user

    
    """
    feature_toggle = {"time_start":"time_start","restrictions":[{"country":"country","ip":"ip","tag_user":"tag_user","operating_system_name":"operating_system_name"},{"country":"country","ip":"ip","tag_user":"tag_user","operating_system_name":"operating_system_name"}],"comment":"comment","time_end":"time_end","type":"type","status":"status"}

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
    #    "/user/{userID}/feature-toggle/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=feature_toggle,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

