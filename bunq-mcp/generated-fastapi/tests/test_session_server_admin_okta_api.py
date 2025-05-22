# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.session_server_admin_okta import SessionServerAdminOkta  # noqa: F401
from openapi_server.models.session_server_admin_okta_create import SessionServerAdminOktaCreate  # noqa: F401
from openapi_server.models.session_server_admin_okta_listing import SessionServerAdminOktaListing  # noqa: F401


def test_c_reate_session_server_admin_okta(client: TestClient):
    """Test case for c_reate_session_server_admin_okta

    
    """
    session_server_admin_okta = {"code":"code","state":"state","redirect_url":"redirect_url"}

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
    #    "/session-server-admin-okta",
    #    headers=headers,
    #    json=session_server_admin_okta,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_session_server_admin_okta(client: TestClient):
    """Test case for list_all_session_server_admin_okta

    
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
    #    "/session-server-admin-okta",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

