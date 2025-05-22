# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.identity_verification_session import IdentityVerificationSession  # noqa: F401
from openapi_server.models.identity_verification_session_create import IdentityVerificationSessionCreate  # noqa: F401
from openapi_server.models.identity_verification_session_listing import IdentityVerificationSessionListing  # noqa: F401
from openapi_server.models.identity_verification_session_public import IdentityVerificationSessionPublic  # noqa: F401
from openapi_server.models.identity_verification_session_public_read import IdentityVerificationSessionPublicRead  # noqa: F401
from openapi_server.models.identity_verification_session_public_update import IdentityVerificationSessionPublicUpdate  # noqa: F401
from openapi_server.models.identity_verification_session_read import IdentityVerificationSessionRead  # noqa: F401
from openapi_server.models.identity_verification_session_update import IdentityVerificationSessionUpdate  # noqa: F401


def test_c_reate_identity_verification_session_for_user(client: TestClient):
    """Test case for c_reate_identity_verification_session_for_user

    
    """
    identity_verification_session = {"purpose":"purpose","url_referrer":"url_referrer","status":"status"}

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
    #    "/user/{userID}/identity-verification-session".format(userID=56),
    #    headers=headers,
    #    json=identity_verification_session,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_identity_verification_session_for_user(client: TestClient):
    """Test case for list_all_identity_verification_session_for_user

    
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
    #    "/user/{userID}/identity-verification-session".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_identity_verification_session_for_device(client: TestClient):
    """Test case for r_ead_identity_verification_session_for_device

    
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
    #    "/device/{deviceID}/identity-verification-session/{itemId}".format(deviceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_identity_verification_session_for_user(client: TestClient):
    """Test case for r_ead_identity_verification_session_for_user

    
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
    #    "/user/{userID}/identity-verification-session/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_identity_verification_session_for_device(client: TestClient):
    """Test case for u_pdate_identity_verification_session_for_device

    
    """
    identity_verification_session_public = {"alias":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"}

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
    #    "/device/{deviceID}/identity-verification-session/{itemId}".format(deviceID=56, itemId=56),
    #    headers=headers,
    #    json=identity_verification_session_public,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_identity_verification_session_for_user(client: TestClient):
    """Test case for u_pdate_identity_verification_session_for_user

    
    """
    identity_verification_session = {"purpose":"purpose","url_referrer":"url_referrer","status":"status"}

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
    #    "/user/{userID}/identity-verification-session/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=identity_verification_session,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

