# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_identification_tax_resident import UserIdentificationTaxResident  # noqa: F401
from openapi_server.models.user_identification_tax_resident_create import UserIdentificationTaxResidentCreate  # noqa: F401
from openapi_server.models.user_identification_tax_resident_listing import UserIdentificationTaxResidentListing  # noqa: F401


def test_c_reate_tax_resident_for_user(client: TestClient):
    """Test case for c_reate_tax_resident_for_user

    
    """
    user_identification_tax_resident = {"tax_resident":[{"country":"country","tax_number":"tax_number","id":0,"status":"status"},{"country":"country","tax_number":"tax_number","id":0,"status":"status"}],"tax_resident_exemption":[{"country":"country","reason":"reason","attachment":[{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"},{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"}]},{"country":"country","reason":"reason","attachment":[{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"},{"urls":[{"type":"type","url":"url"},{"type":"type","url":"url"}],"content_type":"content_type","description":"description"}]}]}

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
    #    "/user/{userID}/tax-resident".format(userID=56),
    #    headers=headers,
    #    json=user_identification_tax_resident,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_tax_resident_for_user(client: TestClient):
    """Test case for list_all_tax_resident_for_user

    
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
    #    "/user/{userID}/tax-resident".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

