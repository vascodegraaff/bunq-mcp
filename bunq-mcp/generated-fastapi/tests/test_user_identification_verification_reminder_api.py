# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.reminder_user_identification_verification import ReminderUserIdentificationVerification  # noqa: F401
from openapi_server.models.reminder_user_identification_verification_create import ReminderUserIdentificationVerificationCreate  # noqa: F401
from openapi_server.models.reminder_user_identification_verification_listing import ReminderUserIdentificationVerificationListing  # noqa: F401
from openapi_server.models.reminder_user_identification_verification_update import ReminderUserIdentificationVerificationUpdate  # noqa: F401


def test_c_reate_user_identification_verification_reminder_for_user(client: TestClient):
    """Test case for c_reate_user_identification_verification_reminder_for_user

    
    """
    reminder_user_identification_verification = {"reminder_time":"reminder_time"}

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
    #    "/user/{userID}/user-identification-verification-reminder".format(userID=56),
    #    headers=headers,
    #    json=reminder_user_identification_verification,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_user_identification_verification_reminder_for_user(client: TestClient):
    """Test case for d_elete_user_identification_verification_reminder_for_user

    
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
    #    "/user/{userID}/user-identification-verification-reminder/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_identification_verification_reminder_for_user(client: TestClient):
    """Test case for list_all_user_identification_verification_reminder_for_user

    
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
    #    "/user/{userID}/user-identification-verification-reminder".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_identification_verification_reminder_for_user(client: TestClient):
    """Test case for u_pdate_user_identification_verification_reminder_for_user

    
    """
    reminder_user_identification_verification = {"reminder_time":"reminder_time"}

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
    #    "/user/{userID}/user-identification-verification-reminder/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=reminder_user_identification_verification,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

