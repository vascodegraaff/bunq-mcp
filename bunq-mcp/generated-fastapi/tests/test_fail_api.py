# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.identity_verification_report_fail import IdentityVerificationReportFail  # noqa: F401
from openapi_server.models.identity_verification_report_fail_create import IdentityVerificationReportFailCreate  # noqa: F401
from openapi_server.models.user_identification_verification_fail import UserIdentificationVerificationFail  # noqa: F401
from openapi_server.models.user_identification_verification_fail_create import UserIdentificationVerificationFailCreate  # noqa: F401


def test_c_reate_fail_for_user_identification_verification(client: TestClient):
    """Test case for c_reate_fail_for_user_identification_verification

    
    """
    user_identification_verification_fail = {"score":"score","fail_type":"fail_type","source":"source"}

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
    #    "/user/{userID}/identification-verification/{identification-verificationID}/fail".format(userID=56, identification-verificationID=56),
    #    headers=headers,
    #    json=user_identification_verification_fail,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_fail_for_user_identity_verification_report(client: TestClient):
    """Test case for c_reate_fail_for_user_identity_verification_report

    
    """
    identity_verification_report_fail = {"score":"score","source":"source","fail_reason":"fail_reason"}

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
    #    "/user/{userID}/identity-verification-report/{identity-verification-reportID}/fail".format(userID=56, identity-verification-reportID=56),
    #    headers=headers,
    #    json=identity_verification_report_fail,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

