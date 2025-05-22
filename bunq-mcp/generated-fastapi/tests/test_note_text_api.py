# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.note_text_adyen_card_transaction import NoteTextAdyenCardTransaction  # noqa: F401
from openapi_server.models.note_text_adyen_card_transaction_create import NoteTextAdyenCardTransactionCreate  # noqa: F401
from openapi_server.models.note_text_adyen_card_transaction_listing import NoteTextAdyenCardTransactionListing  # noqa: F401
from openapi_server.models.note_text_adyen_card_transaction_read import NoteTextAdyenCardTransactionRead  # noqa: F401
from openapi_server.models.note_text_adyen_card_transaction_update import NoteTextAdyenCardTransactionUpdate  # noqa: F401
from openapi_server.models.note_text_bank_switch_service_netherlands_incoming_payment import NoteTextBankSwitchServiceNetherlandsIncomingPayment  # noqa: F401
from openapi_server.models.note_text_bank_switch_service_netherlands_incoming_payment_create import NoteTextBankSwitchServiceNetherlandsIncomingPaymentCreate  # noqa: F401
from openapi_server.models.note_text_bank_switch_service_netherlands_incoming_payment_listing import NoteTextBankSwitchServiceNetherlandsIncomingPaymentListing  # noqa: F401
from openapi_server.models.note_text_bank_switch_service_netherlands_incoming_payment_read import NoteTextBankSwitchServiceNetherlandsIncomingPaymentRead  # noqa: F401
from openapi_server.models.note_text_bank_switch_service_netherlands_incoming_payment_update import NoteTextBankSwitchServiceNetherlandsIncomingPaymentUpdate  # noqa: F401
from openapi_server.models.note_text_bunq_me_fundraiser_result import NoteTextBunqMeFundraiserResult  # noqa: F401
from openapi_server.models.note_text_bunq_me_fundraiser_result_create import NoteTextBunqMeFundraiserResultCreate  # noqa: F401
from openapi_server.models.note_text_bunq_me_fundraiser_result_listing import NoteTextBunqMeFundraiserResultListing  # noqa: F401
from openapi_server.models.note_text_bunq_me_fundraiser_result_read import NoteTextBunqMeFundraiserResultRead  # noqa: F401
from openapi_server.models.note_text_bunq_me_fundraiser_result_update import NoteTextBunqMeFundraiserResultUpdate  # noqa: F401
from openapi_server.models.note_text_draft_payment import NoteTextDraftPayment  # noqa: F401
from openapi_server.models.note_text_draft_payment_create import NoteTextDraftPaymentCreate  # noqa: F401
from openapi_server.models.note_text_draft_payment_listing import NoteTextDraftPaymentListing  # noqa: F401
from openapi_server.models.note_text_draft_payment_read import NoteTextDraftPaymentRead  # noqa: F401
from openapi_server.models.note_text_draft_payment_update import NoteTextDraftPaymentUpdate  # noqa: F401
from openapi_server.models.note_text_ideal_merchant_transaction import NoteTextIdealMerchantTransaction  # noqa: F401
from openapi_server.models.note_text_ideal_merchant_transaction_create import NoteTextIdealMerchantTransactionCreate  # noqa: F401
from openapi_server.models.note_text_ideal_merchant_transaction_listing import NoteTextIdealMerchantTransactionListing  # noqa: F401
from openapi_server.models.note_text_ideal_merchant_transaction_read import NoteTextIdealMerchantTransactionRead  # noqa: F401
from openapi_server.models.note_text_ideal_merchant_transaction_update import NoteTextIdealMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.note_text_listing import NoteTextListing  # noqa: F401
from openapi_server.models.note_text_master_card_action import NoteTextMasterCardAction  # noqa: F401
from openapi_server.models.note_text_master_card_action_create import NoteTextMasterCardActionCreate  # noqa: F401
from openapi_server.models.note_text_master_card_action_listing import NoteTextMasterCardActionListing  # noqa: F401
from openapi_server.models.note_text_master_card_action_read import NoteTextMasterCardActionRead  # noqa: F401
from openapi_server.models.note_text_master_card_action_update import NoteTextMasterCardActionUpdate  # noqa: F401
from openapi_server.models.note_text_open_banking_merchant_transaction import NoteTextOpenBankingMerchantTransaction  # noqa: F401
from openapi_server.models.note_text_open_banking_merchant_transaction_create import NoteTextOpenBankingMerchantTransactionCreate  # noqa: F401
from openapi_server.models.note_text_open_banking_merchant_transaction_listing import NoteTextOpenBankingMerchantTransactionListing  # noqa: F401
from openapi_server.models.note_text_open_banking_merchant_transaction_read import NoteTextOpenBankingMerchantTransactionRead  # noqa: F401
from openapi_server.models.note_text_open_banking_merchant_transaction_update import NoteTextOpenBankingMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.note_text_payment import NoteTextPayment  # noqa: F401
from openapi_server.models.note_text_payment_batch import NoteTextPaymentBatch  # noqa: F401
from openapi_server.models.note_text_payment_batch_create import NoteTextPaymentBatchCreate  # noqa: F401
from openapi_server.models.note_text_payment_batch_listing import NoteTextPaymentBatchListing  # noqa: F401
from openapi_server.models.note_text_payment_batch_read import NoteTextPaymentBatchRead  # noqa: F401
from openapi_server.models.note_text_payment_batch_update import NoteTextPaymentBatchUpdate  # noqa: F401
from openapi_server.models.note_text_payment_create import NoteTextPaymentCreate  # noqa: F401
from openapi_server.models.note_text_payment_delayed import NoteTextPaymentDelayed  # noqa: F401
from openapi_server.models.note_text_payment_delayed_create import NoteTextPaymentDelayedCreate  # noqa: F401
from openapi_server.models.note_text_payment_delayed_listing import NoteTextPaymentDelayedListing  # noqa: F401
from openapi_server.models.note_text_payment_delayed_read import NoteTextPaymentDelayedRead  # noqa: F401
from openapi_server.models.note_text_payment_delayed_update import NoteTextPaymentDelayedUpdate  # noqa: F401
from openapi_server.models.note_text_payment_listing import NoteTextPaymentListing  # noqa: F401
from openapi_server.models.note_text_payment_read import NoteTextPaymentRead  # noqa: F401
from openapi_server.models.note_text_payment_update import NoteTextPaymentUpdate  # noqa: F401
from openapi_server.models.note_text_read import NoteTextRead  # noqa: F401
from openapi_server.models.note_text_request_inquiry import NoteTextRequestInquiry  # noqa: F401
from openapi_server.models.note_text_request_inquiry_batch import NoteTextRequestInquiryBatch  # noqa: F401
from openapi_server.models.note_text_request_inquiry_batch_create import NoteTextRequestInquiryBatchCreate  # noqa: F401
from openapi_server.models.note_text_request_inquiry_batch_listing import NoteTextRequestInquiryBatchListing  # noqa: F401
from openapi_server.models.note_text_request_inquiry_batch_read import NoteTextRequestInquiryBatchRead  # noqa: F401
from openapi_server.models.note_text_request_inquiry_batch_update import NoteTextRequestInquiryBatchUpdate  # noqa: F401
from openapi_server.models.note_text_request_inquiry_create import NoteTextRequestInquiryCreate  # noqa: F401
from openapi_server.models.note_text_request_inquiry_listing import NoteTextRequestInquiryListing  # noqa: F401
from openapi_server.models.note_text_request_inquiry_read import NoteTextRequestInquiryRead  # noqa: F401
from openapi_server.models.note_text_request_inquiry_update import NoteTextRequestInquiryUpdate  # noqa: F401
from openapi_server.models.note_text_request_response import NoteTextRequestResponse  # noqa: F401
from openapi_server.models.note_text_request_response_create import NoteTextRequestResponseCreate  # noqa: F401
from openapi_server.models.note_text_request_response_listing import NoteTextRequestResponseListing  # noqa: F401
from openapi_server.models.note_text_request_response_read import NoteTextRequestResponseRead  # noqa: F401
from openapi_server.models.note_text_request_response_update import NoteTextRequestResponseUpdate  # noqa: F401
from openapi_server.models.note_text_schedule_instance import NoteTextScheduleInstance  # noqa: F401
from openapi_server.models.note_text_schedule_instance_create import NoteTextScheduleInstanceCreate  # noqa: F401
from openapi_server.models.note_text_schedule_instance_listing import NoteTextScheduleInstanceListing  # noqa: F401
from openapi_server.models.note_text_schedule_instance_read import NoteTextScheduleInstanceRead  # noqa: F401
from openapi_server.models.note_text_schedule_instance_update import NoteTextScheduleInstanceUpdate  # noqa: F401
from openapi_server.models.note_text_schedule_payment import NoteTextSchedulePayment  # noqa: F401
from openapi_server.models.note_text_schedule_payment_batch import NoteTextSchedulePaymentBatch  # noqa: F401
from openapi_server.models.note_text_schedule_payment_batch_create import NoteTextSchedulePaymentBatchCreate  # noqa: F401
from openapi_server.models.note_text_schedule_payment_batch_listing import NoteTextSchedulePaymentBatchListing  # noqa: F401
from openapi_server.models.note_text_schedule_payment_batch_read import NoteTextSchedulePaymentBatchRead  # noqa: F401
from openapi_server.models.note_text_schedule_payment_batch_update import NoteTextSchedulePaymentBatchUpdate  # noqa: F401
from openapi_server.models.note_text_schedule_payment_create import NoteTextSchedulePaymentCreate  # noqa: F401
from openapi_server.models.note_text_schedule_payment_listing import NoteTextSchedulePaymentListing  # noqa: F401
from openapi_server.models.note_text_schedule_payment_read import NoteTextSchedulePaymentRead  # noqa: F401
from openapi_server.models.note_text_schedule_payment_update import NoteTextSchedulePaymentUpdate  # noqa: F401
from openapi_server.models.note_text_schedule_request import NoteTextScheduleRequest  # noqa: F401
from openapi_server.models.note_text_schedule_request_batch import NoteTextScheduleRequestBatch  # noqa: F401
from openapi_server.models.note_text_schedule_request_batch_create import NoteTextScheduleRequestBatchCreate  # noqa: F401
from openapi_server.models.note_text_schedule_request_batch_listing import NoteTextScheduleRequestBatchListing  # noqa: F401
from openapi_server.models.note_text_schedule_request_batch_read import NoteTextScheduleRequestBatchRead  # noqa: F401
from openapi_server.models.note_text_schedule_request_batch_update import NoteTextScheduleRequestBatchUpdate  # noqa: F401
from openapi_server.models.note_text_schedule_request_create import NoteTextScheduleRequestCreate  # noqa: F401
from openapi_server.models.note_text_schedule_request_listing import NoteTextScheduleRequestListing  # noqa: F401
from openapi_server.models.note_text_schedule_request_read import NoteTextScheduleRequestRead  # noqa: F401
from openapi_server.models.note_text_schedule_request_update import NoteTextScheduleRequestUpdate  # noqa: F401
from openapi_server.models.note_text_sofort_merchant_transaction import NoteTextSofortMerchantTransaction  # noqa: F401
from openapi_server.models.note_text_sofort_merchant_transaction_create import NoteTextSofortMerchantTransactionCreate  # noqa: F401
from openapi_server.models.note_text_sofort_merchant_transaction_listing import NoteTextSofortMerchantTransactionListing  # noqa: F401
from openapi_server.models.note_text_sofort_merchant_transaction_read import NoteTextSofortMerchantTransactionRead  # noqa: F401
from openapi_server.models.note_text_sofort_merchant_transaction_update import NoteTextSofortMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.note_text_whitelist_result import NoteTextWhitelistResult  # noqa: F401
from openapi_server.models.note_text_whitelist_result_create import NoteTextWhitelistResultCreate  # noqa: F401
from openapi_server.models.note_text_whitelist_result_listing import NoteTextWhitelistResultListing  # noqa: F401
from openapi_server.models.note_text_whitelist_result_read import NoteTextWhitelistResultRead  # noqa: F401
from openapi_server.models.note_text_whitelist_result_update import NoteTextWhitelistResultUpdate  # noqa: F401


