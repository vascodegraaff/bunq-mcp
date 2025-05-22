# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ticket_transfer import TicketTransfer  # noqa: F401
from openapi_server.models.ticket_transfer_listing import TicketTransferListing  # noqa: F401
from openapi_server.models.ticket_transfer_update import TicketTransferUpdate  # noqa: F401


def test_list_all_transfer_for_user_ticket(client: TestClient):
    """Test case for list_all_transfer_for_user_ticket

    
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
    #    "/user/{userID}/ticket/{ticketID}/transfer".format(userID=56, ticketID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_transfer_for_user_ticket(client: TestClient):
    """Test case for u_pdate_transfer_for_user_ticket

    
    """
    ticket_transfer = {"user_id":0}

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
    #    "/user/{userID}/ticket/{ticketID}/transfer/{itemId}".format(userID=56, ticketID=56, itemId=56),
    #    headers=headers,
    #    json=ticket_transfer,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

