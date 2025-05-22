# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.process_definition import ProcessDefinition  # noqa: F401
from openapi_server.models.process_definition_create import ProcessDefinitionCreate  # noqa: F401
from openapi_server.models.process_definition_listing import ProcessDefinitionListing  # noqa: F401
from openapi_server.models.process_definition_read import ProcessDefinitionRead  # noqa: F401
from openapi_server.models.process_definition_update import ProcessDefinitionUpdate  # noqa: F401


def test_c_reate_process_definition(client: TestClient):
    """Test case for c_reate_process_definition

    
    """
    process_definition = {"blueprint":"blueprint","user_backup_id":6,"process_name":"process_name","executor_group_id":1,"category":"category","user_owner_id":0}

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
    #    "/process-definition",
    #    headers=headers,
    #    json=process_definition,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_process_definition(client: TestClient):
    """Test case for list_all_process_definition

    
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
    #    "/process-definition",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_process_definition(client: TestClient):
    """Test case for r_ead_process_definition

    
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
    #    "/process-definition/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_process_definition(client: TestClient):
    """Test case for u_pdate_process_definition

    
    """
    process_definition = {"blueprint":"blueprint","user_backup_id":6,"process_name":"process_name","executor_group_id":1,"category":"category","user_owner_id":0}

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
    #    "/process-definition/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=process_definition,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

