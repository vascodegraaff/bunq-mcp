# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_iberpay_return_request_incoming import AdminIberpayReturnRequestIncoming  # noqa: F401
from openapi_server.models.admin_iberpay_return_request_incoming_listing import AdminIberpayReturnRequestIncomingListing  # noqa: F401
from openapi_server.models.admin_iberpay_return_request_incoming_read import AdminIberpayReturnRequestIncomingRead  # noqa: F401
from openapi_server.models.admin_iberpay_return_request_incoming_update import AdminIberpayReturnRequestIncomingUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_list_all_admin_iberpay_return_request_incoming(client: TestClient):
    """Test case for list_all_admin_iberpay_return_request_incoming

    
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
    #    "/admin-iberpay-return-request-incoming",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_iberpay_return_request_incoming(client: TestClient):
    """Test case for r_ead_admin_iberpay_return_request_incoming

    
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
    #    "/admin-iberpay-return-request-incoming/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_iberpay_return_request_incoming(client: TestClient):
    """Test case for u_pdate_admin_iberpay_return_request_incoming

    
    """
    admin_iberpay_return_request_incoming = {"reject_reason":"reject_reason","all_additional_information":["all_additional_information","all_additional_information"],"status":"status"}

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
    #    "/admin-iberpay-return-request-incoming/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_iberpay_return_request_incoming,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

