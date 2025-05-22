# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_result_listing import TransactionMonitoringMachineLearningResultListing  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_result_read import TransactionMonitoringMachineLearningResultRead  # noqa: F401


def test_list_all_transaction_monitoring_machine_learning_result_for_transaction_monitoring_metadata(client: TestClient):
    """Test case for list_all_transaction_monitoring_machine_learning_result_for_transaction_monitoring_metadata

    
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
    #    "/transaction-monitoring-metadata/{transaction-monitoring-metadataID}/transaction-monitoring-machine-learning-result".format(transaction-monitoring-metadataID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transaction_monitoring_machine_learning_result_for_transaction_monitoring_metadata(client: TestClient):
    """Test case for r_ead_transaction_monitoring_machine_learning_result_for_transaction_monitoring_metadata

    
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
    #    "/transaction-monitoring-metadata/{transaction-monitoring-metadataID}/transaction-monitoring-machine-learning-result/{itemId}".format(transaction-monitoring-metadataID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

