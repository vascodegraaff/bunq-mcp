# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ginmon_instrument_display import GinmonInstrumentDisplay  # noqa: F401
from openapi_server.models.ginmon_instrument_display_create import GinmonInstrumentDisplayCreate  # noqa: F401
from openapi_server.models.ginmon_instrument_display_listing import GinmonInstrumentDisplayListing  # noqa: F401
from openapi_server.models.ginmon_instrument_display_read import GinmonInstrumentDisplayRead  # noqa: F401
from openapi_server.models.ginmon_instrument_display_update import GinmonInstrumentDisplayUpdate  # noqa: F401


def test_c_reate_ginmon_instrument_display(client: TestClient):
    """Test case for c_reate_ginmon_instrument_display

    
    """
    ginmon_instrument_display = {"dividend_type":"dividend_type","country":"country","ticker":"ticker","url_avatar":"url_avatar","rank_popularity":0,"ratio_total_expense":"ratio_total_expense","description":"description","amount_market_cap":{"currency":"currency","value":"value"},"name_legal":"name_legal","industry":"industry","amount_fund_volume":{"currency":"currency","value":"value"},"issuer":"issuer","url_full_detail":"url_full_detail","name":"name","currency":"currency","category":"category","all_key_information_document":[null,null],"isin":"isin","visibility_type":"visibility_type"}

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
    #    "/ginmon-instrument-display",
    #    headers=headers,
    #    json=ginmon_instrument_display,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_ginmon_instrument_display(client: TestClient):
    """Test case for d_elete_ginmon_instrument_display

    
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
    #    "/ginmon-instrument-display/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_ginmon_instrument_display(client: TestClient):
    """Test case for list_all_ginmon_instrument_display

    
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
    #    "/ginmon-instrument-display",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_ginmon_instrument_display(client: TestClient):
    """Test case for r_ead_ginmon_instrument_display

    
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
    #    "/ginmon-instrument-display/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_ginmon_instrument_display(client: TestClient):
    """Test case for u_pdate_ginmon_instrument_display

    
    """
    ginmon_instrument_display = {"dividend_type":"dividend_type","country":"country","ticker":"ticker","url_avatar":"url_avatar","rank_popularity":0,"ratio_total_expense":"ratio_total_expense","description":"description","amount_market_cap":{"currency":"currency","value":"value"},"name_legal":"name_legal","industry":"industry","amount_fund_volume":{"currency":"currency","value":"value"},"issuer":"issuer","url_full_detail":"url_full_detail","name":"name","currency":"currency","category":"category","all_key_information_document":[null,null],"isin":"isin","visibility_type":"visibility_type"}

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
    #    "/ginmon-instrument-display/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=ginmon_instrument_display,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

