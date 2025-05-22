# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.kraken_asset_display import KrakenAssetDisplay  # noqa: F401
from openapi_server.models.kraken_asset_display_create import KrakenAssetDisplayCreate  # noqa: F401
from openapi_server.models.kraken_asset_display_listing import KrakenAssetDisplayListing  # noqa: F401
from openapi_server.models.kraken_asset_display_read import KrakenAssetDisplayRead  # noqa: F401
from openapi_server.models.kraken_asset_display_update import KrakenAssetDisplayUpdate  # noqa: F401


def test_c_reate_kraken_asset_display(client: TestClient):
    """Test case for c_reate_kraken_asset_display

    
    """
    kraken_asset_display = {"identifier":"identifier","url_avatar":"url_avatar","full_name":"full_name","rank_popularity":0,"description":["description","description"],"spread":"spread","visibility_type":"visibility_type"}

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
    #    "/kraken-asset-display",
    #    headers=headers,
    #    json=kraken_asset_display,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_kraken_asset_display(client: TestClient):
    """Test case for list_all_kraken_asset_display

    
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
    #    "/kraken-asset-display",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_kraken_asset_display(client: TestClient):
    """Test case for r_ead_kraken_asset_display

    
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
    #    "/kraken-asset-display/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_kraken_asset_display(client: TestClient):
    """Test case for u_pdate_kraken_asset_display

    
    """
    kraken_asset_display = {"identifier":"identifier","url_avatar":"url_avatar","full_name":"full_name","rank_popularity":0,"description":["description","description"],"spread":"spread","visibility_type":"visibility_type"}

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
    #    "/kraken-asset-display/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=kraken_asset_display,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

