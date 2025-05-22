# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transferwise_transfer import TransferwiseTransfer  # noqa: F401
from openapi_server.models.transferwise_transfer_create import TransferwiseTransferCreate  # noqa: F401
from openapi_server.models.transferwise_transfer_listing import TransferwiseTransferListing  # noqa: F401
from openapi_server.models.transferwise_transfer_read import TransferwiseTransferRead  # noqa: F401


def test_c_reate_transferwise_transfer_for_user_transferwise_quote(client: TestClient):
    """Test case for c_reate_transferwise_transfer_for_user_transferwise_quote

    
    """
    transferwise_transfer = {"sub_status":"sub_status","time_delivery_estimate":"time_delivery_estimate","monetary_account_id":"monetary_account_id","status_transferwise_issue":"status_transferwise_issue","pay_in_reference":"pay_in_reference","reference":"reference","amount_source":{"currency":"currency","value":"value"},"status_transferwise":"status_transferwise","quote":{"amount_source":{"currency":"currency","value":"value"},"currency_source":"currency_source","rate":"rate","created":"created","time_expiry":"time_expiry","time_delivery_estimate":"time_delivery_estimate","currency_target":"currency_target","quote_id":"quote_id","amount_fee":{"currency":"currency","value":"value"},"amount_target":{"currency":"currency","value":"value"},"id":5,"updated":"updated"},"rate":"rate","counterparty_alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"amount_target":{"currency":"currency","value":"value"},"recipient_id":"recipient_id","status":"status"}

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
    #    "/user/{userID}/transferwise-quote/{transferwise-quoteID}/transferwise-transfer".format(userID=56, transferwise-quoteID=56),
    #    headers=headers,
    #    json=transferwise_transfer,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_transferwise_transfer_for_user_transferwise_quote(client: TestClient):
    """Test case for list_all_transferwise_transfer_for_user_transferwise_quote

    
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
    #    "/user/{userID}/transferwise-quote/{transferwise-quoteID}/transferwise-transfer".format(userID=56, transferwise-quoteID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transferwise_transfer_for_user_transferwise_quote(client: TestClient):
    """Test case for r_ead_transferwise_transfer_for_user_transferwise_quote

    
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
    #    "/user/{userID}/transferwise-quote/{transferwise-quoteID}/transferwise-transfer/{itemId}".format(userID=56, transferwise-quoteID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

