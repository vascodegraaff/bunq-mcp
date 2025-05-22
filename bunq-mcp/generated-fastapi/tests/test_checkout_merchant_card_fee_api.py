# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.checkout_merchant_card_fee import CheckoutMerchantCardFee  # noqa: F401
from openapi_server.models.checkout_merchant_card_fee_create import CheckoutMerchantCardFeeCreate  # noqa: F401


def test_c_reate_checkout_merchant_card_fee_for_user(client: TestClient):
    """Test case for c_reate_checkout_merchant_card_fee_for_user

    
    """
    checkout_merchant_card_fee = {"checkout_merchant_card_id":0,"amount_requested":{"currency":"currency","value":"value"},"token_type":"token_type"}

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
    #    "/user/{userID}/checkout-merchant-card-fee".format(userID=56),
    #    headers=headers,
    #    json=checkout_merchant_card_fee,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

