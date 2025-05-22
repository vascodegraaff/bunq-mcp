# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.sim_virtual_product_order import SimVirtualProductOrder  # noqa: F401
from openapi_server.models.sim_virtual_product_order_create import SimVirtualProductOrderCreate  # noqa: F401
from openapi_server.models.sim_virtual_product_order_listing import SimVirtualProductOrderListing  # noqa: F401
from openapi_server.models.sim_virtual_product_order_update import SimVirtualProductOrderUpdate  # noqa: F401


def test_c_reate_product_order_for_user_sim_virtual(client: TestClient):
    """Test case for c_reate_product_order_for_user_sim_virtual

    
    """
    sim_virtual_product_order = {"product_offering_id":"product_offering_id","amount_billing_override":{"currency":"currency","value":"value"},"activation_type":"activation_type","country_purchase":"country_purchase","type":"type","activation_time":"activation_time","status":"status"}

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
    #    "/user/{userID}/sim-virtual/{sim-virtualID}/product-order".format(userID=56, sim-virtualID=56),
    #    headers=headers,
    #    json=sim_virtual_product_order,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_product_order_for_user_sim_virtual(client: TestClient):
    """Test case for list_all_product_order_for_user_sim_virtual

    
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
    #    "/user/{userID}/sim-virtual/{sim-virtualID}/product-order".format(userID=56, sim-virtualID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_product_order_for_user_sim_virtual(client: TestClient):
    """Test case for u_pdate_product_order_for_user_sim_virtual

    
    """
    sim_virtual_product_order = {"product_offering_id":"product_offering_id","amount_billing_override":{"currency":"currency","value":"value"},"activation_type":"activation_type","country_purchase":"country_purchase","type":"type","activation_time":"activation_time","status":"status"}

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
    #    "/user/{userID}/sim-virtual/{sim-virtualID}/product-order/{itemId}".format(userID=56, sim-virtualID=56, itemId=56),
    #    headers=headers,
    #    json=sim_virtual_product_order,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

