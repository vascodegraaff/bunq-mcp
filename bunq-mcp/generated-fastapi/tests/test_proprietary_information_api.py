# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_identity_check_proprietary_information import MasterCardIdentityCheckProprietaryInformation  # noqa: F401
from openapi_server.models.master_card_identity_check_proprietary_information_create import MasterCardIdentityCheckProprietaryInformationCreate  # noqa: F401


def test_c_reate_proprietary_information(client: TestClient):
    """Test case for c_reate_proprietary_information

    
    """
    master_card_identity_check_proprietary_information = {"acs":"acs","cancel":"cancel","data_entry":"data_entry"}

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
    #    "/proprietary-information",
    #    headers=headers,
    #    json=master_card_identity_check_proprietary_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

