# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.invite_profile_public_registration import InviteProfilePublicRegistration  # noqa: F401
from openapi_server.models.invite_profile_public_registration_create import InviteProfilePublicRegistrationCreate  # noqa: F401


def test_c_reate_registration_for_invite_profile_public(client: TestClient):
    """Test case for c_reate_registration_for_invite_profile_public

    
    """
    invite_profile_public_registration = {"status":"status"}

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
    #    "/invite-profile-public/{invite-profile-publicUUID}/registration".format(invite-profile-publicUUID='invite_profile_public_uuid_example'),
    #    headers=headers,
    #    json=invite_profile_public_registration,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

