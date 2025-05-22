# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_partner_promotion_detail import AdminPartnerPromotionDetail  # noqa: F401
from openapi_server.models.admin_partner_promotion_detail_create import AdminPartnerPromotionDetailCreate  # noqa: F401
from openapi_server.models.admin_partner_promotion_detail_listing import AdminPartnerPromotionDetailListing  # noqa: F401
from openapi_server.models.admin_partner_promotion_detail_read import AdminPartnerPromotionDetailRead  # noqa: F401
from openapi_server.models.admin_partner_promotion_detail_update import AdminPartnerPromotionDetailUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_partner_promotion_detail_for_admin_partner_promotion_deal(client: TestClient):
    """Test case for c_reate_admin_partner_promotion_detail_for_admin_partner_promotion_deal

    
    """
    admin_partner_promotion_detail = {"description":["description","description"],"title":["title","title"],"avatar_uuid":"avatar_uuid","order":0}

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
    #    "/admin-partner-promotion-deal/{admin-partner-promotion-dealID}/admin-partner-promotion-detail".format(admin-partner-promotion-dealID=56),
    #    headers=headers,
    #    json=admin_partner_promotion_detail,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_admin_partner_promotion_detail_for_admin_partner_promotion_deal(client: TestClient):
    """Test case for d_elete_admin_partner_promotion_detail_for_admin_partner_promotion_deal

    
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
    #    "/admin-partner-promotion-deal/{admin-partner-promotion-dealID}/admin-partner-promotion-detail/{itemId}".format(admin-partner-promotion-dealID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_partner_promotion_detail_for_admin_partner_promotion_deal(client: TestClient):
    """Test case for list_all_admin_partner_promotion_detail_for_admin_partner_promotion_deal

    
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
    #    "/admin-partner-promotion-deal/{admin-partner-promotion-dealID}/admin-partner-promotion-detail".format(admin-partner-promotion-dealID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_partner_promotion_detail_for_admin_partner_promotion_deal(client: TestClient):
    """Test case for r_ead_admin_partner_promotion_detail_for_admin_partner_promotion_deal

    
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
    #    "/admin-partner-promotion-deal/{admin-partner-promotion-dealID}/admin-partner-promotion-detail/{itemId}".format(admin-partner-promotion-dealID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_partner_promotion_detail_for_admin_partner_promotion_deal(client: TestClient):
    """Test case for u_pdate_admin_partner_promotion_detail_for_admin_partner_promotion_deal

    
    """
    admin_partner_promotion_detail = {"description":["description","description"],"title":["title","title"],"avatar_uuid":"avatar_uuid","order":0}

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
    #    "/admin-partner-promotion-deal/{admin-partner-promotion-dealID}/admin-partner-promotion-detail/{itemId}".format(admin-partner-promotion-dealID=56, itemId=56),
    #    headers=headers,
    #    json=admin_partner_promotion_detail,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

