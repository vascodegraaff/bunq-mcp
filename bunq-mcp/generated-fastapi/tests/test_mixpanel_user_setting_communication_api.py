# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.mixpanel_user_setting_communication import MixpanelUserSettingCommunication  # noqa: F401
from openapi_server.models.mixpanel_user_setting_communication_update import MixpanelUserSettingCommunicationUpdate  # noqa: F401


def test_u_pdate_mixpanel_user_setting_communication(client: TestClient):
    """Test case for u_pdate_mixpanel_user_setting_communication

    
    """
    mixpanel_user_setting_communication = {"marketing_communication":"marketing_communication"}

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
    #    "/mixpanel-user-setting-communication/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=mixpanel_user_setting_communication,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

