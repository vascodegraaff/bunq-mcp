# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.monetary_account_public import MonetaryAccountPublic  # noqa: F401
from openapi_server.models.monetary_account_public_create import MonetaryAccountPublicCreate  # noqa: F401
from openapi_server.models.monetary_account_public_listing import MonetaryAccountPublicListing  # noqa: F401


def test_c_reate_monetary_account_public(client: TestClient):
    """Test case for c_reate_monetary_account_public

    
    """
    monetary_account_public = {"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}]}

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
    #    "/monetary-account-public",
    #    headers=headers,
    #    json=monetary_account_public,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_monetary_account_public(client: TestClient):
    """Test case for list_all_monetary_account_public

    
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
    #    "/monetary-account-public",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

