# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.instant_payment_recall_request_incoming import InstantPaymentRecallRequestIncoming  # noqa: F401
from openapi_server.models.instant_payment_recall_request_incoming_listing import InstantPaymentRecallRequestIncomingListing  # noqa: F401
from openapi_server.models.instant_payment_recall_request_incoming_read import InstantPaymentRecallRequestIncomingRead  # noqa: F401
from openapi_server.models.instant_payment_recall_request_incoming_update import InstantPaymentRecallRequestIncomingUpdate  # noqa: F401


def test_list_all_instant_payment_recall_request_incoming(client: TestClient):
    """Test case for list_all_instant_payment_recall_request_incoming

    
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
    #    "/instant-payment-recall-request-incoming",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_instant_payment_recall_request_incoming(client: TestClient):
    """Test case for r_ead_instant_payment_recall_request_incoming

    
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
    #    "/instant-payment-recall-request-incoming/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_instant_payment_recall_request_incoming(client: TestClient):
    """Test case for u_pdate_instant_payment_recall_request_incoming

    
    """
    instant_payment_recall_request_incoming = {"additional_information":"additional_information","amount_returned":{"currency":"currency","value":"value"},"reject_reason":"reject_reason","status":"status"}

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
    #    "/instant-payment-recall-request-incoming/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=instant_payment_recall_request_incoming,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

