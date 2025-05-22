# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.payment_service_provider_draft_payment import PaymentServiceProviderDraftPayment  # noqa: F401
from openapi_server.models.payment_service_provider_draft_payment_create import PaymentServiceProviderDraftPaymentCreate  # noqa: F401
from openapi_server.models.payment_service_provider_draft_payment_listing import PaymentServiceProviderDraftPaymentListing  # noqa: F401
from openapi_server.models.payment_service_provider_draft_payment_oauth_request_listing import PaymentServiceProviderDraftPaymentOauthRequestListing  # noqa: F401
from openapi_server.models.payment_service_provider_draft_payment_read import PaymentServiceProviderDraftPaymentRead  # noqa: F401
from openapi_server.models.payment_service_provider_draft_payment_update import PaymentServiceProviderDraftPaymentUpdate  # noqa: F401


def test_c_reate_payment_service_provider_draft_payment_for_user(client: TestClient):
    """Test case for c_reate_payment_service_provider_draft_payment_for_user

    
    """
    payment_service_provider_draft_payment = {"counterparty_name":"counterparty_name","amount":{"currency":"currency","value":"value"},"counterparty_iban":"counterparty_iban","description":"description","sender_name":"sender_name","sender_iban":"sender_iban","status":"status"}

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
    #    "/user/{userID}/payment-service-provider-draft-payment".format(userID=56),
    #    headers=headers,
    #    json=payment_service_provider_draft_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_payment_service_provider_draft_payment_for_user(client: TestClient):
    """Test case for list_all_payment_service_provider_draft_payment_for_user

    
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
    #    "/user/{userID}/payment-service-provider-draft-payment".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_payment_service_provider_draft_payment_for_user_oauth_request(client: TestClient):
    """Test case for list_all_payment_service_provider_draft_payment_for_user_oauth_request

    
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
    #    "/user/{userID}/oauth-request/{oauth-requestID}/payment-service-provider-draft-payment".format(userID=56, oauth-requestID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_payment_service_provider_draft_payment_for_user(client: TestClient):
    """Test case for r_ead_payment_service_provider_draft_payment_for_user

    
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
    #    "/user/{userID}/payment-service-provider-draft-payment/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_payment_service_provider_draft_payment_for_user(client: TestClient):
    """Test case for u_pdate_payment_service_provider_draft_payment_for_user

    
    """
    payment_service_provider_draft_payment = {"counterparty_name":"counterparty_name","amount":{"currency":"currency","value":"value"},"counterparty_iban":"counterparty_iban","description":"description","sender_name":"sender_name","sender_iban":"sender_iban","status":"status"}

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
    #    "/user/{userID}/payment-service-provider-draft-payment/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=payment_service_provider_draft_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

