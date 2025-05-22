# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.google_pay_provision import GooglePayProvision  # noqa: F401
from openapi_server.models.google_pay_provision_create import GooglePayProvisionCreate  # noqa: F401
from openapi_server.models.google_pay_provision_listing import GooglePayProvisionListing  # noqa: F401
from openapi_server.models.google_pay_provision_update import GooglePayProvisionUpdate  # noqa: F401


def test_c_reate_google_pay_provision_for_user_card(client: TestClient):
    """Test case for c_reate_google_pay_provision_for_user_card

    
    """
    google_pay_provision = {"status":"status"}

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
    #    "/user/{userID}/card/{cardID}/google-pay-provision".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=google_pay_provision,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_google_pay_provision_for_user_card(client: TestClient):
    """Test case for list_all_google_pay_provision_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/google-pay-provision".format(userID=56, cardID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_google_pay_provision_for_user_card(client: TestClient):
    """Test case for u_pdate_google_pay_provision_for_user_card

    
    """
    google_pay_provision = {"status":"status"}

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
    #    "/user/{userID}/card/{cardID}/google-pay-provision/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #    json=google_pay_provision,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

