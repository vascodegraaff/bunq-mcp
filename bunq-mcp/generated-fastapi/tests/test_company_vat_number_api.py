# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.tax_resident_company import TaxResidentCompany  # noqa: F401
from openapi_server.models.tax_resident_company_create import TaxResidentCompanyCreate  # noqa: F401
from openapi_server.models.tax_resident_company_listing import TaxResidentCompanyListing  # noqa: F401


def test_c_reate_company_vat_number_for_user_company(client: TestClient):
    """Test case for c_reate_company_vat_number_for_user_company

    
    """
    tax_resident_company = {"vat_numbers":[{"country":"country","type":"type","value":"value"},{"country":"country","type":"type","value":"value"}]}

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
    #    "/user-company/{user-companyID}/company-vat-number".format(user-companyID=56),
    #    headers=headers,
    #    json=tax_resident_company,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_company_vat_number_for_user_company(client: TestClient):
    """Test case for list_all_company_vat_number_for_user_company

    
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
    #    "/user-company/{user-companyID}/company-vat-number".format(user-companyID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

