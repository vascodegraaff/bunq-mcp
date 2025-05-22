# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_reactivation import UserReactivation  # noqa: F401
from openapi_server.models.user_reactivation_create import UserReactivationCreate  # noqa: F401
from openapi_server.models.user_reactivation_listing import UserReactivationListing  # noqa: F401
from openapi_server.models.user_reactivation_read import UserReactivationRead  # noqa: F401
from openapi_server.models.user_reactivation_update import UserReactivationUpdate  # noqa: F401


def test_c_reate_user_reactivation_for_device(client: TestClient):
    """Test case for c_reate_user_reactivation_for_device

    
    """
    user_reactivation = {"identity_verification_session_id":5,"document_number":"document_number","method":"method","sub_status":"sub_status","document_back_attachment_id":1,"user_label":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"type":"type","document_front_attachment_id":6,"user_uuid":"user_uuid","url_referrer":"url_referrer","document_country_of_issuance":"document_country_of_issuance","alias":{"service":"service","name":"name","type":"type","value":"value"},"user_identification_verification_id":5,"document_type":"document_type","status":"status"}

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
    #    "/device/{deviceID}/user-reactivation".format(deviceID=56),
    #    headers=headers,
    #    json=user_reactivation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_reactivation_for_device(client: TestClient):
    """Test case for list_all_user_reactivation_for_device

    
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
    #    "/device/{deviceID}/user-reactivation".format(deviceID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_user_reactivation_for_device(client: TestClient):
    """Test case for r_ead_user_reactivation_for_device

    
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
    #    "/device/{deviceID}/user-reactivation/{itemId}".format(deviceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_reactivation_for_device(client: TestClient):
    """Test case for u_pdate_user_reactivation_for_device

    
    """
    user_reactivation = {"identity_verification_session_id":5,"document_number":"document_number","method":"method","sub_status":"sub_status","document_back_attachment_id":1,"user_label":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"type":"type","document_front_attachment_id":6,"user_uuid":"user_uuid","url_referrer":"url_referrer","document_country_of_issuance":"document_country_of_issuance","alias":{"service":"service","name":"name","type":"type","value":"value"},"user_identification_verification_id":5,"document_type":"document_type","status":"status"}

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
    #    "/device/{deviceID}/user-reactivation/{itemId}".format(deviceID=56, itemId=56),
    #    headers=headers,
    #    json=user_reactivation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

