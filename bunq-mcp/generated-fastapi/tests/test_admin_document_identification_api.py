# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_document_identification import AdminDocumentIdentification  # noqa: F401
from openapi_server.models.admin_document_identification_create import AdminDocumentIdentificationCreate  # noqa: F401
from openapi_server.models.admin_document_identification_listing import AdminDocumentIdentificationListing  # noqa: F401
from openapi_server.models.admin_document_identification_read import AdminDocumentIdentificationRead  # noqa: F401
from openapi_server.models.admin_document_identification_update import AdminDocumentIdentificationUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_document_identification_for_user(client: TestClient):
    """Test case for c_reate_admin_document_identification_for_user

    
    """
    admin_document_identification = {"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_status":"document_status","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0}

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
    #    "/user/{userID}/admin-document-identification".format(userID=56),
    #    headers=headers,
    #    json=admin_document_identification,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_document_identification_for_user(client: TestClient):
    """Test case for list_all_admin_document_identification_for_user

    
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
    #    "/user/{userID}/admin-document-identification".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_admin_document_identification_for_user(client: TestClient):
    """Test case for r_ead_admin_document_identification_for_user

    
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
    #    "/user/{userID}/admin-document-identification/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_document_identification_for_user(client: TestClient):
    """Test case for u_pdate_admin_document_identification_for_user

    
    """
    admin_document_identification = {"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_status":"document_status","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0}

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
    #    "/user/{userID}/admin-document-identification/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=admin_document_identification,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

