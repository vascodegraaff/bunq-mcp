# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bunq_me_merchant_request import BunqMeMerchantRequest  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_create import BunqMeMerchantRequestCreate  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_read import BunqMeMerchantRequestRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_bunqme_merchant_request(client: TestClient):
    """Test case for c_reate_bunqme_merchant_request

    
    """
    bunq_me_merchant_request = {"google_recaptcha_code":"google_recaptcha_code","adyen_checkout_sdk_response":["adyen_checkout_sdk_response","adyen_checkout_sdk_response"],"description":"description","adyen_payment_method":"adyen_payment_method","issuer":"issuer","bunqme_type":"bunqme_type","captcha":{"code":"code","provider":"provider"},"amount_requested":{"currency":"currency","value":"value"},"apple_pay_payment_token_data":"apple_pay_payment_token_data","bunqme_uuid":"bunqme_uuid","name":"name","address_billing":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"adyen_browser_data":["adyen_browser_data","adyen_browser_data"],"card_payment_token_data":"card_payment_token_data","merchant_type":"merchant_type"}

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
    #    "/bunqme-merchant-request",
    #    headers=headers,
    #    json=bunq_me_merchant_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_bunqme_merchant_request(client: TestClient):
    """Test case for r_ead_bunqme_merchant_request

    
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
    #    "/bunqme-merchant-request/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

