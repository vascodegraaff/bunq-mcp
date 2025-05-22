# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.adyen_card_transaction_refund import AdyenCardTransactionRefund  # noqa: F401
from openapi_server.models.adyen_card_transaction_refund_create import AdyenCardTransactionRefundCreate  # noqa: F401
from openapi_server.models.adyen_card_transaction_refund_listing import AdyenCardTransactionRefundListing  # noqa: F401
from openapi_server.models.adyen_card_transaction_refund_read import AdyenCardTransactionRefundRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_action_refund import MasterCardActionRefund  # noqa: F401
from openapi_server.models.master_card_action_refund_create import MasterCardActionRefundCreate  # noqa: F401
from openapi_server.models.master_card_action_refund_listing import MasterCardActionRefundListing  # noqa: F401
from openapi_server.models.master_card_action_refund_read import MasterCardActionRefundRead  # noqa: F401
from openapi_server.models.master_card_action_refund_update import MasterCardActionRefundUpdate  # noqa: F401


def test_c_reate_refund_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for c_reate_refund_for_user_monetary_account_adyen_card_transaction

    
    """
    adyen_card_transaction_refund = {"amount":{"currency":"currency","value":"value"}}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/refund".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56),
    #    headers=headers,
    #    json=adyen_card_transaction_refund,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_refund_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for c_reate_refund_for_user_monetary_account_mastercard_action

    
    """
    master_card_action_refund = {"reason":"reason","amount":{"currency":"currency","value":"value"},"status_description":"status_description","status_together_url":"status_together_url","created":"created","description":"description","type":"type","reference_mastercard_action_event":[{"event_id":0},{"event_id":0}],"terms_and_conditions":"terms_and_conditions","additional_information":{"terms_and_conditions":"terms_and_conditions","reason":"reason","attachment":[{"id":5},{"id":5}],"comment":"comment","category":"category"},"attachment":[{"id":5},{"id":5}],"sub_type":"sub_type","counterparty_alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"time_refund":"time_refund","alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"status_description_translated":"status_description_translated","comment":"comment","id":7,"category":"category","updated":"updated","label_user_creator":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"label_card":{"second_line":"second_line","expiry_date":"expiry_date","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"type":"type","uuid":"uuid","status":"status"},"status":"status","mastercard_action_id":3}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/refund".format(userID=56, monetary-accountID=56, mastercard-actionID=56),
    #    headers=headers,
    #    json=master_card_action_refund,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_refund_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for list_all_refund_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/refund".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_refund_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for list_all_refund_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/refund".format(userID=56, monetary-accountID=56, mastercard-actionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_refund_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for r_ead_refund_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/refund/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_refund_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for r_ead_refund_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/refund/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_refund_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for u_pdate_refund_for_user_monetary_account_mastercard_action

    
    """
    master_card_action_refund = {"reason":"reason","amount":{"currency":"currency","value":"value"},"status_description":"status_description","status_together_url":"status_together_url","created":"created","description":"description","type":"type","reference_mastercard_action_event":[{"event_id":0},{"event_id":0}],"terms_and_conditions":"terms_and_conditions","additional_information":{"terms_and_conditions":"terms_and_conditions","reason":"reason","attachment":[{"id":5},{"id":5}],"comment":"comment","category":"category"},"attachment":[{"id":5},{"id":5}],"sub_type":"sub_type","counterparty_alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"time_refund":"time_refund","alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"status_description_translated":"status_description_translated","comment":"comment","id":7,"category":"category","updated":"updated","label_user_creator":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"label_card":{"second_line":"second_line","expiry_date":"expiry_date","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"type":"type","uuid":"uuid","status":"status"},"status":"status","mastercard_action_id":3}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/refund/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #    json=master_card_action_refund,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

