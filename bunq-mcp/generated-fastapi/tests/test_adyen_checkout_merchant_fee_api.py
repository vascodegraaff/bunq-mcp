# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.adyen_checkout_merchant_transaction_fee import AdyenCheckoutMerchantTransactionFee  # noqa: F401
from openapi_server.models.adyen_checkout_merchant_transaction_fee_create import AdyenCheckoutMerchantTransactionFeeCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_adyen_checkout_merchant_fee_for_user(client: TestClient):
    """Test case for c_reate_adyen_checkout_merchant_fee_for_user

    
    """
    adyen_checkout_merchant_transaction_fee = {"amount_requested":{"currency":"currency","value":"value"},"payment_method":"payment_method"}

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
    #    "/user/{userID}/adyen-checkout-merchant-fee".format(userID=56),
    #    headers=headers,
    #    json=adyen_checkout_merchant_transaction_fee,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

