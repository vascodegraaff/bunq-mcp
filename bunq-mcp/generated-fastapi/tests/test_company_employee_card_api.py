# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.company_employee_card import CompanyEmployeeCard  # noqa: F401
from openapi_server.models.company_employee_card_create import CompanyEmployeeCardCreate  # noqa: F401
from openapi_server.models.company_employee_card_read import CompanyEmployeeCardRead  # noqa: F401
from openapi_server.models.company_employee_card_update import CompanyEmployeeCardUpdate  # noqa: F401


def test_c_reate_company_employee_card_for_user(client: TestClient):
    """Test case for c_reate_company_employee_card_for_user

    
    """
    company_employee_card = {"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"}

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
    #    "/user/{userID}/company-employee-card".format(userID=56),
    #    headers=headers,
    #    json=company_employee_card,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_company_employee_card_for_user(client: TestClient):
    """Test case for r_ead_company_employee_card_for_user

    
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
    #    "/user/{userID}/company-employee-card/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_company_employee_card_for_user(client: TestClient):
    """Test case for u_pdate_company_employee_card_for_user

    
    """
    company_employee_card = {"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"}

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
    #    "/user/{userID}/company-employee-card/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=company_employee_card,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

