# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.adyen_merchant_transaction import AdyenMerchantTransaction  # noqa: F401
from openapi_server.models.adyen_merchant_transaction_create import AdyenMerchantTransactionCreate  # noqa: F401
from openapi_server.models.adyen_merchant_transaction_listing import AdyenMerchantTransactionListing  # noqa: F401
from openapi_server.models.adyen_merchant_transaction_read import AdyenMerchantTransactionRead  # noqa: F401
from openapi_server.models.adyen_merchant_transaction_update import AdyenMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_adyen_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for c_reate_adyen_merchant_transaction_for_user_monetary_account

    
    """
    adyen_merchant_transaction = {"payment_detail":["payment_detail","payment_detail"],"adyen_checkout_sdk_response":["adyen_checkout_sdk_response","adyen_checkout_sdk_response"],"should_store_payment_method":1,"adyen_browser_data":["adyen_browser_data","adyen_browser_data"],"status":"status"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-merchant-transaction".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #    json=adyen_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_adyen_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for list_all_adyen_merchant_transaction_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-merchant-transaction".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_adyen_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_adyen_merchant_transaction_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-merchant-transaction/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_adyen_merchant_transaction_for_user_monetary_account(client: TestClient):
    """Test case for u_pdate_adyen_merchant_transaction_for_user_monetary_account

    
    """
    adyen_merchant_transaction = {"payment_detail":["payment_detail","payment_detail"],"adyen_checkout_sdk_response":["adyen_checkout_sdk_response","adyen_checkout_sdk_response"],"should_store_payment_method":1,"adyen_browser_data":["adyen_browser_data","adyen_browser_data"],"status":"status"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-merchant-transaction/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #    json=adyen_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

