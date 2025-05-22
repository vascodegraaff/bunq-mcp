# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_replace import CardReplace  # noqa: F401
from openapi_server.models.card_replace_create import CardReplaceCreate  # noqa: F401


def test_c_reate_replace_for_user_card(client: TestClient):
    """Test case for c_reate_replace_for_user_card

    
    """
    card_replace = {"second_line":"second_line","preferred_name_on_card":"preferred_name_on_card","pin_code_assignment":[{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"},{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"}],"attachment_id":0,"name_on_card":"name_on_card","customization_type":"customization_type"}

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
    #    "/user/{userID}/card/{cardID}/replace".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=card_replace,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

