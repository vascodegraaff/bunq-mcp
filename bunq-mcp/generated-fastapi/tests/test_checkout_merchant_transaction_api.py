# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_checkout_merchant_transaction_read import AdminCheckoutMerchantTransactionRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.checkout_merchant_transaction import CheckoutMerchantTransaction  # noqa: F401
from openapi_server.models.checkout_merchant_transaction_create import CheckoutMerchantTransactionCreate  # noqa: F401
from openapi_server.models.checkout_merchant_transaction_listing import CheckoutMerchantTransactionListing  # noqa: F401
from openapi_server.models.checkout_merchant_transaction_read import CheckoutMerchantTransactionRead  # noqa: F401


def test_c_reate_checkout_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for c_reate_checkout_merchant_transaction_for_user_monetary_account

    
    """
    checkout_merchant_transaction = {"checkout_merchant_card_id":0,"amount_requested":{"currency":"currency","value":"value"},"apple_pay_payment_token_data":"apple_pay_payment_token_data","token_type":"token_type"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/checkout-merchant-transaction".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #    json=checkout_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_checkout_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for list_all_checkout_merchant_transaction_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/checkout-merchant-transaction".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_checkout_merchant_transaction(client: TestClient):
    """Test case for r_ead_checkout_merchant_transaction

    
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
    #    "/checkout-merchant-transaction/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_checkout_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_checkout_merchant_transaction_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/checkout-merchant-transaction/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

