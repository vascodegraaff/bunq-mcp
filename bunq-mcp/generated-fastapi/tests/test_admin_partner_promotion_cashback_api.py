# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_partner_promotion_cashback import AdminPartnerPromotionCashback  # noqa: F401
from openapi_server.models.admin_partner_promotion_cashback_create import AdminPartnerPromotionCashbackCreate  # noqa: F401
from openapi_server.models.admin_partner_promotion_cashback_listing import AdminPartnerPromotionCashbackListing  # noqa: F401
from openapi_server.models.admin_partner_promotion_cashback_read import AdminPartnerPromotionCashbackRead  # noqa: F401
from openapi_server.models.admin_partner_promotion_cashback_update import AdminPartnerPromotionCashbackUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_partner_promotion_cashback(client: TestClient):
    """Test case for c_reate_admin_partner_promotion_cashback

    
    """
    admin_partner_promotion_cashback = {"time_start":"time_start","partner_name":"partner_name","promotion_code":"promotion_code","deeplink":"deeplink","description":["description","description"],"title_long":["title_long","title_long"],"number_of_transaction_maximum":0,"title":["title","title"],"avatar_uuid":"avatar_uuid","amount_cashback_per_transaction_maximum":{"currency":"currency","value":"value"},"amount_transaction_minimum":{"currency":"currency","value":"value"},"currency":"currency","time_end":"time_end","all_partner_identifier":["all_partner_identifier","all_partner_identifier"],"url_learn_more":"url_learn_more","description_internal":"description_internal","status":"status"}

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
    #    "/admin-partner-promotion-cashback",
    #    headers=headers,
    #    json=admin_partner_promotion_cashback,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_partner_promotion_cashback(client: TestClient):
    """Test case for list_all_admin_partner_promotion_cashback

    
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
    #    "/admin-partner-promotion-cashback",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_partner_promotion_cashback(client: TestClient):
    """Test case for r_ead_admin_partner_promotion_cashback

    
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
    #    "/admin-partner-promotion-cashback/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_partner_promotion_cashback(client: TestClient):
    """Test case for u_pdate_admin_partner_promotion_cashback

    
    """
    admin_partner_promotion_cashback = {"time_start":"time_start","partner_name":"partner_name","promotion_code":"promotion_code","deeplink":"deeplink","description":["description","description"],"title_long":["title_long","title_long"],"number_of_transaction_maximum":0,"title":["title","title"],"avatar_uuid":"avatar_uuid","amount_cashback_per_transaction_maximum":{"currency":"currency","value":"value"},"amount_transaction_minimum":{"currency":"currency","value":"value"},"currency":"currency","time_end":"time_end","all_partner_identifier":["all_partner_identifier","all_partner_identifier"],"url_learn_more":"url_learn_more","description_internal":"description_internal","status":"status"}

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
    #    "/admin-partner-promotion-cashback/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_partner_promotion_cashback,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

