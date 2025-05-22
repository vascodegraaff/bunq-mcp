# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_review_value_company_person import UserReviewValueCompanyPerson  # noqa: F401
from openapi_server.models.user_review_value_company_person_create import UserReviewValueCompanyPersonCreate  # noqa: F401
from openapi_server.models.user_review_value_company_person_update import UserReviewValueCompanyPersonUpdate  # noqa: F401


def test_c_reate_value_company_person_for_user_review_check(client: TestClient):
    """Test case for c_reate_value_company_person_for_user_review_check

    
    """
    user_review_value_company_person = {"company_person_id":0,"identification_document":{"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0},"created":"created","identification_document_id":6,"id":1,"updated":"updated","label_company_person":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/value-company-person".format(userID=56, reviewID=56, checkID=56),
    #    headers=headers,
    #    json=user_review_value_company_person,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_value_company_person_for_user_review_check(client: TestClient):
    """Test case for u_pdate_value_company_person_for_user_review_check

    
    """
    user_review_value_company_person = {"company_person_id":0,"identification_document":{"document_expiry_date":"document_expiry_date","document_number":"document_number","document_issuing_authority":"document_issuing_authority","document_back_attachment_id":6,"document_country_of_issuance":"document_country_of_issuance","document_type":"document_type","document_attachment_id":0},"created":"created","identification_document_id":6,"id":1,"updated":"updated","label_company_person":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"status":"status"}

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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/value-company-person/{itemId}".format(userID=56, reviewID=56, checkID=56, itemId=56),
    #    headers=headers,
    #    json=user_review_value_company_person,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

