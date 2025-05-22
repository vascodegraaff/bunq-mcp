# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_information_inquiry_entry import UserInformationInquiryEntry  # noqa: F401
from openapi_server.models.user_information_inquiry_entry_read import UserInformationInquiryEntryRead  # noqa: F401
from openapi_server.models.user_information_inquiry_entry_update import UserInformationInquiryEntryUpdate  # noqa: F401


def test_r_ead_entry_for_user_user_information_inquiry(client: TestClient):
    """Test case for r_ead_entry_for_user_user_information_inquiry

    
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
    #    "/user/{userID}/user-information-inquiry/{user-information-inquiryID}/entry/{itemId}".format(userID=56, user-information-inquiryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_entry_for_user_user_information_inquiry(client: TestClient):
    """Test case for u_pdate_entry_for_user_user_information_inquiry

    
    """
    user_information_inquiry_entry = {"reject_reason":"reject_reason","status":"status"}

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
    #    "/user/{userID}/user-information-inquiry/{user-information-inquiryID}/entry/{itemId}".format(userID=56, user-information-inquiryID=56, itemId=56),
    #    headers=headers,
    #    json=user_information_inquiry_entry,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

