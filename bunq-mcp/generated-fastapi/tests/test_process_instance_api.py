# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.process_instance import ProcessInstance  # noqa: F401
from openapi_server.models.process_instance_create import ProcessInstanceCreate  # noqa: F401
from openapi_server.models.process_instance_read import ProcessInstanceRead  # noqa: F401
from openapi_server.models.process_instance_update import ProcessInstanceUpdate  # noqa: F401


def test_c_reate_process_instance(client: TestClient):
    """Test case for c_reate_process_instance

    
    """
    process_instance = {"user_inputs":["user_inputs","user_inputs"],"process_name":"process_name","external_model_id":6,"deadline":"deadline","user_owner_id":0,"status":"status"}

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
    #    "/process-instance",
    #    headers=headers,
    #    json=process_instance,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_process_instance(client: TestClient):
    """Test case for r_ead_process_instance

    
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
    #    "/process-instance/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_process_instance(client: TestClient):
    """Test case for u_pdate_process_instance

    
    """
    process_instance = {"user_inputs":["user_inputs","user_inputs"],"process_name":"process_name","external_model_id":6,"deadline":"deadline","user_owner_id":0,"status":"status"}

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
    #    "/process-instance/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=process_instance,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

