# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_admin import UserAdmin  # noqa: F401
from openapi_server.models.user_admin_read import UserAdminRead  # noqa: F401
from openapi_server.models.user_admin_update import UserAdminUpdate  # noqa: F401


def test_r_ead_user_admin(client: TestClient):
    """Test case for r_ead_user_admin

    
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
    #    "/user-admin/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_admin(client: TestClient):
    """Test case for u_pdate_user_admin

    
    """
    user_admin = {"avatar":"avatar","display_name":"display_name","time_zone":"time_zone","avatar_uuid":"avatar_uuid","admin_group_main_id":5,"admin_groups":[{"name":"name","id":6},{"name":"name","id":6}],"public_uuid":"public_uuid","public_nick_name":"public_nick_name","alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"phone_number":"phone_number","email":"email","session_timeout":1,"flarum_username":"flarum_username","hashed_secret":"hashed_secret","status":"status"}

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
    #    "/user-admin/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=user_admin,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

