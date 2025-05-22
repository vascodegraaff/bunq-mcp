# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.analytics_identifier import AnalyticsIdentifier  # noqa: F401
from openapi_server.models.analytics_identifier_create import AnalyticsIdentifierCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_analytics_identifier_for_user_device(client: TestClient):
    """Test case for c_reate_analytics_identifier_for_user_device

    
    """
    analytics_identifier = {"type":"type","token":"token"}

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
    #    "/user/{userID}/device/{deviceID}/analytics-identifier".format(userID=56, deviceID=56),
    #    headers=headers,
    #    json=analytics_identifier,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

