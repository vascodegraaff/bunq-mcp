# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.session_registry_installation import SessionRegistryInstallation  # noqa: F401
from openapi_server.models.session_registry_installation_create import SessionRegistryInstallationCreate  # noqa: F401


def test_c_reate_session_registry_installation(client: TestClient):
    """Test case for c_reate_session_registry_installation

    
    """
    session_registry_installation = {"client_public_key":"client_public_key","device_description":"device_description","app_installation_uuid":"app_installation_uuid"}

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
    #    "/session-registry-installation",
    #    headers=headers,
    #    json=session_registry_installation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

