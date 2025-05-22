# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.company_employee_card_limit import CompanyEmployeeCardLimit  # noqa: F401
from openapi_server.models.company_employee_card_limit_read import CompanyEmployeeCardLimitRead  # noqa: F401
from openapi_server.models.company_employee_card_limit_update import CompanyEmployeeCardLimitUpdate  # noqa: F401


def test_r_ead_company_employee_card_limit_for_user(client: TestClient):
    """Test case for r_ead_company_employee_card_limit_for_user

    
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
    #    "/user/{userID}/company-employee-card-limit/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_company_employee_card_limit_for_user(client: TestClient):
    """Test case for u_pdate_company_employee_card_limit_for_user

    
    """
    company_employee_card_limit = {"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8}

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
    #    "/user/{userID}/company-employee-card-limit/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=company_employee_card_limit,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

