# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.chamber_of_commerce_excerpt_basic import ChamberOfCommerceExcerptBasic  # noqa: F401
from openapi_server.models.chamber_of_commerce_excerpt_basic_create import ChamberOfCommerceExcerptBasicCreate  # noqa: F401
from openapi_server.models.chamber_of_commerce_excerpt_basic_listing import ChamberOfCommerceExcerptBasicListing  # noqa: F401
from openapi_server.models.chamber_of_commerce_excerpt_user_basic_create import ChamberOfCommerceExcerptUserBasicCreate  # noqa: F401
from openapi_server.models.chamber_of_commerce_excerpt_user_basic_listing import ChamberOfCommerceExcerptUserBasicListing  # noqa: F401


def test_c_reate_chamber_of_commerce_excerpt_basic(client: TestClient):
    """Test case for c_reate_chamber_of_commerce_excerpt_basic

    
    """
    chamber_of_commerce_excerpt_basic = {"country":"country","chamber_of_commerce_number":"chamber_of_commerce_number"}

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
    #    "/chamber-of-commerce-excerpt-basic",
    #    headers=headers,
    #    json=chamber_of_commerce_excerpt_basic,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_chamber_of_commerce_excerpt_basic_for_user(client: TestClient):
    """Test case for c_reate_chamber_of_commerce_excerpt_basic_for_user

    
    """
    body = None

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
    #    "/user/{userID}/chamber-of-commerce-excerpt-basic".format(userID=56),
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_chamber_of_commerce_excerpt_basic(client: TestClient):
    """Test case for list_all_chamber_of_commerce_excerpt_basic

    
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
    #    "/chamber-of-commerce-excerpt-basic",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_chamber_of_commerce_excerpt_basic_for_user(client: TestClient):
    """Test case for list_all_chamber_of_commerce_excerpt_basic_for_user

    
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
    #    "/user/{userID}/chamber-of-commerce-excerpt-basic".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

