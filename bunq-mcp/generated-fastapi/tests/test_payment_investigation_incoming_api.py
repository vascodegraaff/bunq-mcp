# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.payment_investigation_incoming import PaymentInvestigationIncoming  # noqa: F401
from openapi_server.models.payment_investigation_incoming_create import PaymentInvestigationIncomingCreate  # noqa: F401


def test_c_reate_payment_investigation_incoming_for_user(client: TestClient):
    """Test case for c_reate_payment_investigation_incoming_for_user

    
    """
    payment_investigation_incoming = {"amount":{"currency":"currency","value":"value"},"attachment":[{"id":6},{"id":6}],"monetary_account_id":0,"description":"description","payment_reference":"payment_reference","type":"type","date_payment_sent":"date_payment_sent","account_number_counterparty":"account_number_counterparty"}

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
    #    "/user/{userID}/payment-investigation-incoming".format(userID=56),
    #    headers=headers,
    #    json=payment_investigation_incoming,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

