# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_payment_request import AdminPaymentRequest  # noqa: F401
from openapi_server.models.admin_payment_request_create import AdminPaymentRequestCreate  # noqa: F401
from openapi_server.models.admin_payment_request_listing import AdminPaymentRequestListing  # noqa: F401
from openapi_server.models.admin_payment_request_read import AdminPaymentRequestRead  # noqa: F401
from openapi_server.models.admin_payment_request_update import AdminPaymentRequestUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_payment_request(client: TestClient):
    """Test case for c_reate_admin_payment_request

    
    """
    admin_payment_request = {"monetary_account_origin_id":6,"counterparty_name":"counterparty_name","amount":{"currency":"currency","value":"value"},"counterparty_iban":"counterparty_iban","user_id":0,"counterparty_alias":{"service":"service","name":"name","type":"type","value":"value"},"description":"description","comment":"comment","status":"status"}

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
    #    "/admin-payment-request",
    #    headers=headers,
    #    json=admin_payment_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_payment_request(client: TestClient):
    """Test case for list_all_admin_payment_request

    
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
    #    "/admin-payment-request",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_payment_request(client: TestClient):
    """Test case for r_ead_admin_payment_request

    
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
    #    "/admin-payment-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_payment_request(client: TestClient):
    """Test case for u_pdate_admin_payment_request

    
    """
    admin_payment_request = {"monetary_account_origin_id":6,"counterparty_name":"counterparty_name","amount":{"currency":"currency","value":"value"},"counterparty_iban":"counterparty_iban","user_id":0,"counterparty_alias":{"service":"service","name":"name","type":"type","value":"value"},"description":"description","comment":"comment","status":"status"}

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
    #    "/admin-payment-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_payment_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

