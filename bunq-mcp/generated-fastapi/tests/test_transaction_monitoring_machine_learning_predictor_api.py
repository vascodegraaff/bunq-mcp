# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_predictor import TransactionMonitoringMachineLearningPredictor  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_predictor_create import TransactionMonitoringMachineLearningPredictorCreate  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_predictor_listing import TransactionMonitoringMachineLearningPredictorListing  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_predictor_read import TransactionMonitoringMachineLearningPredictorRead  # noqa: F401
from openapi_server.models.transaction_monitoring_machine_learning_predictor_update import TransactionMonitoringMachineLearningPredictorUpdate  # noqa: F401


def test_c_reate_transaction_monitoring_machine_learning_predictor(client: TestClient):
    """Test case for c_reate_transaction_monitoring_machine_learning_predictor

    
    """
    transaction_monitoring_machine_learning_predictor = {"status_deployment":"status_deployment","name":"name","status_reporting":"status_reporting","transaction_direction":"transaction_direction","risk_indicator":"risk_indicator","threshold":0,"transaction_account_type":"transaction_account_type"}

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
    #    "/transaction-monitoring-machine-learning-predictor",
    #    headers=headers,
    #    json=transaction_monitoring_machine_learning_predictor,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_transaction_monitoring_machine_learning_predictor(client: TestClient):
    """Test case for list_all_transaction_monitoring_machine_learning_predictor

    
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
    #    "/transaction-monitoring-machine-learning-predictor",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transaction_monitoring_machine_learning_predictor(client: TestClient):
    """Test case for r_ead_transaction_monitoring_machine_learning_predictor

    
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
    #    "/transaction-monitoring-machine-learning-predictor/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_transaction_monitoring_machine_learning_predictor(client: TestClient):
    """Test case for u_pdate_transaction_monitoring_machine_learning_predictor

    
    """
    transaction_monitoring_machine_learning_predictor = {"status_deployment":"status_deployment","name":"name","status_reporting":"status_reporting","transaction_direction":"transaction_direction","risk_indicator":"risk_indicator","threshold":0,"transaction_account_type":"transaction_account_type"}

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
    #    "/transaction-monitoring-machine-learning-predictor/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=transaction_monitoring_machine_learning_predictor,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

