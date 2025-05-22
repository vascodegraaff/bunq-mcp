# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.note_attachment_adyen_card_transaction import NoteAttachmentAdyenCardTransaction  # noqa: F401
from openapi_server.models.note_attachment_adyen_card_transaction_create import NoteAttachmentAdyenCardTransactionCreate  # noqa: F401
from openapi_server.models.note_attachment_adyen_card_transaction_listing import NoteAttachmentAdyenCardTransactionListing  # noqa: F401
from openapi_server.models.note_attachment_adyen_card_transaction_read import NoteAttachmentAdyenCardTransactionRead  # noqa: F401
from openapi_server.models.note_attachment_adyen_card_transaction_update import NoteAttachmentAdyenCardTransactionUpdate  # noqa: F401
from openapi_server.models.note_attachment_bank_switch_service_netherlands_incoming_payment import NoteAttachmentBankSwitchServiceNetherlandsIncomingPayment  # noqa: F401
from openapi_server.models.note_attachment_bank_switch_service_netherlands_incoming_payment_create import NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentCreate  # noqa: F401
from openapi_server.models.note_attachment_bank_switch_service_netherlands_incoming_payment_listing import NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentListing  # noqa: F401
from openapi_server.models.note_attachment_bank_switch_service_netherlands_incoming_payment_read import NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentRead  # noqa: F401
from openapi_server.models.note_attachment_bank_switch_service_netherlands_incoming_payment_update import NoteAttachmentBankSwitchServiceNetherlandsIncomingPaymentUpdate  # noqa: F401
from openapi_server.models.note_attachment_bunq_me_fundraiser_result import NoteAttachmentBunqMeFundraiserResult  # noqa: F401
from openapi_server.models.note_attachment_bunq_me_fundraiser_result_create import NoteAttachmentBunqMeFundraiserResultCreate  # noqa: F401
from openapi_server.models.note_attachment_bunq_me_fundraiser_result_listing import NoteAttachmentBunqMeFundraiserResultListing  # noqa: F401
from openapi_server.models.note_attachment_bunq_me_fundraiser_result_read import NoteAttachmentBunqMeFundraiserResultRead  # noqa: F401
from openapi_server.models.note_attachment_bunq_me_fundraiser_result_update import NoteAttachmentBunqMeFundraiserResultUpdate  # noqa: F401
from openapi_server.models.note_attachment_draft_payment import NoteAttachmentDraftPayment  # noqa: F401
from openapi_server.models.note_attachment_draft_payment_create import NoteAttachmentDraftPaymentCreate  # noqa: F401
from openapi_server.models.note_attachment_draft_payment_listing import NoteAttachmentDraftPaymentListing  # noqa: F401
from openapi_server.models.note_attachment_draft_payment_read import NoteAttachmentDraftPaymentRead  # noqa: F401
from openapi_server.models.note_attachment_draft_payment_update import NoteAttachmentDraftPaymentUpdate  # noqa: F401
from openapi_server.models.note_attachment_ideal_merchant_transaction import NoteAttachmentIdealMerchantTransaction  # noqa: F401
from openapi_server.models.note_attachment_ideal_merchant_transaction_create import NoteAttachmentIdealMerchantTransactionCreate  # noqa: F401
from openapi_server.models.note_attachment_ideal_merchant_transaction_listing import NoteAttachmentIdealMerchantTransactionListing  # noqa: F401
from openapi_server.models.note_attachment_ideal_merchant_transaction_read import NoteAttachmentIdealMerchantTransactionRead  # noqa: F401
from openapi_server.models.note_attachment_ideal_merchant_transaction_update import NoteAttachmentIdealMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.note_attachment_listing import NoteAttachmentListing  # noqa: F401
from openapi_server.models.note_attachment_master_card_action import NoteAttachmentMasterCardAction  # noqa: F401
from openapi_server.models.note_attachment_master_card_action_create import NoteAttachmentMasterCardActionCreate  # noqa: F401
from openapi_server.models.note_attachment_master_card_action_listing import NoteAttachmentMasterCardActionListing  # noqa: F401
from openapi_server.models.note_attachment_master_card_action_read import NoteAttachmentMasterCardActionRead  # noqa: F401
from openapi_server.models.note_attachment_master_card_action_update import NoteAttachmentMasterCardActionUpdate  # noqa: F401
from openapi_server.models.note_attachment_open_banking_merchant_transaction import NoteAttachmentOpenBankingMerchantTransaction  # noqa: F401
from openapi_server.models.note_attachment_open_banking_merchant_transaction_create import NoteAttachmentOpenBankingMerchantTransactionCreate  # noqa: F401
from openapi_server.models.note_attachment_open_banking_merchant_transaction_listing import NoteAttachmentOpenBankingMerchantTransactionListing  # noqa: F401
from openapi_server.models.note_attachment_open_banking_merchant_transaction_read import NoteAttachmentOpenBankingMerchantTransactionRead  # noqa: F401
from openapi_server.models.note_attachment_open_banking_merchant_transaction_update import NoteAttachmentOpenBankingMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.note_attachment_payment import NoteAttachmentPayment  # noqa: F401
from openapi_server.models.note_attachment_payment_batch import NoteAttachmentPaymentBatch  # noqa: F401
from openapi_server.models.note_attachment_payment_batch_create import NoteAttachmentPaymentBatchCreate  # noqa: F401
from openapi_server.models.note_attachment_payment_batch_listing import NoteAttachmentPaymentBatchListing  # noqa: F401
from openapi_server.models.note_attachment_payment_batch_read import NoteAttachmentPaymentBatchRead  # noqa: F401
from openapi_server.models.note_attachment_payment_batch_update import NoteAttachmentPaymentBatchUpdate  # noqa: F401
from openapi_server.models.note_attachment_payment_create import NoteAttachmentPaymentCreate  # noqa: F401
from openapi_server.models.note_attachment_payment_delayed import NoteAttachmentPaymentDelayed  # noqa: F401
from openapi_server.models.note_attachment_payment_delayed_create import NoteAttachmentPaymentDelayedCreate  # noqa: F401
from openapi_server.models.note_attachment_payment_delayed_listing import NoteAttachmentPaymentDelayedListing  # noqa: F401
from openapi_server.models.note_attachment_payment_delayed_read import NoteAttachmentPaymentDelayedRead  # noqa: F401
from openapi_server.models.note_attachment_payment_delayed_update import NoteAttachmentPaymentDelayedUpdate  # noqa: F401
from openapi_server.models.note_attachment_payment_listing import NoteAttachmentPaymentListing  # noqa: F401
from openapi_server.models.note_attachment_payment_read import NoteAttachmentPaymentRead  # noqa: F401
from openapi_server.models.note_attachment_payment_update import NoteAttachmentPaymentUpdate  # noqa: F401
from openapi_server.models.note_attachment_read import NoteAttachmentRead  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry import NoteAttachmentRequestInquiry  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_batch import NoteAttachmentRequestInquiryBatch  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_batch_create import NoteAttachmentRequestInquiryBatchCreate  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_batch_listing import NoteAttachmentRequestInquiryBatchListing  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_batch_read import NoteAttachmentRequestInquiryBatchRead  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_batch_update import NoteAttachmentRequestInquiryBatchUpdate  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_create import NoteAttachmentRequestInquiryCreate  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_listing import NoteAttachmentRequestInquiryListing  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_read import NoteAttachmentRequestInquiryRead  # noqa: F401
from openapi_server.models.note_attachment_request_inquiry_update import NoteAttachmentRequestInquiryUpdate  # noqa: F401
from openapi_server.models.note_attachment_request_response import NoteAttachmentRequestResponse  # noqa: F401
from openapi_server.models.note_attachment_request_response_create import NoteAttachmentRequestResponseCreate  # noqa: F401
from openapi_server.models.note_attachment_request_response_listing import NoteAttachmentRequestResponseListing  # noqa: F401
from openapi_server.models.note_attachment_request_response_read import NoteAttachmentRequestResponseRead  # noqa: F401
from openapi_server.models.note_attachment_request_response_update import NoteAttachmentRequestResponseUpdate  # noqa: F401
from openapi_server.models.note_attachment_schedule_instance import NoteAttachmentScheduleInstance  # noqa: F401
from openapi_server.models.note_attachment_schedule_instance_create import NoteAttachmentScheduleInstanceCreate  # noqa: F401
from openapi_server.models.note_attachment_schedule_instance_listing import NoteAttachmentScheduleInstanceListing  # noqa: F401
from openapi_server.models.note_attachment_schedule_instance_read import NoteAttachmentScheduleInstanceRead  # noqa: F401
from openapi_server.models.note_attachment_schedule_instance_update import NoteAttachmentScheduleInstanceUpdate  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment import NoteAttachmentSchedulePayment  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_batch import NoteAttachmentSchedulePaymentBatch  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_batch_create import NoteAttachmentSchedulePaymentBatchCreate  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_batch_listing import NoteAttachmentSchedulePaymentBatchListing  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_batch_read import NoteAttachmentSchedulePaymentBatchRead  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_batch_update import NoteAttachmentSchedulePaymentBatchUpdate  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_create import NoteAttachmentSchedulePaymentCreate  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_listing import NoteAttachmentSchedulePaymentListing  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_read import NoteAttachmentSchedulePaymentRead  # noqa: F401
from openapi_server.models.note_attachment_schedule_payment_update import NoteAttachmentSchedulePaymentUpdate  # noqa: F401
from openapi_server.models.note_attachment_schedule_request import NoteAttachmentScheduleRequest  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_batch import NoteAttachmentScheduleRequestBatch  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_batch_create import NoteAttachmentScheduleRequestBatchCreate  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_batch_listing import NoteAttachmentScheduleRequestBatchListing  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_batch_read import NoteAttachmentScheduleRequestBatchRead  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_batch_update import NoteAttachmentScheduleRequestBatchUpdate  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_create import NoteAttachmentScheduleRequestCreate  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_listing import NoteAttachmentScheduleRequestListing  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_read import NoteAttachmentScheduleRequestRead  # noqa: F401
from openapi_server.models.note_attachment_schedule_request_update import NoteAttachmentScheduleRequestUpdate  # noqa: F401
from openapi_server.models.note_attachment_sofort_merchant_transaction import NoteAttachmentSofortMerchantTransaction  # noqa: F401
from openapi_server.models.note_attachment_sofort_merchant_transaction_create import NoteAttachmentSofortMerchantTransactionCreate  # noqa: F401
from openapi_server.models.note_attachment_sofort_merchant_transaction_listing import NoteAttachmentSofortMerchantTransactionListing  # noqa: F401
from openapi_server.models.note_attachment_sofort_merchant_transaction_read import NoteAttachmentSofortMerchantTransactionRead  # noqa: F401
from openapi_server.models.note_attachment_sofort_merchant_transaction_update import NoteAttachmentSofortMerchantTransactionUpdate  # noqa: F401
from openapi_server.models.note_attachment_whitelist_result import NoteAttachmentWhitelistResult  # noqa: F401
from openapi_server.models.note_attachment_whitelist_result_create import NoteAttachmentWhitelistResultCreate  # noqa: F401
from openapi_server.models.note_attachment_whitelist_result_listing import NoteAttachmentWhitelistResultListing  # noqa: F401
from openapi_server.models.note_attachment_whitelist_result_read import NoteAttachmentWhitelistResultRead  # noqa: F401
from openapi_server.models.note_attachment_whitelist_result_update import NoteAttachmentWhitelistResultUpdate  # noqa: F401


