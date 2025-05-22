# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_review_value_identification_document import UserReviewValueIdentificationDocument  # noqa: F401
from openapi_server.models.user_review_value_identification_document_create import UserReviewValueIdentificationDocumentCreate  # noqa: F401
from openapi_server.models.user_review_value_identification_document_update import UserReviewValueIdentificationDocumentUpdate  # noqa: F401


def test_c_reate_value_identification_document_for_user_review_check(client: TestClient):
    """Test case for c_reate_value_identification_document_for_user_review_check

    
    """
    user_review_value_identification_document = {"company_person_id":6,"identification_document":{"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0},"template_url":"template_url","document_description":"document_description","identification_document_id":0,"together_url":"together_url","description":"description","document_type_title":"document_type_title","deny_reason":"deny_reason","document_type":"document_type","status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/value-identification-document".format(userID=56, reviewID=56, checkID=56),
    #    headers=headers,
    #    json=user_review_value_identification_document,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_value_identification_document_for_user_review_check(client: TestClient):
    """Test case for u_pdate_value_identification_document_for_user_review_check

    
    """
    user_review_value_identification_document = {"company_person_id":6,"identification_document":{"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0},"template_url":"template_url","document_description":"document_description","identification_document_id":0,"together_url":"together_url","description":"description","document_type_title":"document_type_title","deny_reason":"deny_reason","document_type":"document_type","status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/value-identification-document/{itemId}".format(userID=56, reviewID=56, checkID=56, itemId=56),
    #    headers=headers,
    #    json=user_review_value_identification_document,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

