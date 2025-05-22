# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_partner_promotion_category import AdminPartnerPromotionCategory  # noqa: F401
from openapi_server.models.admin_partner_promotion_category_create import AdminPartnerPromotionCategoryCreate  # noqa: F401
from openapi_server.models.admin_partner_promotion_category_listing import AdminPartnerPromotionCategoryListing  # noqa: F401
from openapi_server.models.admin_partner_promotion_category_read import AdminPartnerPromotionCategoryRead  # noqa: F401
from openapi_server.models.admin_partner_promotion_category_update import AdminPartnerPromotionCategoryUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_partner_promotion_category(client: TestClient):
    """Test case for c_reate_admin_partner_promotion_category

    
    """
    admin_partner_promotion_category = {"emoji":"emoji","title":["title","title"],"status":"status"}

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
    #    "/admin-partner-promotion-category",
    #    headers=headers,
    #    json=admin_partner_promotion_category,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_partner_promotion_category(client: TestClient):
    """Test case for list_all_admin_partner_promotion_category

    
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
    #    "/admin-partner-promotion-category",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_partner_promotion_category(client: TestClient):
    """Test case for r_ead_admin_partner_promotion_category

    
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
    #    "/admin-partner-promotion-category/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_partner_promotion_category(client: TestClient):
    """Test case for u_pdate_admin_partner_promotion_category

    
    """
    admin_partner_promotion_category = {"emoji":"emoji","title":["title","title"],"status":"status"}

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
    #    "/admin-partner-promotion-category/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_partner_promotion_category,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

