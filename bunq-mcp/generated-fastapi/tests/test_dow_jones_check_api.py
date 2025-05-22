# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.dow_jones_check import DowJonesCheck  # noqa: F401
from openapi_server.models.dow_jones_check_read import DowJonesCheckRead  # noqa: F401
from openapi_server.models.dow_jones_check_update import DowJonesCheckUpdate  # noqa: F401


def test_r_ead_dow_jones_check(client: TestClient):
    """Test case for r_ead_dow_jones_check

    
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
    #    "/dow-jones-check/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_dow_jones_check(client: TestClient):
    """Test case for u_pdate_dow_jones_check

    
    """
    dow_jones_check = {"user_admin_id":6,"sub_status":"sub_status","user_id":0,"time_last_check":"time_last_check","dow_jones_hit":[{"risk_class":"risk_class","xml":"xml","dow_jones_id":"dow_jones_id"},{"risk_class":"risk_class","xml":"xml","dow_jones_id":"dow_jones_id"}],"status":"status"}

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
    #    "/dow-jones-check/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=dow_jones_check,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

