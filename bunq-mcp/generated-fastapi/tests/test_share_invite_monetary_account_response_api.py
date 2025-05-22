# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.share_invite_monetary_account_response import ShareInviteMonetaryAccountResponse  # noqa: F401
from openapi_server.models.share_invite_monetary_account_response_listing import ShareInviteMonetaryAccountResponseListing  # noqa: F401
from openapi_server.models.share_invite_monetary_account_response_read import ShareInviteMonetaryAccountResponseRead  # noqa: F401
from openapi_server.models.share_invite_monetary_account_response_update import ShareInviteMonetaryAccountResponseUpdate  # noqa: F401


def test_list_all_share_invite_monetary_account_response_for_user(client: TestClient):
    """Test case for list_all_share_invite_monetary_account_response_for_user

    
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
    #    "/user/{userID}/share-invite-monetary-account-response".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_share_invite_monetary_account_response_for_user(client: TestClient):
    """Test case for r_ead_share_invite_monetary_account_response_for_user

    
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
    #    "/user/{userID}/share-invite-monetary-account-response/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_share_invite_monetary_account_response_for_user(client: TestClient):
    """Test case for u_pdate_share_invite_monetary_account_response_for_user

    
    """
    share_invite_monetary_account_response = {"end_date":"end_date","share_detail":{"read_only":{"view_balance":1,"view_new_events":1,"view_old_events":1},"payment":{"make_draft_payments":1,"view_balance":1,"view_new_events":1,"make_payments":1,"view_old_events":1},"draft_payment":{"make_draft_payments":1,"view_balance":1,"view_new_events":1,"view_old_events":1}},"access_type":"access_type","created":"created","counter_alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"monetary_account_id":7,"description":"description","card_id":7,"user_alias_cancelled":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"share_type":"share_type","relation_user":{"user_status":"user_status","all_company_employee_card":[{"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"},{"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"}],"user_id":"user_id","counter_user_id":"counter_user_id","counter_label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"company_employee_setting_adyen_card_transaction":{"monetary_account_payout_id":0,"pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"},"relationship":"relationship","counter_user_status":"counter_user_status","status":"status"},"draft_share_invite_bank_id":6,"id":0,"updated":"updated","status":"status","start_date":"start_date"}

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
    #    "/user/{userID}/share-invite-monetary-account-response/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=share_invite_monetary_account_response,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