def test_c_reate_note_text_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_adyen_card_transaction

    
    """
    note_text_adyen_card_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-text".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56),
    #    headers=headers,
    #    json=note_text_adyen_card_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_bunqme_fundraiser_result

    
    """
    note_text_bunq_me_fundraiser_result = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-text".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56),
    #    headers=headers,
    #    json=note_text_bunq_me_fundraiser_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_draft_payment

    
    """
    note_text_draft_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-text".format(userID=56, monetary-accountID=56, draft-paymentID=56),
    #    headers=headers,
    #    json=note_text_draft_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_ideal_merchant_transaction

    
    """
    note_text_ideal_merchant_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-text".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56),
    #    headers=headers,
    #    json=note_text_ideal_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_mastercard_action

    
    """
    note_text_master_card_action = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-text".format(userID=56, monetary-accountID=56, mastercard-actionID=56),
    #    headers=headers,
    #    json=note_text_master_card_action,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_open_banking_merchant_transaction

    
    """
    note_text_open_banking_merchant_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-text".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56),
    #    headers=headers,
    #    json=note_text_open_banking_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_payment(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_payment

    
    """
    note_text_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-text".format(userID=56, monetary-accountID=56, paymentID=56),
    #    headers=headers,
    #    json=note_text_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_payment_batch

    
    """
    note_text_payment_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-text".format(userID=56, monetary-accountID=56, payment-batchID=56),
    #    headers=headers,
    #    json=note_text_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_payment_delayed

    
    """
    note_text_payment_delayed = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-text".format(userID=56, monetary-accountID=56, payment-delayedID=56),
    #    headers=headers,
    #    json=note_text_payment_delayed,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_request_inquiry

    
    """
    note_text_request_inquiry = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-text".format(userID=56, monetary-accountID=56, request-inquiryID=56),
    #    headers=headers,
    #    json=note_text_request_inquiry,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_request_inquiry_batch

    
    """
    note_text_request_inquiry_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-text".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56),
    #    headers=headers,
    #    json=note_text_request_inquiry_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_request_response(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_request_response

    
    """
    note_text_request_response = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-text".format(userID=56, monetary-accountID=56, request-responseID=56),
    #    headers=headers,
    #    json=note_text_request_response,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_schedule_payment

    
    """
    note_text_schedule_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-text".format(userID=56, monetary-accountID=56, schedule-paymentID=56),
    #    headers=headers,
    #    json=note_text_schedule_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_schedule_payment_batch

    
    """
    note_text_schedule_payment_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-text".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56),
    #    headers=headers,
    #    json=note_text_schedule_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_schedule_request_inquiry

    
    """
    note_text_schedule_request = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-text".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56),
    #    headers=headers,
    #    json=note_text_schedule_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_schedule_request_inquiry_batch

    
    """
    note_text_schedule_request_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-text".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56),
    #    headers=headers,
    #    json=note_text_schedule_request_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_schedule_schedule_instance

    
    """
    note_text_schedule_instance = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-text".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56),
    #    headers=headers,
    #    json=note_text_schedule_instance,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_sofort_merchant_transaction

    
    """
    note_text_sofort_merchant_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-text".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56),
    #    headers=headers,
    #    json=note_text_sofort_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_switch_service_payment

    
    """
    note_text_bank_switch_service_netherlands_incoming_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-text".format(userID=56, monetary-accountID=56, switch-service-paymentID=56),
    #    headers=headers,
    #    json=note_text_bank_switch_service_netherlands_incoming_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_text_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for c_reate_note_text_for_user_monetary_account_whitelist_whitelist_result

    
    """
    note_text_whitelist_result = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-text".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56),
    #    headers=headers,
    #    json=note_text_whitelist_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_bunqme_fundraiser_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_draft_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, draft-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_ideal_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_open_banking_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_payment(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_payment_delayed

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, payment-delayedID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_request_response(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_request_response

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-responseID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_schedule_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_schedule_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_schedule_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_schedule_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_schedule_schedule_instance

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_sofort_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_switch_service_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, switch-service-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_text_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for d_elete_note_text_for_user_monetary_account_whitelist_whitelist_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/note-text".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-text".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_bunqme_fundraiser_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-text".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_draft_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-text".format(userID=56, monetary-accountID=56, draft-paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_ideal_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-text".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-text".format(userID=56, monetary-accountID=56, mastercard-actionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_open_banking_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-text".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_payment(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-text".format(userID=56, monetary-accountID=56, paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-text".format(userID=56, monetary-accountID=56, payment-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_payment_delayed

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-text".format(userID=56, monetary-accountID=56, payment-delayedID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-text".format(userID=56, monetary-accountID=56, request-inquiryID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-text".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_request_response(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_request_response

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-text".format(userID=56, monetary-accountID=56, request-responseID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_schedule_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-text".format(userID=56, monetary-accountID=56, schedule-paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_schedule_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-text".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_schedule_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-text".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_schedule_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-text".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_schedule_schedule_instance

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-text".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_sofort_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-text".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_switch_service_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-text".format(userID=56, monetary-accountID=56, switch-service-paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_text_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for list_all_note_text_for_user_monetary_account_whitelist_whitelist_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-text".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_bunqme_fundraiser_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_draft_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, draft-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_ideal_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_open_banking_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_payment(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_payment_delayed

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, payment-delayedID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_request_response(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_request_response

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-responseID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_schedule_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_schedule_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_schedule_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_schedule_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_schedule_schedule_instance

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_sofort_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_switch_service_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, switch-service-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_text_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for r_ead_note_text_for_user_monetary_account_whitelist_whitelist_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_adyen_card_transaction

    
    """
    note_text_adyen_card_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_adyen_card_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_bunqme_fundraiser_result

    
    """
    note_text_bunq_me_fundraiser_result = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_bunq_me_fundraiser_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_draft_payment

    
    """
    note_text_draft_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, draft-paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_draft_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_ideal_merchant_transaction

    
    """
    note_text_ideal_merchant_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_ideal_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_mastercard_action

    
    """
    note_text_master_card_action = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_master_card_action,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_open_banking_merchant_transaction

    
    """
    note_text_open_banking_merchant_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_open_banking_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_payment(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_payment

    
    """
    note_text_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_payment_batch

    
    """
    note_text_payment_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, payment-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_payment_delayed

    
    """
    note_text_payment_delayed = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, payment-delayedID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_payment_delayed,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_request_inquiry

    
    """
    note_text_request_inquiry = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-inquiryID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_request_inquiry,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_request_inquiry_batch

    
    """
    note_text_request_inquiry_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_request_inquiry_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_request_response(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_request_response

    
    """
    note_text_request_response = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, request-responseID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_request_response,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_schedule_payment

    
    """
    note_text_schedule_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_schedule_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_schedule_payment_batch

    
    """
    note_text_schedule_payment_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_schedule_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_schedule_request_inquiry

    
    """
    note_text_schedule_request = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_schedule_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_schedule_request_inquiry_batch

    
    """
    note_text_schedule_request_batch = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_schedule_request_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_schedule_schedule_instance

    
    """
    note_text_schedule_instance = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_schedule_instance,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_sofort_merchant_transaction

    
    """
    note_text_sofort_merchant_transaction = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_sofort_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_switch_service_payment

    
    """
    note_text_bank_switch_service_netherlands_incoming_payment = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, switch-service-paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_bank_switch_service_netherlands_incoming_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_text_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for u_pdate_note_text_for_user_monetary_account_whitelist_whitelist_result

    
    """
    note_text_whitelist_result = {"content":"content"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-text/{itemId}".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56, itemId=56),
    #    headers=headers,
    #    json=note_text_whitelist_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

