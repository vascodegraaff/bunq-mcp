# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.company_person_ubo import CompanyPersonUbo  # noqa: F401
from openapi_server.models.company_person_ubo_create import CompanyPersonUboCreate  # noqa: F401
from openapi_server.models.company_person_ubo_listing import CompanyPersonUboListing  # noqa: F401
from openapi_server.models.company_person_ubo_read import CompanyPersonUboRead  # noqa: F401


def test_c_reate_company_person_ubo_for_user_company(client: TestClient):
    """Test case for c_reate_company_person_ubo_for_user_company

    
    """
    company_person_ubo = {"document_number":"document_number","date_of_birth":"date_of_birth","document_back_attachment_id":6,"last_name":"last_name","middle_name":"middle_name","tax_resident":[{"country":"country","tax_number":"tax_number","id":0,"status":"status"},{"country":"country","tax_number":"tax_number","id":0,"status":"status"}],"remove_old_ubos":1,"document_front_attachment_id":0,"user_person_id":1,"nationality":"nationality","document_country_of_issuance":"document_country_of_issuance","pointer_director":{"service":"service","name":"name","type":"type","value":"value"},"first_name":"first_name","document_type":"document_type","status":"status","is_company_director":1}

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
    #    "/user-company/{user-companyID}/company-person-ubo".format(user-companyID=56),
    #    headers=headers,
    #    json=company_person_ubo,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_company_person_ubo_for_user_company(client: TestClient):
    """Test case for d_elete_company_person_ubo_for_user_company

    
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
    #    "/user-company/{user-companyID}/company-person-ubo/{itemId}".format(user-companyID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_company_person_ubo_for_user_company(client: TestClient):
    """Test case for list_all_company_person_ubo_for_user_company

    
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
    #    "/user-company/{user-companyID}/company-person-ubo".format(user-companyID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_company_person_ubo_for_user_company(client: TestClient):
    """Test case for r_ead_company_person_ubo_for_user_company

    
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
    #    "/user-company/{user-companyID}/company-person-ubo/{itemId}".format(user-companyID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