def test_c_reate_note_attachment_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_adyen_card_transaction

    
    """
    note_attachment_adyen_card_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56),
    #    headers=headers,
    #    json=note_attachment_adyen_card_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_bunqme_fundraiser_result

    
    """
    note_attachment_bunq_me_fundraiser_result = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-attachment".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56),
    #    headers=headers,
    #    json=note_attachment_bunq_me_fundraiser_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_draft_payment

    
    """
    note_attachment_draft_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-attachment".format(userID=56, monetary-accountID=56, draft-paymentID=56),
    #    headers=headers,
    #    json=note_attachment_draft_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_ideal_merchant_transaction

    
    """
    note_attachment_ideal_merchant_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56),
    #    headers=headers,
    #    json=note_attachment_ideal_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_mastercard_action

    
    """
    note_attachment_master_card_action = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-attachment".format(userID=56, monetary-accountID=56, mastercard-actionID=56),
    #    headers=headers,
    #    json=note_attachment_master_card_action,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_open_banking_merchant_transaction

    
    """
    note_attachment_open_banking_merchant_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56),
    #    headers=headers,
    #    json=note_attachment_open_banking_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_payment(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_payment

    
    """
    note_attachment_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-attachment".format(userID=56, monetary-accountID=56, paymentID=56),
    #    headers=headers,
    #    json=note_attachment_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_payment_batch

    
    """
    note_attachment_payment_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-attachment".format(userID=56, monetary-accountID=56, payment-batchID=56),
    #    headers=headers,
    #    json=note_attachment_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_payment_delayed

    
    """
    note_attachment_payment_delayed = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-attachment".format(userID=56, monetary-accountID=56, payment-delayedID=56),
    #    headers=headers,
    #    json=note_attachment_payment_delayed,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_request_inquiry

    
    """
    note_attachment_request_inquiry = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-attachment".format(userID=56, monetary-accountID=56, request-inquiryID=56),
    #    headers=headers,
    #    json=note_attachment_request_inquiry,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_request_inquiry_batch

    
    """
    note_attachment_request_inquiry_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-attachment".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56),
    #    headers=headers,
    #    json=note_attachment_request_inquiry_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_request_response(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_request_response

    
    """
    note_attachment_request_response = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-attachment".format(userID=56, monetary-accountID=56, request-responseID=56),
    #    headers=headers,
    #    json=note_attachment_request_response,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_schedule_payment

    
    """
    note_attachment_schedule_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-paymentID=56),
    #    headers=headers,
    #    json=note_attachment_schedule_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_schedule_payment_batch

    
    """
    note_attachment_schedule_payment_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56),
    #    headers=headers,
    #    json=note_attachment_schedule_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_schedule_request_inquiry

    
    """
    note_attachment_schedule_request = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56),
    #    headers=headers,
    #    json=note_attachment_schedule_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch

    
    """
    note_attachment_schedule_request_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56),
    #    headers=headers,
    #    json=note_attachment_schedule_request_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_schedule_schedule_instance

    
    """
    note_attachment_schedule_instance = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-attachment".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56),
    #    headers=headers,
    #    json=note_attachment_schedule_instance,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_sofort_merchant_transaction

    
    """
    note_attachment_sofort_merchant_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56),
    #    headers=headers,
    #    json=note_attachment_sofort_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_switch_service_payment

    
    """
    note_attachment_bank_switch_service_netherlands_incoming_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-attachment".format(userID=56, monetary-accountID=56, switch-service-paymentID=56),
    #    headers=headers,
    #    json=note_attachment_bank_switch_service_netherlands_incoming_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_note_attachment_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for c_reate_note_attachment_for_user_monetary_account_whitelist_whitelist_result

    
    """
    note_attachment_whitelist_result = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-attachment".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56),
    #    headers=headers,
    #    json=note_attachment_whitelist_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_bunqme_fundraiser_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_draft_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, draft-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_ideal_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_open_banking_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_payment(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_payment_delayed

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, payment-delayedID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_request_response(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_request_response

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-responseID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_schedule_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_schedule_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_schedule_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_schedule_schedule_instance

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_sofort_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_switch_service_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, switch-service-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_note_attachment_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for d_elete_note_attachment_for_user_monetary_account_whitelist_whitelist_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/note-attachment".format(userID=56, monetary-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_bunqme_fundraiser_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-attachment".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_draft_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-attachment".format(userID=56, monetary-accountID=56, draft-paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_ideal_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-attachment".format(userID=56, monetary-accountID=56, mastercard-actionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_open_banking_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_payment(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-attachment".format(userID=56, monetary-accountID=56, paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-attachment".format(userID=56, monetary-accountID=56, payment-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_payment_delayed

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-attachment".format(userID=56, monetary-accountID=56, payment-delayedID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-attachment".format(userID=56, monetary-accountID=56, request-inquiryID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-attachment".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_request_response(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_request_response

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-attachment".format(userID=56, monetary-accountID=56, request-responseID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_schedule_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_schedule_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_schedule_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-attachment".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_schedule_schedule_instance

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-attachment".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_sofort_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-attachment".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_switch_service_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-attachment".format(userID=56, monetary-accountID=56, switch-service-paymentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for list_all_note_attachment_for_user_monetary_account_whitelist_whitelist_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-attachment".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_adyen_card_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_bunqme_fundraiser_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_draft_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, draft-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_ideal_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_mastercard_action

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_open_banking_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_payment(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_payment_delayed

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, payment-delayedID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_request_response(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_request_response

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-responseID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_schedule_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_schedule_payment_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_schedule_request_inquiry

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_schedule_schedule_instance

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_sofort_merchant_transaction

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_switch_service_payment

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, switch-service-paymentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_note_attachment_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for r_ead_note_attachment_for_user_monetary_account_whitelist_whitelist_result

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_adyen_card_transaction(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_adyen_card_transaction

    
    """
    note_attachment_adyen_card_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/adyen-card-transaction/{adyen-card-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, adyen-card-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_adyen_card_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_bunqme_fundraiser_result(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_bunqme_fundraiser_result

    
    """
    note_attachment_bunq_me_fundraiser_result = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-fundraiser-result/{bunqme-fundraiser-resultID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, bunqme-fundraiser-resultID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_bunq_me_fundraiser_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_draft_payment(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_draft_payment

    
    """
    note_attachment_draft_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/draft-payment/{draft-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, draft-paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_draft_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_ideal_merchant_transaction(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_ideal_merchant_transaction

    
    """
    note_attachment_ideal_merchant_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/ideal-merchant-transaction/{ideal-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, ideal-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_ideal_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_mastercard_action(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_mastercard_action

    
    """
    note_attachment_master_card_action = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/mastercard-action/{mastercard-actionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_master_card_action,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_open_banking_merchant_transaction(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_open_banking_merchant_transaction

    
    """
    note_attachment_open_banking_merchant_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/open-banking-merchant-transaction/{open-banking-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, open-banking-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_open_banking_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_payment(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_payment

    
    """
    note_attachment_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment/{paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_payment_batch(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_payment_batch

    
    """
    note_attachment_payment_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-batch/{payment-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, payment-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_payment_delayed(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_payment_delayed

    
    """
    note_attachment_payment_delayed = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/payment-delayed/{payment-delayedID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, payment-delayedID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_payment_delayed,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_request_inquiry(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_request_inquiry

    
    """
    note_attachment_request_inquiry = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry/{request-inquiryID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-inquiryID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_request_inquiry,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_request_inquiry_batch(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_request_inquiry_batch

    
    """
    note_attachment_request_inquiry_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-inquiry-batch/{request-inquiry-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_request_inquiry_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_request_response(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_request_response

    
    """
    note_attachment_request_response = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/request-response/{request-responseID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, request-responseID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_request_response,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_schedule_payment(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_schedule_payment

    
    """
    note_attachment_schedule_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment/{schedule-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_schedule_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_schedule_payment_batch(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_schedule_payment_batch

    
    """
    note_attachment_schedule_payment_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-payment-batch/{schedule-payment-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-payment-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_schedule_payment_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_schedule_request_inquiry(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_schedule_request_inquiry

    
    """
    note_attachment_schedule_request = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry/{schedule-request-inquiryID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiryID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_schedule_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_schedule_request_inquiry_batch

    
    """
    note_attachment_schedule_request_batch = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule-request-inquiry-batch/{schedule-request-inquiry-batchID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, schedule-request-inquiry-batchID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_schedule_request_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_schedule_schedule_instance(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_schedule_schedule_instance

    
    """
    note_attachment_schedule_instance = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/schedule/{scheduleID}/schedule-instance/{schedule-instanceID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, scheduleID=56, schedule-instanceID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_schedule_instance,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_sofort_merchant_transaction(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_sofort_merchant_transaction

    
    """
    note_attachment_sofort_merchant_transaction = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/sofort-merchant-transaction/{sofort-merchant-transactionID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, sofort-merchant-transactionID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_sofort_merchant_transaction,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_switch_service_payment(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_switch_service_payment

    
    """
    note_attachment_bank_switch_service_netherlands_incoming_payment = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/switch-service-payment/{switch-service-paymentID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, switch-service-paymentID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_bank_switch_service_netherlands_incoming_payment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_note_attachment_for_user_monetary_account_whitelist_whitelist_result(client: TestClient):
    """Test case for u_pdate_note_attachment_for_user_monetary_account_whitelist_whitelist_result

    
    """
    note_attachment_whitelist_result = {"attachment_id":0,"description":"description"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/whitelist/{whitelistID}/whitelist-result/{whitelist-resultID}/note-attachment/{itemId}".format(userID=56, monetary-accountID=56, whitelistID=56, whitelist-resultID=56, itemId=56),
    #    headers=headers,
    #    json=note_attachment_whitelist_result,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

