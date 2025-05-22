# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_admin_profile import UserAdminProfile  # noqa: F401
from openapi_server.models.user_admin_profile_read import UserAdminProfileRead  # noqa: F401
from openapi_server.models.user_admin_profile_update import UserAdminProfileUpdate  # noqa: F401


def test_r_ead_user_admin_profile(client: TestClient):
    """Test case for r_ead_user_admin_profile

    
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
    #    "/user-admin-profile/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_admin_profile(client: TestClient):
    """Test case for u_pdate_user_admin_profile

    
    """
    user_admin_profile = {"city":"city","pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"favorite_feature":"favorite_feature","status":"status"}

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
    #    "/user-admin-profile/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=user_admin_profile,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

