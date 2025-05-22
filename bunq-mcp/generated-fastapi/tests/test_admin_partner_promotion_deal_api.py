# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_partner_promotion_deal import AdminPartnerPromotionDeal  # noqa: F401
from openapi_server.models.admin_partner_promotion_deal_create import AdminPartnerPromotionDealCreate  # noqa: F401
from openapi_server.models.admin_partner_promotion_deal_listing import AdminPartnerPromotionDealListing  # noqa: F401
from openapi_server.models.admin_partner_promotion_deal_read import AdminPartnerPromotionDealRead  # noqa: F401
from openapi_server.models.admin_partner_promotion_deal_update import AdminPartnerPromotionDealUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_partner_promotion_deal(client: TestClient):
    """Test case for c_reate_admin_partner_promotion_deal

    
    """
    admin_partner_promotion_deal = {"time_start":"time_start","partner_name":"partner_name","description":["description","description"],"title_long":["title_long","title_long"],"url_terms_and_conditions":"url_terms_and_conditions","title":["title","title"],"all_category_id":["all_category_id","all_category_id"],"avatar_uuid":"avatar_uuid","all_country_restricted":["all_country_restricted","all_country_restricted"],"terms_and_conditions_text":["terms_and_conditions_text","terms_and_conditions_text"],"all_tag":["all_tag","all_tag"],"time_end":"time_end","monitoring_limit":6,"description_internal":"description_internal","deeplink":"deeplink","background_uuid":"background_uuid","footer_text":["footer_text","footer_text"],"priority":0,"learn_more_text":["learn_more_text","learn_more_text"],"identifier_deeplink_internal":"identifier_deeplink_internal","voucher_type":"voucher_type","button_text":["button_text","button_text"],"url_learn_more":"url_learn_more","all_user_life_stage_restricted":["all_user_life_stage_restricted","all_user_life_stage_restricted"],"status":"status"}

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
    #    "/admin-partner-promotion-deal",
    #    headers=headers,
    #    json=admin_partner_promotion_deal,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_partner_promotion_deal(client: TestClient):
    """Test case for list_all_admin_partner_promotion_deal

    
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
    #    "/admin-partner-promotion-deal",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_partner_promotion_deal(client: TestClient):
    """Test case for r_ead_admin_partner_promotion_deal

    
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
    #    "/admin-partner-promotion-deal/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_partner_promotion_deal(client: TestClient):
    """Test case for u_pdate_admin_partner_promotion_deal

    
    """
    admin_partner_promotion_deal = {"time_start":"time_start","partner_name":"partner_name","description":["description","description"],"title_long":["title_long","title_long"],"url_terms_and_conditions":"url_terms_and_conditions","title":["title","title"],"all_category_id":["all_category_id","all_category_id"],"avatar_uuid":"avatar_uuid","all_country_restricted":["all_country_restricted","all_country_restricted"],"terms_and_conditions_text":["terms_and_conditions_text","terms_and_conditions_text"],"all_tag":["all_tag","all_tag"],"time_end":"time_end","monitoring_limit":6,"description_internal":"description_internal","deeplink":"deeplink","background_uuid":"background_uuid","footer_text":["footer_text","footer_text"],"priority":0,"learn_more_text":["learn_more_text","learn_more_text"],"identifier_deeplink_internal":"identifier_deeplink_internal","voucher_type":"voucher_type","button_text":["button_text","button_text"],"url_learn_more":"url_learn_more","all_user_life_stage_restricted":["all_user_life_stage_restricted","all_user_life_stage_restricted"],"status":"status"}

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
    #    "/admin-partner-promotion-deal/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_partner_promotion_deal,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

