# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_approval_time_waiting import UserApprovalTimeWaiting  # noqa: F401
from openapi_server.models.user_approval_time_waiting_create import UserApprovalTimeWaitingCreate  # noqa: F401
from openapi_server.models.user_approval_time_waiting_listing import UserApprovalTimeWaitingListing  # noqa: F401


def test_c_reate_user_approval_time_waiting(client: TestClient):
    """Test case for c_reate_user_approval_time_waiting

    
    """
    user_approval_time_waiting = {"time_waiting_expected":0,"user_type":"user_type","day_of_week":"day_of_week"}

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
    #    "/user-approval-time-waiting",
    #    headers=headers,
    #    json=user_approval_time_waiting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_approval_time_waiting(client: TestClient):
    """Test case for list_all_user_approval_time_waiting

    
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
    #    "/user-approval-time-waiting",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

