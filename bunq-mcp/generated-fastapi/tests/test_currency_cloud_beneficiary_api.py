# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary import CurrencyCloudBeneficiary  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_bunq_to import CurrencyCloudBeneficiaryBunqTo  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_bunq_to_create import CurrencyCloudBeneficiaryBunqToCreate  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_create import CurrencyCloudBeneficiaryCreate  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_listing import CurrencyCloudBeneficiaryListing  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_read import CurrencyCloudBeneficiaryRead  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_retool import CurrencyCloudBeneficiaryRetool  # noqa: F401
from openapi_server.models.currency_cloud_beneficiary_retool_create import CurrencyCloudBeneficiaryRetoolCreate  # noqa: F401


def test_c_reate_currency_cloud_beneficiary(client: TestClient):
    """Test case for c_reate_currency_cloud_beneficiary

    
    """
    currency_cloud_beneficiary_bunq_to = {"country":"country","payment_type":"payment_type","all_field":["all_field","all_field"],"name":"name","currency":"currency","legal_entity_type":"legal_entity_type"}

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
    #    "/currency-cloud-beneficiary",
    #    headers=headers,
    #    json=currency_cloud_beneficiary_bunq_to,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_currency_cloud_beneficiary_for_admin_monetary_account(client: TestClient):
    """Test case for c_reate_currency_cloud_beneficiary_for_admin_monetary_account

    
    """
    currency_cloud_beneficiary_retool = {"country":"country","payment_type":"payment_type","all_field":["all_field","all_field"],"name":"name","currency":"currency","legal_entity_type":"legal_entity_type"}

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
    #    "/admin-monetary-account/{admin-monetary-accountID}/currency-cloud-beneficiary".format(admin-monetary-accountID=56),
    #    headers=headers,
    #    json=currency_cloud_beneficiary_retool,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_currency_cloud_beneficiary_for_user(client: TestClient):
    """Test case for c_reate_currency_cloud_beneficiary_for_user

    
    """
    currency_cloud_beneficiary = {"country":"country","payment_type":"payment_type","all_field":["all_field","all_field"],"name":"name","currency":"currency","legal_entity_type":"legal_entity_type"}

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
    #    "/user/{userID}/currency-cloud-beneficiary".format(userID=56),
    #    headers=headers,
    #    json=currency_cloud_beneficiary,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_currency_cloud_beneficiary_for_user(client: TestClient):
    """Test case for list_all_currency_cloud_beneficiary_for_user

    
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
    #    "/user/{userID}/currency-cloud-beneficiary".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_currency_cloud_beneficiary_for_user(client: TestClient):
    """Test case for r_ead_currency_cloud_beneficiary_for_user

    
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
    #    "/user/{userID}/currency-cloud-beneficiary/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

