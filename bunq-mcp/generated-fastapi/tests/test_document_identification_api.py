# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.document_identification import DocumentIdentification  # noqa: F401
from openapi_server.models.document_identification_create import DocumentIdentificationCreate  # noqa: F401
from openapi_server.models.document_identification_listing import DocumentIdentificationListing  # noqa: F401


def test_c_reate_document_identification_for_user(client: TestClient):
    """Test case for c_reate_document_identification_for_user

    
    """
    document_identification = {"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0}

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
    #    "/user/{userID}/document-identification".format(userID=56),
    #    headers=headers,
    #    json=document_identification,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_document_identification_for_user(client: TestClient):
    """Test case for list_all_document_identification_for_user

    
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
    #    "/user/{userID}/document-identification".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

