# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_admin_support_team import UserAdminSupportTeam  # noqa: F401
from openapi_server.models.user_admin_support_team_create import UserAdminSupportTeamCreate  # noqa: F401
from openapi_server.models.user_admin_support_team_listing import UserAdminSupportTeamListing  # noqa: F401
from openapi_server.models.user_admin_support_team_update import UserAdminSupportTeamUpdate  # noqa: F401


def test_c_reate_support_team(client: TestClient):
    """Test case for c_reate_support_team

    
    """
    user_admin_support_team = {"user_admin_id":0,"team":"team"}

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
    #    "/support-team",
    #    headers=headers,
    #    json=user_admin_support_team,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_support_team(client: TestClient):
    """Test case for list_all_support_team

    
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
    #    "/support-team",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_support_team(client: TestClient):
    """Test case for u_pdate_support_team

    
    """
    user_admin_support_team = {"user_admin_id":0,"team":"team"}

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
    #    "/support-team/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=user_admin_support_team,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

