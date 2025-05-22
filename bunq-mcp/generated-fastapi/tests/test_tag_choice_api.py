# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.tag_choice import TagChoice  # noqa: F401
from openapi_server.models.tag_choice_create import TagChoiceCreate  # noqa: F401
from openapi_server.models.tag_choice_read import TagChoiceRead  # noqa: F401
from openapi_server.models.tag_choice_update import TagChoiceUpdate  # noqa: F401


def test_c_reate_tag_choice(client: TestClient):
    """Test case for c_reate_tag_choice

    
    """
    tag_choice = {"tag_type":"tag_type","created":"created","scope":"scope","id":2,"choice":"choice","updated":"updated","status":"status"}

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
    #    "/tag-choice",
    #    headers=headers,
    #    json=tag_choice,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_tag_choice(client: TestClient):
    """Test case for r_ead_tag_choice

    
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
    #    "/tag-choice/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_tag_choice(client: TestClient):
    """Test case for u_pdate_tag_choice

    
    """
    tag_choice = {"tag_type":"tag_type","created":"created","scope":"scope","id":2,"choice":"choice","updated":"updated","status":"status"}

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
    #    "/tag-choice/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=tag_choice,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

