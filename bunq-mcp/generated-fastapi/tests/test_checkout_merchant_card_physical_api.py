# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.checkout_merchant_card_physical import CheckoutMerchantCardPhysical  # noqa: F401
from openapi_server.models.checkout_merchant_card_physical_create import CheckoutMerchantCardPhysicalCreate  # noqa: F401
from openapi_server.models.checkout_merchant_card_physical_listing import CheckoutMerchantCardPhysicalListing  # noqa: F401
from openapi_server.models.checkout_merchant_card_physical_read import CheckoutMerchantCardPhysicalRead  # noqa: F401
from openapi_server.models.checkout_merchant_card_physical_update import CheckoutMerchantCardPhysicalUpdate  # noqa: F401


def test_c_reate_checkout_merchant_card_physical_for_user(client: TestClient):
    """Test case for c_reate_checkout_merchant_card_physical_for_user

    
    """
    checkout_merchant_card_physical = {"expiry_month":"expiry_month","primary_account_number":"primary_account_number","card_verification_code":"card_verification_code","description":"description","expiry_year":"expiry_year"}

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
    #    "/user/{userID}/checkout-merchant-card-physical".format(userID=56),
    #    headers=headers,
    #    json=checkout_merchant_card_physical,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_checkout_merchant_card_physical_for_user(client: TestClient):
    """Test case for d_elete_checkout_merchant_card_physical_for_user

    
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
    #    "DELETE",
    #    "/user/{userID}/checkout-merchant-card-physical/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_checkout_merchant_card_physical_for_user(client: TestClient):
    """Test case for list_all_checkout_merchant_card_physical_for_user

    
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
    #    "/user/{userID}/checkout-merchant-card-physical".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_checkout_merchant_card_physical_for_user(client: TestClient):
    """Test case for r_ead_checkout_merchant_card_physical_for_user

    
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
    #    "/user/{userID}/checkout-merchant-card-physical/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_checkout_merchant_card_physical_for_user(client: TestClient):
    """Test case for u_pdate_checkout_merchant_card_physical_for_user

    
    """
    checkout_merchant_card_physical = {"expiry_month":"expiry_month","primary_account_number":"primary_account_number","card_verification_code":"card_verification_code","description":"description","expiry_year":"expiry_year"}

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
    #    "/user/{userID}/checkout-merchant-card-physical/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=checkout_merchant_card_physical,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

