# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.apple_pay_provision import ApplePayProvision  # noqa: F401
from openapi_server.models.apple_pay_provision_create import ApplePayProvisionCreate  # noqa: F401
from openapi_server.models.apple_pay_provision_listing import ApplePayProvisionListing  # noqa: F401
from openapi_server.models.apple_pay_provision_update import ApplePayProvisionUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_apple_pay_provision_for_user_card(client: TestClient):
    """Test case for c_reate_apple_pay_provision_for_user_card

    
    """
    apple_pay_provision = {"public_certificates":["public_certificates","public_certificates"],"nonce_signature":"nonce_signature","nonce":"nonce","status":"status"}

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
    #    "/user/{userID}/card/{cardID}/apple-pay-provision".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=apple_pay_provision,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_apple_pay_provision_for_user_card(client: TestClient):
    """Test case for list_all_apple_pay_provision_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/apple-pay-provision".format(userID=56, cardID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_apple_pay_provision_for_user_card(client: TestClient):
    """Test case for u_pdate_apple_pay_provision_for_user_card

    
    """
    apple_pay_provision = {"public_certificates":["public_certificates","public_certificates"],"nonce_signature":"nonce_signature","nonce":"nonce","status":"status"}

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
    #    "/user/{userID}/card/{cardID}/apple-pay-provision/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #    json=apple_pay_provision,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

