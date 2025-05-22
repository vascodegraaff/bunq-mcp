# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.partner_promotion_cashback_listing import PartnerPromotionCashbackListing  # noqa: F401
from openapi_server.models.user_partner_promotion_cashback import UserPartnerPromotionCashback  # noqa: F401
from openapi_server.models.user_partner_promotion_cashback_create import UserPartnerPromotionCashbackCreate  # noqa: F401
from openapi_server.models.user_partner_promotion_cashback_listing import UserPartnerPromotionCashbackListing  # noqa: F401


def test_c_reate_partner_promotion_cashback_for_user(client: TestClient):
    """Test case for c_reate_partner_promotion_cashback_for_user

    
    """
    user_partner_promotion_cashback = {"promotion_code":"promotion_code","number_of_transaction_remaining":8,"status":"status","partner_promotion":{"promotion_code":"promotion_code","partner_name":"partner_name","url_together":"url_together","deeplink":"deeplink","number_of_transaction_maximum":4,"promotion_title_short":["promotion_title_short","promotion_title_short"],"promotion_title_long":["promotion_title_long","promotion_title_long"],"public_uuid":"public_uuid","partner_avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"promotion_description":["promotion_description","promotion_description"],"amount_cashback_per_transaction_maximum":{"currency":"currency","value":"value"},"amount_transaction_minimum":{"currency":"currency","value":"value"},"status":"status"}}

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
    #    "/user/{userID}/partner-promotion-cashback".format(userID=56),
    #    headers=headers,
    #    json=user_partner_promotion_cashback,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_partner_promotion_cashback(client: TestClient):
    """Test case for list_all_partner_promotion_cashback

    
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
    #    "/partner-promotion-cashback",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_partner_promotion_cashback_for_user(client: TestClient):
    """Test case for list_all_partner_promotion_cashback_for_user

    
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
    #    "/user/{userID}/partner-promotion-cashback".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

