# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.sim_virtual_message_installation import SimVirtualMessageInstallation  # noqa: F401
from openapi_server.models.sim_virtual_message_installation_create import SimVirtualMessageInstallationCreate  # noqa: F401


def test_c_reate_sim_virtual_message_installation(client: TestClient):
    """Test case for c_reate_sim_virtual_message_installation

    
    """
    sim_virtual_message_installation = {"data":["data","data"],"created_at":"created_at","id":"id","type":"type"}

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
    #    "/sim-virtual-message-installation",
    #    headers=headers,
    #    json=sim_virtual_message_installation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

