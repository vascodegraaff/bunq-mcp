# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation import TransactionMonitoringInvestigation  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_create import TransactionMonitoringInvestigationCreate  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_listing import TransactionMonitoringInvestigationListing  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_read import TransactionMonitoringInvestigationRead  # noqa: F401
from openapi_server.models.transaction_monitoring_investigation_update import TransactionMonitoringInvestigationUpdate  # noqa: F401


def test_c_reate_transaction_monitoring_investigation(client: TestClient):
    """Test case for c_reate_transaction_monitoring_investigation

    
    """
    transaction_monitoring_investigation = {"external_url":"external_url","user_id":0,"metadata_status":"metadata_status","investigation_status":"investigation_status","description":"description"}

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
    #    "/transaction-monitoring-investigation",
    #    headers=headers,
    #    json=transaction_monitoring_investigation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_transaction_monitoring_investigation(client: TestClient):
    """Test case for list_all_transaction_monitoring_investigation

    
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
    #    "/transaction-monitoring-investigation",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transaction_monitoring_investigation(client: TestClient):
    """Test case for r_ead_transaction_monitoring_investigation

    
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
    #    "/transaction-monitoring-investigation/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_transaction_monitoring_investigation(client: TestClient):
    """Test case for u_pdate_transaction_monitoring_investigation

    
    """
    transaction_monitoring_investigation = {"external_url":"external_url","user_id":0,"metadata_status":"metadata_status","investigation_status":"investigation_status","description":"description"}

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
    #    "/transaction-monitoring-investigation/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=transaction_monitoring_investigation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

