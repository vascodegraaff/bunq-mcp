# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.token_customer_service import TokenCustomerService  # noqa: F401
from openapi_server.models.token_customer_service_listing import TokenCustomerServiceListing  # noqa: F401
from openapi_server.models.token_customer_service_read import TokenCustomerServiceRead  # noqa: F401
from openapi_server.models.token_customer_service_update import TokenCustomerServiceUpdate  # noqa: F401
from openapi_server.models.token_customer_service_user import TokenCustomerServiceUser  # noqa: F401
from openapi_server.models.token_customer_service_user_create import TokenCustomerServiceUserCreate  # noqa: F401
from openapi_server.models.token_customer_service_user_listing import TokenCustomerServiceUserListing  # noqa: F401


def test_c_reate_token_customer_service_for_user(client: TestClient):
    """Test case for c_reate_token_customer_service_for_user

    
    """
    token_customer_service_user = {"token_unique_reference":"token_unique_reference","status":"status"}

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
    #    "/user/{userID}/token-customer-service".format(userID=56),
    #    headers=headers,
    #    json=token_customer_service_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_token_customer_service_for_user(client: TestClient):
    """Test case for list_all_token_customer_service_for_user

    
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
    #    "/user/{userID}/token-customer-service".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_token_customer_service_for_user_card(client: TestClient):
    """Test case for list_all_token_customer_service_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/token-customer-service".format(userID=56, cardID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_token_customer_service_for_user_card(client: TestClient):
    """Test case for r_ead_token_customer_service_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/token-customer-service/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_token_customer_service_for_user_card(client: TestClient):
    """Test case for u_pdate_token_customer_service_for_user_card

    
    """
    token_customer_service = {"status":"status"}

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
    #    "/user/{userID}/card/{cardID}/token-customer-service/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #    json=token_customer_service,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

