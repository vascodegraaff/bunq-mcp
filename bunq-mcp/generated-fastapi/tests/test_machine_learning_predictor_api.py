# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.machine_learning_predictor import MachineLearningPredictor  # noqa: F401
from openapi_server.models.machine_learning_predictor_create import MachineLearningPredictorCreate  # noqa: F401
from openapi_server.models.machine_learning_predictor_listing import MachineLearningPredictorListing  # noqa: F401
from openapi_server.models.machine_learning_predictor_read import MachineLearningPredictorRead  # noqa: F401
from openapi_server.models.machine_learning_predictor_update import MachineLearningPredictorUpdate  # noqa: F401


def test_c_reate_machine_learning_predictor(client: TestClient):
    """Test case for c_reate_machine_learning_predictor

    
    """
    machine_learning_predictor = {"application":"application","predictor_name":"predictor_name","threshold":0,"type":"type","status":"status"}

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
    #    "/machine-learning-predictor",
    #    headers=headers,
    #    json=machine_learning_predictor,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_machine_learning_predictor(client: TestClient):
    """Test case for list_all_machine_learning_predictor

    
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
    #    "/machine-learning-predictor",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_machine_learning_predictor(client: TestClient):
    """Test case for r_ead_machine_learning_predictor

    
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
    #    "/machine-learning-predictor/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_machine_learning_predictor(client: TestClient):
    """Test case for u_pdate_machine_learning_predictor

    
    """
    machine_learning_predictor = {"application":"application","predictor_name":"predictor_name","threshold":0,"type":"type","status":"status"}

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
    #    "/machine-learning-predictor/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=machine_learning_predictor,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

