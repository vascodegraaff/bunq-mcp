# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.dow_jones_white_list import DowJonesWhiteList  # noqa: F401
from openapi_server.models.dow_jones_white_list_create import DowJonesWhiteListCreate  # noqa: F401
from openapi_server.models.dow_jones_white_list_read import DowJonesWhiteListRead  # noqa: F401
from openapi_server.models.dow_jones_white_list_update import DowJonesWhiteListUpdate  # noqa: F401


def test_c_reate_dow_jones_white_list(client: TestClient):
    """Test case for c_reate_dow_jones_white_list

    
    """
    dow_jones_white_list = {"white_listed_dow_jones_id":0,"white_listed_type":"white_listed_type","iban":"iban","comment":"comment","status":"status"}

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
    #    "/dow-jones-white-list",
    #    headers=headers,
    #    json=dow_jones_white_list,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_dow_jones_white_list(client: TestClient):
    """Test case for r_ead_dow_jones_white_list

    
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
    #    "/dow-jones-white-list/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_dow_jones_white_list(client: TestClient):
    """Test case for u_pdate_dow_jones_white_list

    
    """
    dow_jones_white_list = {"white_listed_dow_jones_id":0,"white_listed_type":"white_listed_type","iban":"iban","comment":"comment","status":"status"}

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
    #    "/dow-jones-white-list/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=dow_jones_white_list,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

