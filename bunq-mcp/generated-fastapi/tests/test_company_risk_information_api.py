# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.company_risk_information import CompanyRiskInformation  # noqa: F401
from openapi_server.models.company_risk_information_create import CompanyRiskInformationCreate  # noqa: F401
from openapi_server.models.company_risk_information_listing import CompanyRiskInformationListing  # noqa: F401
from openapi_server.models.company_risk_information_read import CompanyRiskInformationRead  # noqa: F401
from openapi_server.models.company_risk_information_update import CompanyRiskInformationUpdate  # noqa: F401


def test_c_reate_company_risk_information_for_user_company(client: TestClient):
    """Test case for c_reate_company_risk_information_for_user_company

    
    """
    company_risk_information = {"company_chamber_of_commerce_activity_description_ids":["company_chamber_of_commerce_activity_description_ids","company_chamber_of_commerce_activity_description_ids"],"volume_transaction_monthly":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"volume_transaction_monthly_maximum":{"currency":"currency","value":"value"},"activities":[{"description":"description","value":"value"},{"description":"description","value":"value"}],"passive_income_types":["passive_income_types","passive_income_types"],"volume_transaction_monthly_minimum":{"currency":"currency","value":"value"}}

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
    #    "/user-company/{user-companyID}/company-risk-information".format(user-companyID=56),
    #    headers=headers,
    #    json=company_risk_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_company_risk_information_for_user_company(client: TestClient):
    """Test case for list_all_company_risk_information_for_user_company

    
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
    #    "/user-company/{user-companyID}/company-risk-information".format(user-companyID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_company_risk_information_for_user_company(client: TestClient):
    """Test case for r_ead_company_risk_information_for_user_company

    
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
    #    "/user-company/{user-companyID}/company-risk-information/{itemId}".format(user-companyID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_company_risk_information_for_user_company(client: TestClient):
    """Test case for u_pdate_company_risk_information_for_user_company

    
    """
    company_risk_information = {"company_chamber_of_commerce_activity_description_ids":["company_chamber_of_commerce_activity_description_ids","company_chamber_of_commerce_activity_description_ids"],"volume_transaction_monthly":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"volume_transaction_monthly_maximum":{"currency":"currency","value":"value"},"activities":[{"description":"description","value":"value"},{"description":"description","value":"value"}],"passive_income_types":["passive_income_types","passive_income_types"],"volume_transaction_monthly_minimum":{"currency":"currency","value":"value"}}

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
    #    "/user-company/{user-companyID}/company-risk-information/{itemId}".format(user-companyID=56, itemId=56),
    #    headers=headers,
    #    json=company_risk_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

