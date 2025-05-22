# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.confirmation_alias_confirm import ConfirmationAliasConfirm  # noqa: F401
from openapi_server.models.confirmation_alias_confirm_create import ConfirmationAliasConfirmCreate  # noqa: F401
from openapi_server.models.confirmation_alias_confirm_read import ConfirmationAliasConfirmRead  # noqa: F401


def test_c_reate_confirmation_alias_confirm(client: TestClient):
    """Test case for c_reate_confirmation_alias_confirm

    
    """
    confirmation_alias_confirm = {"confirmation_code":"confirmation_code"}

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
    #    "/confirmation-alias-confirm",
    #    headers=headers,
    #    json=confirmation_alias_confirm,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_confirmation_alias_confirm(client: TestClient):
    """Test case for r_ead_confirmation_alias_confirm

    
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
    #    "/confirmation-alias-confirm/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

