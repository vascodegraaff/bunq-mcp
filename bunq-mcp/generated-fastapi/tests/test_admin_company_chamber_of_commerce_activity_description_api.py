# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_company_chamber_of_commerce_activity_description import AdminCompanyChamberOfCommerceActivityDescription  # noqa: F401
from openapi_server.models.admin_company_chamber_of_commerce_activity_description_create import AdminCompanyChamberOfCommerceActivityDescriptionCreate  # noqa: F401
from openapi_server.models.admin_company_chamber_of_commerce_activity_description_listing import AdminCompanyChamberOfCommerceActivityDescriptionListing  # noqa: F401
from openapi_server.models.admin_company_chamber_of_commerce_activity_description_update import AdminCompanyChamberOfCommerceActivityDescriptionUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_company_chamber_of_commerce_activity_description(client: TestClient):
    """Test case for c_reate_admin_company_chamber_of_commerce_activity_description

    
    """
    admin_company_chamber_of_commerce_activity_description = {"code":"code","description":"description","risk":"risk"}

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
    #    "/admin-company-chamber-of-commerce-activity-description",
    #    headers=headers,
    #    json=admin_company_chamber_of_commerce_activity_description,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_company_chamber_of_commerce_activity_description(client: TestClient):
    """Test case for list_all_admin_company_chamber_of_commerce_activity_description

    
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
    #    "/admin-company-chamber-of-commerce-activity-description",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_company_chamber_of_commerce_activity_description(client: TestClient):
    """Test case for u_pdate_admin_company_chamber_of_commerce_activity_description

    
    """
    admin_company_chamber_of_commerce_activity_description = {"code":"code","description":"description","risk":"risk"}

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
    #    "/admin-company-chamber-of-commerce-activity-description/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_company_chamber_of_commerce_activity_description,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

