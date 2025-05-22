# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.pack_group import PackGroup  # noqa: F401
from openapi_server.models.pack_group_create import PackGroupCreate  # noqa: F401
from openapi_server.models.pack_group_listing import PackGroupListing  # noqa: F401
from openapi_server.models.pack_group_read import PackGroupRead  # noqa: F401
from openapi_server.models.pack_group_update import PackGroupUpdate  # noqa: F401


def test_c_reate_pack_group_for_user(client: TestClient):
    """Test case for c_reate_pack_group_for_user

    
    """
    pack_group = {"person_memberships":[{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}},{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}}],"company_memberships":[{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}},{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}}],"type":"type"}

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
    #    "/user/{userID}/pack-group".format(userID=56),
    #    headers=headers,
    #    json=pack_group,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_pack_group_for_user(client: TestClient):
    """Test case for d_elete_pack_group_for_user

    
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
    #    "DELETE",
    #    "/user/{userID}/pack-group/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_pack_group_for_user(client: TestClient):
    """Test case for list_all_pack_group_for_user

    
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
    #    "/user/{userID}/pack-group".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_pack_group_for_user(client: TestClient):
    """Test case for r_ead_pack_group_for_user

    
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
    #    "/user/{userID}/pack-group/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_pack_group_for_user(client: TestClient):
    """Test case for u_pdate_pack_group_for_user

    
    """
    pack_group = {"person_memberships":[{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}},{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}}],"company_memberships":[{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}},{"user_pointer":{"service":"service","name":"name","type":"type","value":"value"}}],"type":"type"}

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
    #    "/user/{userID}/pack-group/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=pack_group,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

