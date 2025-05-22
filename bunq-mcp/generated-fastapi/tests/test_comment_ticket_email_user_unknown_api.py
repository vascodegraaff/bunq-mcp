# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_comment_email_without_alias import AdminCommentEmailWithoutAlias  # noqa: F401
from openapi_server.models.admin_comment_email_without_alias_create import AdminCommentEmailWithoutAliasCreate  # noqa: F401
from openapi_server.models.admin_comment_email_without_alias_listing import AdminCommentEmailWithoutAliasListing  # noqa: F401
from openapi_server.models.admin_comment_email_without_alias_update import AdminCommentEmailWithoutAliasUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_comment_ticket_email_user_unknown_for_ticket(client: TestClient):
    """Test case for c_reate_comment_ticket_email_user_unknown_for_ticket

    
    """
    admin_comment_email_without_alias = {"visibility":"visibility","attachment_id":0,"text":"text","status":"status"}

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
    #    "/ticket/{ticketID}/comment-ticket-email-user-unknown".format(ticketID=56),
    #    headers=headers,
    #    json=admin_comment_email_without_alias,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_comment_ticket_email_user_unknown_for_ticket(client: TestClient):
    """Test case for list_all_comment_ticket_email_user_unknown_for_ticket

    
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
    #    "/ticket/{ticketID}/comment-ticket-email-user-unknown".format(ticketID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_comment_ticket_email_user_unknown_for_ticket(client: TestClient):
    """Test case for u_pdate_comment_ticket_email_user_unknown_for_ticket

    
    """
    admin_comment_email_without_alias = {"visibility":"visibility","attachment_id":0,"text":"text","status":"status"}

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
    #    "/ticket/{ticketID}/comment-ticket-email-user-unknown/{itemId}".format(ticketID=56, itemId=56),
    #    headers=headers,
    #    json=admin_comment_email_without_alias,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

