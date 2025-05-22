# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_transport import UserTransport  # noqa: F401
from openapi_server.models.user_transport_create import UserTransportCreate  # noqa: F401
from openapi_server.models.user_transport_listing import UserTransportListing  # noqa: F401
from openapi_server.models.user_transport_read import UserTransportRead  # noqa: F401
from openapi_server.models.user_transport_update import UserTransportUpdate  # noqa: F401


def test_c_reate_user_transport(client: TestClient):
    """Test case for c_reate_user_transport

    
    """
    user_transport = {"address_postal":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"date_of_birth":"date_of_birth","public_nick_name":"public_nick_name","last_name":"last_name","address_main":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"middle_name":"middle_name","display_name":"display_name","first_name":"first_name"}

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
    #    "/user-transport",
    #    headers=headers,
    #    json=user_transport,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_transport(client: TestClient):
    """Test case for list_all_user_transport

    
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
    #    "/user-transport",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_user_transport(client: TestClient):
    """Test case for r_ead_user_transport

    
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
    #    "/user-transport/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_transport(client: TestClient):
    """Test case for u_pdate_user_transport

    
    """
    user_transport = {"address_postal":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"date_of_birth":"date_of_birth","public_nick_name":"public_nick_name","last_name":"last_name","address_main":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"middle_name":"middle_name","display_name":"display_name","first_name":"first_name"}

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
    #    "/user-transport/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=user_transport,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

