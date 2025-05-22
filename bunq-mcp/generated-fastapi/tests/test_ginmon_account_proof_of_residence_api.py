# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.ginmon_account_proof_of_residence import GinmonAccountProofOfResidence  # noqa: F401
from openapi_server.models.ginmon_account_proof_of_residence_create import GinmonAccountProofOfResidenceCreate  # noqa: F401
from openapi_server.models.ginmon_account_proof_of_residence_listing import GinmonAccountProofOfResidenceListing  # noqa: F401


def test_c_reate_ginmon_account_proof_of_residence_for_user_ginmon_account(client: TestClient):
    """Test case for c_reate_ginmon_account_proof_of_residence_for_user_ginmon_account

    
    """
    ginmon_account_proof_of_residence = {"residence_document_attachment_id":0,"residence_document_type":"residence_document_type","residence_document_issue_date":"residence_document_issue_date"}

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
    #    "/user/{userID}/ginmon-account/{ginmon-accountID}/ginmon-account-proof-of-residence".format(userID=56, ginmon-accountID=56),
    #    headers=headers,
    #    json=ginmon_account_proof_of_residence,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_ginmon_account_proof_of_residence_for_user_ginmon_account(client: TestClient):
    """Test case for list_all_ginmon_account_proof_of_residence_for_user_ginmon_account

    
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
    #    "/user/{userID}/ginmon-account/{ginmon-accountID}/ginmon-account-proof-of-residence".format(userID=56, ginmon-accountID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

