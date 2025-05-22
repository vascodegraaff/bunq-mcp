# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.push_message_read_category import PushMessageReadCategory  # noqa: F401
from openapi_server.models.push_message_read_category_create import PushMessageReadCategoryCreate  # noqa: F401


def test_c_reate_push_message_read_category_for_user(client: TestClient):
    """Test case for c_reate_push_message_read_category_for_user

    
    """
    push_message_read_category = {"installed_app":"installed_app","read_category":[{"monetary_account_id":0,"category":"category","registry_id":6},{"monetary_account_id":0,"category":"category","registry_id":6}]}

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
    #    "/user/{userID}/push-message-read-category".format(userID=56),
    #    headers=headers,
    #    json=push_message_read_category,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

