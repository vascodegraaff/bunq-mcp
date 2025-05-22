# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.prompt_manager_action import PromptManagerAction  # noqa: F401
from openapi_server.models.prompt_manager_action_create import PromptManagerActionCreate  # noqa: F401


def test_c_reate_prompt_manager_action_for_user(client: TestClient):
    """Test case for c_reate_prompt_manager_action_for_user

    
    """
    prompt_manager_action = {"all_chat":[{"role":"role","content":"content"},{"role":"role","content":"content"}],"action_type":"action_type","commit_message":"commit_message","text":"text","project_name":"project_name","prompt_tag":"prompt_tag","prompt_name":"prompt_name","prompt_page_number":0}

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
    #    "/user/{userID}/prompt-manager-action".format(userID=56),
    #    headers=headers,
    #    json=prompt_manager_action,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

