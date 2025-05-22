# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.birdee_customer_financial_situation import BirdeeCustomerFinancialSituation  # noqa: F401
from openapi_server.models.birdee_customer_financial_situation_create import BirdeeCustomerFinancialSituationCreate  # noqa: F401
from openapi_server.models.birdee_customer_financial_situation_listing import BirdeeCustomerFinancialSituationListing  # noqa: F401
from openapi_server.models.birdee_customer_financial_situation_read import BirdeeCustomerFinancialSituationRead  # noqa: F401
from openapi_server.models.birdee_customer_financial_situation_update import BirdeeCustomerFinancialSituationUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_financial_situation_for_user_birdee_customer(client: TestClient):
    """Test case for c_reate_financial_situation_for_user_birdee_customer

    
    """
    birdee_customer_financial_situation = {"amount_patrimony_total":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"patrimony_origin":"patrimony_origin","amount_income_monthly":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"patrimony_distribution":{"security":"security","other":"other","life_insurance":"life_insurance","real_estate":"real_estate"}}

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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/financial-situation".format(userID=56, birdee-customerID=56),
    #    headers=headers,
    #    json=birdee_customer_financial_situation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_financial_situation_for_user_birdee_customer(client: TestClient):
    """Test case for list_all_financial_situation_for_user_birdee_customer

    
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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/financial-situation".format(userID=56, birdee-customerID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_financial_situation_for_user_birdee_customer(client: TestClient):
    """Test case for r_ead_financial_situation_for_user_birdee_customer

    
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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/financial-situation/{itemId}".format(userID=56, birdee-customerID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_financial_situation_for_user_birdee_customer(client: TestClient):
    """Test case for u_pdate_financial_situation_for_user_birdee_customer

    
    """
    birdee_customer_financial_situation = {"amount_patrimony_total":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"patrimony_origin":"patrimony_origin","amount_income_monthly":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"patrimony_distribution":{"security":"security","other":"other","life_insurance":"life_insurance","real_estate":"real_estate"}}

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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/financial-situation/{itemId}".format(userID=56, birdee-customerID=56, itemId=56),
    #    headers=headers,
    #    json=birdee_customer_financial_situation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

