# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.birdee_customer_document import BirdeeCustomerDocument  # noqa: F401
from openapi_server.models.birdee_customer_document_create import BirdeeCustomerDocumentCreate  # noqa: F401
from openapi_server.models.birdee_customer_document_listing import BirdeeCustomerDocumentListing  # noqa: F401
from openapi_server.models.birdee_customer_document_read import BirdeeCustomerDocumentRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_identification_verification_document import UserIdentificationVerificationDocument  # noqa: F401
from openapi_server.models.user_identification_verification_document_create import UserIdentificationVerificationDocumentCreate  # noqa: F401
from openapi_server.models.user_identification_verification_document_listing import UserIdentificationVerificationDocumentListing  # noqa: F401


def test_c_reate_document_for_user_birdee_customer(client: TestClient):
    """Test case for c_reate_document_for_user_birdee_customer

    
    """
    birdee_customer_document = {"expiry_date":"expiry_date","attachment_id":0,"document_type":"document_type"}

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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/document".format(userID=56, birdee-customerID=56),
    #    headers=headers,
    #    json=birdee_customer_document,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_document_for_user_identification_verification(client: TestClient):
    """Test case for c_reate_document_for_user_identification_verification

    
    """
    user_identification_verification_document = {"document_id":"document_id","type":"type"}

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
    #    "/user/{userID}/identification-verification/{identification-verificationID}/document".format(userID=56, identification-verificationID=56),
    #    headers=headers,
    #    json=user_identification_verification_document,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_document_for_user_birdee_customer(client: TestClient):
    """Test case for list_all_document_for_user_birdee_customer

    
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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/document".format(userID=56, birdee-customerID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_document_for_user_identification_verification(client: TestClient):
    """Test case for list_all_document_for_user_identification_verification

    
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
    #    "/user/{userID}/identification-verification/{identification-verificationID}/document".format(userID=56, identification-verificationID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_document_for_user_birdee_customer(client: TestClient):
    """Test case for r_ead_document_for_user_birdee_customer

    
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
    #    "/user/{userID}/birdee-customer/{birdee-customerID}/document/{itemId}".format(userID=56, birdee-customerID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

