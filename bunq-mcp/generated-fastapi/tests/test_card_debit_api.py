# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_debit import CardDebit  # noqa: F401
from openapi_server.models.card_debit_create import CardDebitCreate  # noqa: F401


def test_c_reate_card_debit_for_user(client: TestClient):
    """Test case for c_reate_card_debit_for_user

    
    """
    card_debit = {"second_line":"second_line","order_status":"order_status","preferred_name_on_card":"preferred_name_on_card","product_type":"product_type","pin_code_assignment":[{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"},{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"}],"alias":{"service":"service","name":"name","type":"type","value":"value"},"monetary_account_id_fallback":6,"type":"type","name_on_card":"name_on_card"}

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
    #    "/user/{userID}/card-debit".format(userID=56),
    #    headers=headers,
    #    json=card_debit,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

