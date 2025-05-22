# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_browser import MasterCardIdentityCheckChallengeRequestBrowser  # noqa: F401
from openapi_server.models.master_card_identity_check_challenge_request_browser_create import MasterCardIdentityCheckChallengeRequestBrowserCreate  # noqa: F401


def test_c_reate_challenge_request_browser(client: TestClient):
    """Test case for c_reate_challenge_request_browser

    
    """
    master_card_identity_check_challenge_request_browser = {"acs_trans_id":"acsTransID","challenge_window_size":"challengeWindowSize","message_type":"messageType","challenge_cancel":"challengeCancel","message_version":"messageVersion","message_extension":["messageExtension","messageExtension"],"three_ds_server_trans_id":"threeDSServerTransID"}

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
    #    "/challenge-request-browser",
    #    headers=headers,
    #    json=master_card_identity_check_challenge_request_browser,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

