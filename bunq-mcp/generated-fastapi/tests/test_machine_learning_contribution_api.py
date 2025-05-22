# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.machine_learning_contribution import MachineLearningContribution  # noqa: F401
from openapi_server.models.machine_learning_contribution_listing import MachineLearningContributionListing  # noqa: F401
from openapi_server.models.machine_learning_contribution_read import MachineLearningContributionRead  # noqa: F401
from openapi_server.models.machine_learning_contribution_update import MachineLearningContributionUpdate  # noqa: F401


def test_list_all_machine_learning_contribution(client: TestClient):
    """Test case for list_all_machine_learning_contribution

    
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
    #    "/machine-learning-contribution",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_machine_learning_contribution(client: TestClient):
    """Test case for r_ead_machine_learning_contribution

    
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
    #    "/machine-learning-contribution/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_machine_learning_contribution(client: TestClient):
    """Test case for u_pdate_machine_learning_contribution

    
    """
    machine_learning_contribution = {"explanation_content_quality":"explanation_content_quality"}

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
    #    "/machine-learning-contribution/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=machine_learning_contribution,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

