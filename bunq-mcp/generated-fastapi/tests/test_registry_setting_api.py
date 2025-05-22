# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.registry_setting import RegistrySetting  # noqa: F401
from openapi_server.models.registry_setting_read import RegistrySettingRead  # noqa: F401
from openapi_server.models.registry_setting_update import RegistrySettingUpdate  # noqa: F401


def test_r_ead_registry_setting_for_user_registry(client: TestClient):
    """Test case for r_ead_registry_setting_for_user_registry

    
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
    #    "/user/{userID}/registry/{registryID}/registry-setting/{itemId}".format(userID=56, registryID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_registry_setting_for_user_registry(client: TestClient):
    """Test case for u_pdate_registry_setting_for_user_registry

    
    """
    registry_setting = {"color":"color","sdd_expiration_action":"sdd_expiration_action","icon":"icon","default_avatar_status":"default_avatar_status"}

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
    #    "/user/{userID}/registry/{registryID}/registry-setting/{itemId}".format(userID=56, registryID=56, itemId=56),
    #    headers=headers,
    #    json=registry_setting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

