# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.identity_verification_message_incode_watchlist import IdentityVerificationMessageIncodeWatchlist  # noqa: F401
from openapi_server.models.identity_verification_message_incode_watchlist_create import IdentityVerificationMessageIncodeWatchlistCreate  # noqa: F401


def test_c_reate_watchlist(client: TestClient):
    """Test case for c_reate_watchlist

    
    """
    identity_verification_message_incode_watchlist = {"interview_id":"interviewId","ref":"ref","search_id":"search_id"}

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
    #    "/watchlist",
    #    headers=headers,
    #    json=identity_verification_message_incode_watchlist,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

