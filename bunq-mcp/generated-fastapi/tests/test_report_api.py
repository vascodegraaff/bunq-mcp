# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.birdee_customer_report_listing import BirdeeCustomerReportListing  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_report_create import BunqMeFundraiserProfileReportCreate  # noqa: F401
from openapi_server.models.bunq_me_request_report_create import BunqMeRequestReportCreate  # noqa: F401
from openapi_server.models.bunq_me_tab_entry_report_create import BunqMeTabEntryReportCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.fiu_report_listing import FiuReportListing  # noqa: F401


def test_c_reate_report_for_bunqme_fundraiser_profile(client: TestClient):
    """Test case for c_reate_report_for_bunqme_fundraiser_profile

    
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
    #    "/bunqme-fundraiser-profile/{bunqme-fundraiser-profileUUID}/report".format(bunqme-fundraiser-profileUUID='bunqme_fundraiser_profile_uuid_example'),
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_report_for_bunqme_request(client: TestClient):
    """Test case for c_reate_report_for_bunqme_request

    
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
    #    "/bunqme-request/{bunqme-requestUUID}/report".format(bunqme-requestUUID='bunqme_request_uuid_example'),
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_report_for_bunqme_tab_entry(client: TestClient):
    """Test case for c_reate_report_for_bunqme_tab_entry

    
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
    #    "/bunqme-tab-entry/{bunqme-tab-entryUUID}/report".format(bunqme-tab-entryUUID='bunqme_tab_entry_uuid_example'),
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_report_for_user_birdee_customer(client: TestClient):
    """Test case for list_all_report_for_user_birdee_customer

    
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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/report".format(userID=56, birdee-customerID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_report_for_user_fiu_report_batch(client: TestClient):
    """Test case for list_all_report_for_user_fiu_report_batch

    
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
    #    "/user/{userID}/fiu-report-batch/{fiu-report-batchID}/report".format(userID=56, fiu-report-batchID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

