# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_generated_cvc2 import CardGeneratedCvc2  # noqa: F401
from openapi_server.models.card_generated_cvc2_create import CardGeneratedCvc2Create  # noqa: F401
from openapi_server.models.card_generated_cvc2_listing import CardGeneratedCvc2Listing  # noqa: F401
from openapi_server.models.card_generated_cvc2_read import CardGeneratedCvc2Read  # noqa: F401
from openapi_server.models.card_generated_cvc2_update import CardGeneratedCvc2Update  # noqa: F401


def test_c_reate_generated_cvc2_for_user_card(client: TestClient):
    """Test case for c_reate_generated_cvc2_for_user_card

    
    """
    card_generated_cvc2 = {"created":"created","id":8,"type":"type","cvc2":"cvc2","expiry_time":"expiry_time","updated":"updated","status":"status"}

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
    #    "/user/{userID}/card/{cardID}/generated-cvc2".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=card_generated_cvc2,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_generated_cvc2_for_user_card(client: TestClient):
    """Test case for list_all_generated_cvc2_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/generated-cvc2".format(userID=56, cardID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_generated_cvc2_for_user_card(client: TestClient):
    """Test case for r_ead_generated_cvc2_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/generated-cvc2/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_generated_cvc2_for_user_card(client: TestClient):
    """Test case for u_pdate_generated_cvc2_for_user_card

    
    """
    card_generated_cvc2 = {"created":"created","id":8,"type":"type","cvc2":"cvc2","expiry_time":"expiry_time","updated":"updated","status":"status"}

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
    #    "/user/{userID}/card/{cardID}/generated-cvc2/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #    json=card_generated_cvc2,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

