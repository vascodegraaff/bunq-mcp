# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.kraken_account_agreement_document_batch import KrakenAccountAgreementDocumentBatch  # noqa: F401
from openapi_server.models.kraken_account_agreement_document_batch_create import KrakenAccountAgreementDocumentBatchCreate  # noqa: F401


def test_c_reate_kraken_account_agreement_document_batch_for_user(client: TestClient):
    """Test case for c_reate_kraken_account_agreement_document_batch_for_user

    
    """
    kraken_account_agreement_document_batch = {"all_agreement_document":[{"document_country":"document_country","document_id":"document_id","document_url":"document_url","document_type":"document_type"},{"document_country":"document_country","document_id":"document_id","document_url":"document_url","document_type":"document_type"}]}

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
    #    "/user/{userID}/kraken-account-agreement-document-batch".format(userID=56),
    #    headers=headers,
    #    json=kraken_account_agreement_document_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

