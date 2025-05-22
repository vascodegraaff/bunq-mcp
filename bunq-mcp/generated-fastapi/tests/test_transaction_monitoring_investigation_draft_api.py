# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_draft import TransactionMonitoringInvestigationDraft  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_draft_listing import TransactionMonitoringInvestigationDraftListing  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_draft_read import TransactionMonitoringInvestigationDraftRead  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_draft_update import TransactionMonitoringInvestigationDraftUpdate  # noqa: F401


def test_list_all_transaction_monitoring_investigation_draft(client: TestClient):
    """Test case for list_all_transaction_monitoring_investigation_draft

    
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
    #    "/transaction-monitoring-investigation-draft",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transaction_monitoring_investigation_draft(client: TestClient):
    """Test case for r_ead_transaction_monitoring_investigation_draft

    
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
    #    "/transaction-monitoring-investigation-draft/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_transaction_monitoring_investigation_draft(client: TestClient):
    """Test case for u_pdate_transaction_monitoring_investigation_draft

    
    """
    transaction_monitoring_investigation_draft = {"feedback_content":"feedback_content","all_feedback":["all_feedback","all_feedback"],"investigation_id":0,"status":"status"}

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
    #    "/transaction-monitoring-investigation-draft/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=transaction_monitoring_investigation_draft,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

