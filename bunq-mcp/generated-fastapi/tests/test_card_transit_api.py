# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_transit import CardTransit  # noqa: F401
from openapi_server.models.card_transit_create import CardTransitCreate  # noqa: F401


def test_c_reate_card_transit_for_user(client: TestClient):
    """Test case for c_reate_card_transit_for_user

    
    """
    card_transit = {"country":"country","preferred_name_on_card":"preferred_name_on_card","first_line":"first_line","address_postal":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"pin_code_assignment":[{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"},{"routing_type":"routing_type","pin_code":"pin_code","monetary_account_id":3,"type":"type","status":"status"}],"monetary_account_id_fallback":0,"type":"type","setting":{"color":"color","service_id":"service_id","icon":"icon","currency_routing_type":"currency_routing_type","border_color":"border_color","image_id":"image_id"},"product_sub_type":"product_sub_type","second_line":"second_line","order_status":"order_status","product_type":"product_type","alias":{"service":"service","name":"name","type":"type","value":"value"},"name_on_card":"name_on_card"}

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
    #    "/user/{userID}/card-transit".format(userID=56),
    #    headers=headers,
    #    json=card_transit,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

