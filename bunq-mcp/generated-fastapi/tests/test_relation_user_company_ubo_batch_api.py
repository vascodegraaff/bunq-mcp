# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.relation_user_company_ubo_batch import RelationUserCompanyUboBatch  # noqa: F401
from openapi_server.models.relation_user_company_ubo_batch_create import RelationUserCompanyUboBatchCreate  # noqa: F401


def test_c_reate_relation_user_company_ubo_batch_for_user_company(client: TestClient):
    """Test case for c_reate_relation_user_company_ubo_batch_for_user_company

    
    """
    relation_user_company_ubo_batch = {"all_relation_user_company_ubo":[{"document_number":"document_number","document_issuing_authority":"document_issuing_authority","date_of_birth":"date_of_birth","document_back_attachment_id":6,"last_name":"last_name","middle_name":"middle_name","tax_resident":[{"country":"country","tax_number":"tax_number","id":0,"status":"status"},{"country":"country","tax_number":"tax_number","id":0,"status":"status"}],"remove_old_ubos":1,"document_front_attachment_id":0,"document_expiry_date":"document_expiry_date","nationality":"nationality","document_country_of_issuance":"document_country_of_issuance","pointer_director":{"service":"service","name":"name","type":"type","value":"value"},"first_name":"first_name","document_type":"document_type","status":"status"},{"document_number":"document_number","document_issuing_authority":"document_issuing_authority","date_of_birth":"date_of_birth","document_back_attachment_id":6,"last_name":"last_name","middle_name":"middle_name","tax_resident":[{"country":"country","tax_number":"tax_number","id":0,"status":"status"},{"country":"country","tax_number":"tax_number","id":0,"status":"status"}],"remove_old_ubos":1,"document_front_attachment_id":0,"document_expiry_date":"document_expiry_date","nationality":"nationality","document_country_of_issuance":"document_country_of_issuance","pointer_director":{"service":"service","name":"name","type":"type","value":"value"},"first_name":"first_name","document_type":"document_type","status":"status"}]}

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
    #    "/user-company/{user-companyID}/relation-user-company-ubo-batch".format(user-companyID=56),
    #    headers=headers,
    #    json=relation_user_company_ubo_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

