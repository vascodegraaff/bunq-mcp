# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.child import Child  # noqa: F401
from openapi_server.models.child_create import ChildCreate  # noqa: F401


def test_c_reate_child_for_user(client: TestClient):
    """Test case for c_reate_child_for_user

    
    """
    child = {"user_onboarding_type":"user_onboarding_type","date_of_birth":"date_of_birth","last_name":"last_name","middle_name":"middle_name","tax_resident":{"country":"country","tax_number":"tax_number","id":0,"status":"status"},"first_name":"first_name","all_pointer":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}]}

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
    #    "/user/{userID}/child".format(userID=56),
    #    headers=headers,
    #    json=child,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

