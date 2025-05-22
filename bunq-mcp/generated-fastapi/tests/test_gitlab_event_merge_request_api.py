# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.gitlab_event_merge_request import GitlabEventMergeRequest  # noqa: F401
from openapi_server.models.gitlab_event_merge_request_create import GitlabEventMergeRequestCreate  # noqa: F401


def test_c_reate_gitlab_event_merge_request(client: TestClient):
    """Test case for c_reate_gitlab_event_merge_request

    
    """
    gitlab_event_merge_request = {"object_attributes":{"iid":1,"target_branch":"target_branch","action":"action"},"changes":{"assignees":{"current":[{"name":"name","id":5,"username":"username"},{"name":"name","id":5,"username":"username"}],"previous":[{"name":"name","id":5,"username":"username"},{"name":"name","id":5,"username":"username"}]}},"project":{"path_with_namespace":"path_with_namespace","ssh_url":"ssh_url","description":"description","git_http_url":"git_http_url","git_ssh_url":"git_ssh_url","url":"url","http_url":"http_url","ci_config_path":"ci_config_path","web_url":"web_url","avatar_url":"avatar_url","name":"name","namespace":"namespace","visibility_level":6,"default_branch":"default_branch","id":0,"homepage":"homepage"}}

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
    #    "/gitlab-event-merge-request",
    #    headers=headers,
    #    json=gitlab_event_merge_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

