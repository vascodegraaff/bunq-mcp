# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.monetary_account_bank import MonetaryAccountBank  # noqa: F401
from openapi_server.models.monetary_account_bank_create import MonetaryAccountBankCreate  # noqa: F401
from openapi_server.models.monetary_account_bank_listing import MonetaryAccountBankListing  # noqa: F401
from openapi_server.models.monetary_account_bank_read import MonetaryAccountBankRead  # noqa: F401
from openapi_server.models.monetary_account_bank_update import MonetaryAccountBankUpdate  # noqa: F401


def test_c_reate_monetary_account_bank_for_user(client: TestClient):
    """Test case for c_reate_monetary_account_bank_for_user

    
    """
    monetary_account_bank = {"reason":"reason","sub_status":"sub_status","overdraft_limit":{"currency":"currency","value":"value"},"country_iban":"country_iban","created":"created","description":"description","monetary_account_profile":{"profile_drain":{"balance_threshold_high":{"currency":"currency","value":"value"},"savings_account_alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"balance_preferred":{"currency":"currency","value":"value"},"status":"status"},"profile_fill":{"balance_threshold_low":{"currency":"currency","value":"value"},"balance_preferred":{"currency":"currency","value":"value"},"issuer":{"name":"name","bic":"bic"},"status":"status"}},"reason_description":"reason_description","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","avatar_uuid":"avatar_uuid","setting":{"color":"color","sdd_expiration_action":"sdd_expiration_action","icon":"icon","default_avatar_status":"default_avatar_status","restriction_chat":"restriction_chat"},"public_uuid":"public_uuid","balance":{"currency":"currency","value":"value"},"all_auto_save_id":[{"id":0},{"id":0}],"user_id":6,"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"currency":"currency","id":0,"updated":"updated","daily_limit":{"currency":"currency","value":"value"},"status":"status"}

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
    #    "/user/{userID}/monetary-account-bank".format(userID=56),
    #    headers=headers,
    #    json=monetary_account_bank,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_monetary_account_bank_for_user(client: TestClient):
    """Test case for list_all_monetary_account_bank_for_user

    
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
    #    "/user/{userID}/monetary-account-bank".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_monetary_account_bank_for_user(client: TestClient):
    """Test case for r_ead_monetary_account_bank_for_user

    
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
    #    "/user/{userID}/monetary-account-bank/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_monetary_account_bank_for_user(client: TestClient):
    """Test case for u_pdate_monetary_account_bank_for_user

    
    """
    monetary_account_bank = {"reason":"reason","sub_status":"sub_status","overdraft_limit":{"currency":"currency","value":"value"},"country_iban":"country_iban","created":"created","description":"description","monetary_account_profile":{"profile_drain":{"balance_threshold_high":{"currency":"currency","value":"value"},"savings_account_alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"balance_preferred":{"currency":"currency","value":"value"},"status":"status"},"profile_fill":{"balance_threshold_low":{"currency":"currency","value":"value"},"balance_preferred":{"currency":"currency","value":"value"},"issuer":{"name":"name","bic":"bic"},"status":"status"}},"reason_description":"reason_description","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","avatar_uuid":"avatar_uuid","setting":{"color":"color","sdd_expiration_action":"sdd_expiration_action","icon":"icon","default_avatar_status":"default_avatar_status","restriction_chat":"restriction_chat"},"public_uuid":"public_uuid","balance":{"currency":"currency","value":"value"},"all_auto_save_id":[{"id":0},{"id":0}],"user_id":6,"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"currency":"currency","id":0,"updated":"updated","daily_limit":{"currency":"currency","value":"value"},"status":"status"}

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
    #    "/user/{userID}/monetary-account-bank/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=monetary_account_bank,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

