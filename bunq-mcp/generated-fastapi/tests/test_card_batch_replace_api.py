# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_batch_replace import CardBatchReplace  # noqa: F401
from openapi_server.models.card_batch_replace_create import CardBatchReplaceCreate  # noqa: F401


def test_c_reate_card_batch_replace_for_user(client: TestClient):
    """Test case for c_reate_card_batch_replace_for_user

    
    """
    card_batch_replace = {"cards":[{"second_line":"second_line","pin_code_assignment":[{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"},{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"}],"id":0,"name_on_card":"name_on_card"},{"second_line":"second_line","pin_code_assignment":[{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"},{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"}],"id":0,"name_on_card":"name_on_card"}]}

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
    #    "/user/{userID}/card-batch-replace".format(userID=56),
    #    headers=headers,
    #    json=card_batch_replace,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

