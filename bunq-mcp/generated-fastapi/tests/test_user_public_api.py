# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_public import UserPublic  # noqa: F401
from openapi_server.models.user_public_create import UserPublicCreate  # noqa: F401
from openapi_server.models.user_public_listing import UserPublicListing  # noqa: F401


def test_c_reate_user_public(client: TestClient):
    """Test case for c_reate_user_public

    
    """
    user_public = {"public_uuid":"public_uuid","name":"name","id":0,"avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"}}

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
    #    "/user-public",
    #    headers=headers,
    #    json=user_public,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_user_public(client: TestClient):
    """Test case for list_all_user_public

    
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
    #    "/user-public",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

