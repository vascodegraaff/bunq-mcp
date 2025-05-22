# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_partner_promotion_prize import AdminPartnerPromotionPrize  # noqa: F401
from openapi_server.models.admin_partner_promotion_prize_create import AdminPartnerPromotionPrizeCreate  # noqa: F401
from openapi_server.models.admin_partner_promotion_prize_listing import AdminPartnerPromotionPrizeListing  # noqa: F401
from openapi_server.models.admin_partner_promotion_prize_read import AdminPartnerPromotionPrizeRead  # noqa: F401
from openapi_server.models.admin_partner_promotion_prize_update import AdminPartnerPromotionPrizeUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_partner_promotion_prize(client: TestClient):
    """Test case for c_reate_admin_partner_promotion_prize

    
    """
    admin_partner_promotion_prize = {"number_of_point":6,"time_start":"time_start","partner_name":"partner_name","description":["description","description"],"background_uuid":"background_uuid","title_long":["title_long","title_long"],"title":["title","title"],"priority":0,"avatar_uuid":"avatar_uuid","all_country_restricted":["all_country_restricted","all_country_restricted"],"learn_more_text":["learn_more_text","learn_more_text"],"identifier_deeplink_internal":"identifier_deeplink_internal","description_claimed":["description_claimed","description_claimed"],"all_tag":["all_tag","all_tag"],"time_end":"time_end","button_text":["button_text","button_text"],"category":"category","deeplink_external":"deeplink_external","url_learn_more":"url_learn_more","monitoring_limit":1,"description_internal":"description_internal","status":"status"}

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
    #    "/admin-partner-promotion-prize",
    #    headers=headers,
    #    json=admin_partner_promotion_prize,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_partner_promotion_prize(client: TestClient):
    """Test case for list_all_admin_partner_promotion_prize

    
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
    #    "/admin-partner-promotion-prize",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_partner_promotion_prize(client: TestClient):
    """Test case for r_ead_admin_partner_promotion_prize

    
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
    #    "/admin-partner-promotion-prize/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_partner_promotion_prize(client: TestClient):
    """Test case for u_pdate_admin_partner_promotion_prize

    
    """
    admin_partner_promotion_prize = {"number_of_point":6,"time_start":"time_start","partner_name":"partner_name","description":["description","description"],"background_uuid":"background_uuid","title_long":["title_long","title_long"],"title":["title","title"],"priority":0,"avatar_uuid":"avatar_uuid","all_country_restricted":["all_country_restricted","all_country_restricted"],"learn_more_text":["learn_more_text","learn_more_text"],"identifier_deeplink_internal":"identifier_deeplink_internal","description_claimed":["description_claimed","description_claimed"],"all_tag":["all_tag","all_tag"],"time_end":"time_end","button_text":["button_text","button_text"],"category":"category","deeplink_external":"deeplink_external","url_learn_more":"url_learn_more","monitoring_limit":1,"description_internal":"description_internal","status":"status"}

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
    #    "/admin-partner-promotion-prize/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_partner_promotion_prize,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

