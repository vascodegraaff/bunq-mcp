# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.tag_ticket import TagTicket  # noqa: F401
from openapi_server.models.tag_ticket_create import TagTicketCreate  # noqa: F401
from openapi_server.models.tag_ticket_listing import TagTicketListing  # noqa: F401


def test_c_reate_tag_ticket_for_ticket(client: TestClient):
    """Test case for c_reate_tag_ticket_for_ticket

    
    """
    tag_ticket = {"tag":"tag","choice":{"tag_type":"tag_type","created":"created","scope":"scope","id":2,"choice":"choice","updated":"updated","status":"status"},"ticket_id":4}

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
    #    "/ticket/{ticketID}/tag-ticket".format(ticketID=56),
    #    headers=headers,
    #    json=tag_ticket,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_tag_ticket_for_ticket(client: TestClient):
    """Test case for list_all_tag_ticket_for_ticket

    
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
    #    "/ticket/{ticketID}/tag-ticket".format(ticketID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

