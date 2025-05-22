# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.partner_signup_check24 import PartnerSignupCheck24  # noqa: F401
from openapi_server.models.partner_signup_check24_create import PartnerSignupCheck24Create  # noqa: F401


def test_c_reate_partner_signup_check24(client: TestClient):
    """Test case for c_reate_partner_signup_check24

    
    """
    partner_signup_check24 = {"product":"product","check24_id":"check24_id","subscription":"subscription","user_data":{"place_of_birth":"place_of_birth","address":{"country":"country","city":"city","street":"street","street_number":"street_number","zip_code":"zip_code"},"nationality":"nationality","date_of_birth":"date_of_birth","residence_permit":"residence_permit","country_of_birth":"country_of_birth","last_name":"last_name","phone_number":"phone_number","first_name":"first_name","email":"email"}}

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
    #    "/partner-signup-check24",
    #    headers=headers,
    #    json=partner_signup_check24,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

