# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.vonage_call_incoming_input import VonageCallIncomingInput  # noqa: F401
from openapi_server.models.vonage_call_incoming_input_create import VonageCallIncomingInputCreate  # noqa: F401


def test_c_reate_input_for_vonage_call_incoming(client: TestClient):
    """Test case for c_reate_input_for_vonage_call_incoming

    
    """
    vonage_call_incoming_input = {"speech":{"recording_url":"recording_url","timeout_reason":"timeout_reason","error":"error","results":[{"confidence":"confidence","text":"text"},{"confidence":"confidence","text":"text"}]},"dtmf":{"digits":"digits","timed_out":1},"from":"from","to":"to","uuid":"uuid","conversation_uuid":"conversation_uuid","timestamp":"timestamp"}

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
    #    "/vonage-call-incoming/{vonage-call-incomingID}/input".format(vonage-call-incomingID=56),
    #    headers=headers,
    #    json=vonage_call_incoming_input,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

