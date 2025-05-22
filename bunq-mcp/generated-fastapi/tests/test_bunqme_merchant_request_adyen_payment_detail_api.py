# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_adyen_payment_detail import BunqMeMerchantRequestAdyenPaymentDetail  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_adyen_payment_detail_update import BunqMeMerchantRequestAdyenPaymentDetailUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_u_pdate_bunqme_merchant_request_adyen_payment_detail(client: TestClient):
    """Test case for u_pdate_bunqme_merchant_request_adyen_payment_detail

    
    """
    bunq_me_merchant_request_adyen_payment_detail = {"payment_detail":["payment_detail","payment_detail"]}

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
    #    "/bunqme-merchant-request-adyen-payment-detail/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=bunq_me_merchant_request_adyen_payment_detail,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

