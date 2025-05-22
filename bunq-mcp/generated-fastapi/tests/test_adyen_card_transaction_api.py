# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.adyen_card_transaction import AdyenCardTransaction  # noqa: F401
from openapi_server.models.adyen_card_transaction_create import AdyenCardTransactionCreate  # noqa: F401
from openapi_server.models.adyen_card_transaction_listing import AdyenCardTransactionListing  # noqa: F401
from openapi_server.models.adyen_card_transaction_read import AdyenCardTransactionRead  # noqa: F401
from openapi_server.models.adyen_card_transaction_update import AdyenCardTransactionUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_adyen_card_transaction_for_user_monetary_account_adyen_store(client: TestClient):
    """Test case for c_reate_adyen_card_transaction_for_user_monetary_account_adyen_store

    
    """
    adyen_card_transaction = {"amount":{"currency":"currency","value":"value"},"status_description":"status_description","status_together_url":"status_together_url","monetary_account_id":0,"adyen_store_id":6,"card_pan_masked":"card_pan_masked","label_monetary_account":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"reference_customer":"reference_customer","card_brand":"card_brand","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"status_description_translated":"status_description_translated","label_user_creator":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"terminal_id":"terminal_id","receipt_attachment":{"monetary_account_id":3,"id":9},"status":"status","request_payment_create":"request_payment_create"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-store/{adyen-storeID}/adyen-card-transaction".format(userID=56, monetary-accountID=56, adyen-storeID=56),
    #    headers=headers,
    #    json=adyen_card_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_adyen_card_transaction_for_user_monetary_account_adyen_store(client: TestClient):
    """Test case for list_all_adyen_card_transaction_for_user_monetary_account_adyen_store

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-store/{adyen-storeID}/adyen-card-transaction".format(userID=56, monetary-accountID=56, adyen-storeID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_adyen_card_transaction_for_user_monetary_account_adyen_store(client: TestClient):
    """Test case for r_ead_adyen_card_transaction_for_user_monetary_account_adyen_store

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-store/{adyen-storeID}/adyen-card-transaction/{itemId}".format(userID=56, monetary-accountID=56, adyen-storeID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_adyen_card_transaction_for_user_monetary_account_adyen_store(client: TestClient):
    """Test case for u_pdate_adyen_card_transaction_for_user_monetary_account_adyen_store

    
    """
    adyen_card_transaction = {"amount":{"currency":"currency","value":"value"},"status_description":"status_description","status_together_url":"status_together_url","monetary_account_id":0,"adyen_store_id":6,"card_pan_masked":"card_pan_masked","label_monetary_account":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"reference_customer":"reference_customer","card_brand":"card_brand","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"status_description_translated":"status_description_translated","label_user_creator":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"terminal_id":"terminal_id","receipt_attachment":{"monetary_account_id":3,"id":9},"status":"status","request_payment_create":"request_payment_create"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-store/{adyen-storeID}/adyen-card-transaction/{itemId}".format(userID=56, monetary-accountID=56, adyen-storeID=56, itemId=56),
    #    headers=headers,
    #    json=adyen_card_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

