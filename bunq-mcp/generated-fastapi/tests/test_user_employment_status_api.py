# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_employment_status import UserEmploymentStatus  # noqa: F401
from openapi_server.models.user_employment_status_create import UserEmploymentStatusCreate  # noqa: F401
from openapi_server.models.user_employment_status_listing import UserEmploymentStatusListing  # noqa: F401
from openapi_server.models.user_employment_status_update import UserEmploymentStatusUpdate  # noqa: F401


def test_c_reate_user_employment_status_for_user(client: TestClient):
    """Test case for c_reate_user_employment_status_for_user

    
    """
    user_employment_status = {"type":"type"}

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
    #    "/user/{userID}/user-employment-status".format(userID=56),
    #    headers=headers,
    #    json=user_employment_status,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_employment_status_for_user(client: TestClient):
    """Test case for list_all_user_employment_status_for_user

    
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
    #    "/user/{userID}/user-employment-status".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_employment_status_for_user(client: TestClient):
    """Test case for u_pdate_user_employment_status_for_user

    
    """
    user_employment_status = {"type":"type"}

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
    #    "/user/{userID}/user-employment-status/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=user_employment_status,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

