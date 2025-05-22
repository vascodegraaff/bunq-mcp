# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.monetary_account_light import MonetaryAccountLight  # noqa: F401
from openapi_server.models.monetary_account_light_create import MonetaryAccountLightCreate  # noqa: F401
from openapi_server.models.monetary_account_light_listing import MonetaryAccountLightListing  # noqa: F401
from openapi_server.models.monetary_account_light_read import MonetaryAccountLightRead  # noqa: F401
from openapi_server.models.monetary_account_light_update import MonetaryAccountLightUpdate  # noqa: F401


def test_c_reate_monetary_account_light_for_user(client: TestClient):
    """Test case for c_reate_monetary_account_light_for_user

    
    """
    monetary_account_light = {"reason":"reason","sub_status":"sub_status","created":"created","budget_month_maximum":{"currency":"currency","value":"value"},"description":"description","reason_description":"reason_description","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"balance_maximum":{"currency":"currency","value":"value"},"avatar_uuid":"avatar_uuid","setting":{"color":"color","sdd_expiration_action":"sdd_expiration_action","icon":"icon","default_avatar_status":"default_avatar_status","restriction_chat":"restriction_chat"},"budget_year_maximum":{"currency":"currency","value":"value"},"public_uuid":"public_uuid","budget_year_used":{"currency":"currency","value":"value"},"balance":{"currency":"currency","value":"value"},"user_id":4,"budget_month_used":{"currency":"currency","value":"value"},"budget_withdrawal_year_maximum":{"currency":"currency","value":"value"},"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"currency":"currency","id":3,"budget_withdrawal_year_used":{"currency":"currency","value":"value"},"updated":"updated","daily_limit":{"currency":"currency","value":"value"},"status":"status"}

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
    #    "/user/{userID}/monetary-account-light".format(userID=56),
    #    headers=headers,
    #    json=monetary_account_light,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_monetary_account_light_for_user(client: TestClient):
    """Test case for list_all_monetary_account_light_for_user

    
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
    #    "/user/{userID}/monetary-account-light".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_monetary_account_light_for_user(client: TestClient):
    """Test case for r_ead_monetary_account_light_for_user

    
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
    #    "/user/{userID}/monetary-account-light/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_monetary_account_light_for_user(client: TestClient):
    """Test case for u_pdate_monetary_account_light_for_user

    
    """
    monetary_account_light = {"reason":"reason","sub_status":"sub_status","created":"created","budget_month_maximum":{"currency":"currency","value":"value"},"description":"description","reason_description":"reason_description","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"balance_maximum":{"currency":"currency","value":"value"},"avatar_uuid":"avatar_uuid","setting":{"color":"color","sdd_expiration_action":"sdd_expiration_action","icon":"icon","default_avatar_status":"default_avatar_status","restriction_chat":"restriction_chat"},"budget_year_maximum":{"currency":"currency","value":"value"},"public_uuid":"public_uuid","budget_year_used":{"currency":"currency","value":"value"},"balance":{"currency":"currency","value":"value"},"user_id":4,"budget_month_used":{"currency":"currency","value":"value"},"budget_withdrawal_year_maximum":{"currency":"currency","value":"value"},"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"currency":"currency","id":3,"budget_withdrawal_year_used":{"currency":"currency","value":"value"},"updated":"updated","daily_limit":{"currency":"currency","value":"value"},"status":"status"}

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
    #    "/user/{userID}/monetary-account-light/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=monetary_account_light,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

