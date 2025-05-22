# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_qr_code_content import BunqMeFundraiserProfileQrCodeContent  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_qr_code_content_create import BunqMeFundraiserProfileQrCodeContentCreate  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_qr_code_content_read import BunqMeFundraiserProfileQrCodeContentRead  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_bunq_qr_code_content_create import BunqMeMerchantRequestBunqQrCodeContentCreate  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_bunq_qr_code_content_read import BunqMeMerchantRequestBunqQrCodeContentRead  # noqa: F401
from openapi_server.models.bunq_me_tab_entry_qr_code_content_create import BunqMeTabEntryQrCodeContentCreate  # noqa: F401
from openapi_server.models.bunq_me_tab_entry_qr_code_content_read import BunqMeTabEntryQrCodeContentRead  # noqa: F401
from openapi_server.models.bunq_to_entry_qr_code_content_listing import BunqToEntryQrCodeContentListing  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reateqr_code_content_for_bunqme_fundraiser_profile(client: TestClient):
    """Test case for c_reateqr_code_content_for_bunqme_fundraiser_profile

    
    """
    bunq_me_fundraiser_profile_qr_code_content = {"amount":{"currency":"currency","value":"value"},"description":"description"}

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
    #    "/bunqme-fundraiser-profile/{bunqme-fundraiser-profileUUID}/qr-code-content".format(bunqme-fundraiser-profileUUID='bunqme_fundraiser_profile_uuid_example'),
    #    headers=headers,
    #    json=bunq_me_fundraiser_profile_qr_code_content,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reateqr_code_content_for_bunqme_merchant_request(client: TestClient):
    """Test case for c_reateqr_code_content_for_bunqme_merchant_request

    
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
    #    "/bunqme-merchant-request/{bunqme-merchant-requestUUID}/qr-code-content".format(bunqme-merchant-requestUUID='bunqme_merchant_request_uuid_example'),
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reateqr_code_content_for_bunqme_tab_entry(client: TestClient):
    """Test case for c_reateqr_code_content_for_bunqme_tab_entry

    
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
    #    "/bunqme-tab-entry/{bunqme-tab-entryUUID}/qr-code-content".format(bunqme-tab-entryUUID='bunqme_tab_entry_uuid_example'),
    #    headers=headers,
    #    json=body,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_qr_code_content_for_bunqto_entry(client: TestClient):
    """Test case for list_all_qr_code_content_for_bunqto_entry

    
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
    #    "/bunqto-entry/{bunqto-entryUUID}/qr-code-content".format(bunqto-entryUUID='bunqto_entry_uuid_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_eadqr_code_content_for_bunqme_fundraiser_profile(client: TestClient):
    """Test case for r_eadqr_code_content_for_bunqme_fundraiser_profile

    
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
    #    "/bunqme-fundraiser-profile/{bunqme-fundraiser-profileUUID}/qr-code-content/{itemId}".format(bunqme-fundraiser-profileUUID='bunqme_fundraiser_profile_uuid_example', itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_eadqr_code_content_for_bunqme_merchant_request(client: TestClient):
    """Test case for r_eadqr_code_content_for_bunqme_merchant_request

    
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
    #    "/bunqme-merchant-request/{bunqme-merchant-requestUUID}/qr-code-content/{itemId}".format(bunqme-merchant-requestUUID='bunqme_merchant_request_uuid_example', itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_eadqr_code_content_for_bunqme_tab_entry(client: TestClient):
    """Test case for r_eadqr_code_content_for_bunqme_tab_entry

    
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
    #    "/bunqme-tab-entry/{bunqme-tab-entryUUID}/qr-code-content/{itemId}".format(bunqme-tab-entryUUID='bunqme_tab_entry_uuid_example', itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

