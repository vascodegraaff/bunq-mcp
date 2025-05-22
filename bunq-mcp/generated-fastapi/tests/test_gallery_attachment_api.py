# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.registry_gallery_attachment import RegistryGalleryAttachment  # noqa: F401
from openapi_server.models.registry_gallery_attachment_create import RegistryGalleryAttachmentCreate  # noqa: F401
from openapi_server.models.registry_gallery_attachment_listing import RegistryGalleryAttachmentListing  # noqa: F401


def test_c_reate_gallery_attachment_for_user_registry(client: TestClient):
    """Test case for c_reate_gallery_attachment_for_user_registry

    
    """
    registry_gallery_attachment = {"attachment":{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"},"user_id":6,"membership_uuid":"membership_uuid"}

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
    #    "/user/{userID}/registry/{registryID}/gallery-attachment".format(userID=56, registryID=56),
    #    headers=headers,
    #    json=registry_gallery_attachment,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_gallery_attachment_for_user_registry(client: TestClient):
    """Test case for d_elete_gallery_attachment_for_user_registry

    
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
    #    "DELETE",
    #    "/user/{userID}/registry/{registryID}/gallery-attachment/{itemId}".format(userID=56, registryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_gallery_attachment_for_user_registry(client: TestClient):
    """Test case for list_all_gallery_attachment_for_user_registry

    
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
    #    "/user/{userID}/registry/{registryID}/gallery-attachment".format(userID=56, registryID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

