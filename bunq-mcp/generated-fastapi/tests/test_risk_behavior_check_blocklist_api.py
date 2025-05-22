# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.risk_behavior_check_blocklist import RiskBehaviorCheckBlocklist  # noqa: F401
from openapi_server.models.risk_behavior_check_blocklist_create import RiskBehaviorCheckBlocklistCreate  # noqa: F401
from openapi_server.models.risk_behavior_check_blocklist_listing import RiskBehaviorCheckBlocklistListing  # noqa: F401
from openapi_server.models.risk_behavior_check_blocklist_read import RiskBehaviorCheckBlocklistRead  # noqa: F401
from openapi_server.models.risk_behavior_check_blocklist_update import RiskBehaviorCheckBlocklistUpdate  # noqa: F401


def test_c_reate_risk_behavior_check_blocklist(client: TestClient):
    """Test case for c_reate_risk_behavior_check_blocklist

    
    """
    risk_behavior_check_blocklist = {"time_expiry":"time_expiry","external_model_id":0,"external_model_name":"external_model_name","comment":"comment","status":"status"}

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
    #    "/risk-behavior-check-blocklist",
    #    headers=headers,
    #    json=risk_behavior_check_blocklist,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_risk_behavior_check_blocklist(client: TestClient):
    """Test case for list_all_risk_behavior_check_blocklist

    
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
    #    "/risk-behavior-check-blocklist",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_risk_behavior_check_blocklist(client: TestClient):
    """Test case for r_ead_risk_behavior_check_blocklist

    
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
    #    "/risk-behavior-check-blocklist/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_risk_behavior_check_blocklist(client: TestClient):
    """Test case for u_pdate_risk_behavior_check_blocklist

    
    """
    risk_behavior_check_blocklist = {"time_expiry":"time_expiry","external_model_id":0,"external_model_name":"external_model_name","comment":"comment","status":"status"}

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
    #    "/risk-behavior-check-blocklist/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=risk_behavior_check_blocklist,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

