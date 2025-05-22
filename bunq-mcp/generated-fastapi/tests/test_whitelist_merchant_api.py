# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.whitelist_merchant import WhitelistMerchant  # noqa: F401
from openapi_server.models.whitelist_merchant_create import WhitelistMerchantCreate  # noqa: F401
from openapi_server.models.whitelist_merchant_listing import WhitelistMerchantListing  # noqa: F401
from openapi_server.models.whitelist_merchant_monetary_account_paying_listing import WhitelistMerchantMonetaryAccountPayingListing  # noqa: F401
from openapi_server.models.whitelist_merchant_monetary_account_paying_read import WhitelistMerchantMonetaryAccountPayingRead  # noqa: F401
from openapi_server.models.whitelist_merchant_read import WhitelistMerchantRead  # noqa: F401
from openapi_server.models.whitelist_merchant_update import WhitelistMerchantUpdate  # noqa: F401


def test_c_reate_whitelist_merchant_for_user(client: TestClient):
    """Test case for c_reate_whitelist_merchant_for_user

    
    """
    whitelist_merchant = {"mastercard_merchant_id":"mastercard_merchant_id","maximum_amount_per_payment":{"currency":"currency","value":"value"},"merchant_identifier":"merchant_identifier","external_merchant_id":"external_merchant_id","maximum_amount_per_month":{"currency":"currency","value":"value"},"monetary_account_paying_id":0,"merchant_name":"merchant_name","merchant_id":"merchant_id"}

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
    #    "/user/{userID}/whitelist-merchant".format(userID=56),
    #    headers=headers,
    #    json=whitelist_merchant,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_whitelist_merchant_for_user(client: TestClient):
    """Test case for d_elete_whitelist_merchant_for_user

    
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
    #    "/user/{userID}/whitelist-merchant/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_whitelist_merchant_for_user(client: TestClient):
    """Test case for list_all_whitelist_merchant_for_user

    
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
    #    "/user/{userID}/whitelist-merchant".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_whitelist_merchant_for_user_monetary_account(client: TestClient):
    """Test case for list_all_whitelist_merchant_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist-merchant".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_whitelist_merchant_for_user(client: TestClient):
    """Test case for r_ead_whitelist_merchant_for_user

    
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
    #    "/user/{userID}/whitelist-merchant/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_whitelist_merchant_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_whitelist_merchant_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist-merchant/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_whitelist_merchant_for_user(client: TestClient):
    """Test case for u_pdate_whitelist_merchant_for_user

    
    """
    whitelist_merchant = {"mastercard_merchant_id":"mastercard_merchant_id","maximum_amount_per_payment":{"currency":"currency","value":"value"},"merchant_identifier":"merchant_identifier","external_merchant_id":"external_merchant_id","maximum_amount_per_month":{"currency":"currency","value":"value"},"monetary_account_paying_id":0,"merchant_name":"merchant_name","merchant_id":"merchant_id"}

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
    #    "/user/{userID}/whitelist-merchant/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=whitelist_merchant,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

