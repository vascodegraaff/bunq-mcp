# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.payment_suspended_outgoing import PaymentSuspendedOutgoing  # noqa: F401
from openapi_server.models.payment_suspended_outgoing_read import PaymentSuspendedOutgoingRead  # noqa: F401
from openapi_server.models.payment_suspended_outgoing_update import PaymentSuspendedOutgoingUpdate  # noqa: F401


def test_r_ead_payment_suspended_outgoing_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_payment_suspended_outgoing_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-suspended-outgoing/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_payment_suspended_outgoing_for_user_monetary_account(client: TestClient):
    """Test case for u_pdate_payment_suspended_outgoing_for_user_monetary_account

    
    """
    payment_suspended_outgoing = {"time_execution":"time_execution","monetary_account_id":"monetary_account_id","status":"status"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-suspended-outgoing/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #    json=payment_suspended_outgoing,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

