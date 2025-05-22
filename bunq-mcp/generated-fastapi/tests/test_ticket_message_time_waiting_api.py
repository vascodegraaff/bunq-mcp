# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ticket_message_time_waiting import TicketMessageTimeWaiting  # noqa: F401
from openapi_server.models.ticket_message_time_waiting_create import TicketMessageTimeWaitingCreate  # noqa: F401
from openapi_server.models.ticket_message_time_waiting_listing import TicketMessageTimeWaitingListing  # noqa: F401


def test_c_reate_ticket_message_time_waiting(client: TestClient):
    """Test case for c_reate_ticket_message_time_waiting

    
    """
    ticket_message_time_waiting = {"time_waiting_expected":0,"message":"message"}

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
    #    "/ticket-message-time-waiting",
    #    headers=headers,
    #    json=ticket_message_time_waiting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_ticket_message_time_waiting(client: TestClient):
    """Test case for list_all_ticket_message_time_waiting

    
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
    #    "/ticket-message-time-waiting",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

