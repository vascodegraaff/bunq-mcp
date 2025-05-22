# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bunq_me_tab_result_inquiry_read import BunqMeTabResultInquiryRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_r_ead_bunqme_tab_result_inquiry_for_user_monetary_account_bunqme_tab(client: TestClient):
    """Test case for r_ead_bunqme_tab_result_inquiry_for_user_monetary_account_bunqme_tab

    
    """

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
    #    "GET",
    #    "/user/{userID}/monetary-account/{monetary-accountID}/bunqme-tab/{bunqme-tabID}/bunqme-tab-result-inquiry/{itemId}".format(userID=56, monetary-accountID=56, bunqme-tabID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

