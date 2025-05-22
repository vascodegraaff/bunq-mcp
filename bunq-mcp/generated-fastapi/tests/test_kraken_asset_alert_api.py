# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.kraken_asset_alert import KrakenAssetAlert  # noqa: F401
from openapi_server.models.kraken_asset_alert_create import KrakenAssetAlertCreate  # noqa: F401
from openapi_server.models.kraken_asset_alert_listing import KrakenAssetAlertListing  # noqa: F401
from openapi_server.models.kraken_asset_alert_read import KrakenAssetAlertRead  # noqa: F401
from openapi_server.models.kraken_asset_alert_update import KrakenAssetAlertUpdate  # noqa: F401


def test_c_reate_kraken_asset_alert_for_user_kraken_account(client: TestClient):
    """Test case for c_reate_kraken_asset_alert_for_user_kraken_account

    
    """
    kraken_asset_alert = {"amount_price_alert":{"currency":"currency","value":"value"},"name":"name","type":"type"}

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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-asset-alert".format(userID=56, kraken-accountID=56),
    #    headers=headers,
    #    json=kraken_asset_alert,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_kraken_asset_alert_for_user_kraken_account(client: TestClient):
    """Test case for d_elete_kraken_asset_alert_for_user_kraken_account

    
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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-asset-alert/{itemId}".format(userID=56, kraken-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_kraken_asset_alert_for_user_kraken_account(client: TestClient):
    """Test case for list_all_kraken_asset_alert_for_user_kraken_account

    
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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-asset-alert".format(userID=56, kraken-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_kraken_asset_alert_for_user_kraken_account(client: TestClient):
    """Test case for r_ead_kraken_asset_alert_for_user_kraken_account

    
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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-asset-alert/{itemId}".format(userID=56, kraken-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_kraken_asset_alert_for_user_kraken_account(client: TestClient):
    """Test case for u_pdate_kraken_asset_alert_for_user_kraken_account

    
    """
    kraken_asset_alert = {"amount_price_alert":{"currency":"currency","value":"value"},"name":"name","type":"type"}

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
    #    "/user/{userID}/kraken-account/{kraken-accountID}/kraken-asset-alert/{itemId}".format(userID=56, kraken-accountID=56, itemId=56),
    #    headers=headers,
    #    json=kraken_asset_alert,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

