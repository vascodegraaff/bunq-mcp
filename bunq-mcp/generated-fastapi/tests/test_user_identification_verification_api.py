# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_identification_verification_public import UserIdentificationVerificationPublic  # noqa: F401
from openapi_server.models.user_identification_verification_public_read import UserIdentificationVerificationPublicRead  # noqa: F401
from openapi_server.models.user_identification_verification_public_update import UserIdentificationVerificationPublicUpdate  # noqa: F401


def test_r_ead_user_identification_verification_for_device(client: TestClient):
    """Test case for r_ead_user_identification_verification_for_device

    
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
    #    "/device/{deviceID}/user-identification-verification/{itemId}".format(deviceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_identification_verification_for_device(client: TestClient):
    """Test case for u_pdate_user_identification_verification_for_device

    
    """
    user_identification_verification_public = {"user_uuid":"user_uuid","alias":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"}

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
    #    "/device/{deviceID}/user-identification-verification/{itemId}".format(deviceID=56, itemId=56),
    #    headers=headers,
    #    json=user_identification_verification_public,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

