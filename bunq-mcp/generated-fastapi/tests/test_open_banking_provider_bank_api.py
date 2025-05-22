# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.open_banking_provider_bank import OpenBankingProviderBank  # noqa: F401
from openapi_server.models.open_banking_provider_bank_listing import OpenBankingProviderBankListing  # noqa: F401
from openapi_server.models.open_banking_provider_bank_update import OpenBankingProviderBankUpdate  # noqa: F401


def test_list_all_open_banking_provider_bank_for_user(client: TestClient):
    """Test case for list_all_open_banking_provider_bank_for_user

    
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
    #    "/user/{userID}/open-banking-provider-bank".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_open_banking_provider_bank_for_user(client: TestClient):
    """Test case for u_pdate_open_banking_provider_bank_for_user

    
    """
    open_banking_provider_bank = {"country":"country","all_payment_method_allowed_domestic":["all_payment_method_allowed_domestic","all_payment_method_allowed_domestic"],"aiia_provider_id":"aiia_provider_id","audience_business_status":1,"audience_private_status":1,"name":"name","all_payment_method_allowed_sepa":["all_payment_method_allowed_sepa","all_payment_method_allowed_sepa"],"payment_information_service_status":"payment_information_service_status","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"account_information_service_status":"account_information_service_status"}

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
    #    "/user/{userID}/open-banking-provider-bank/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=open_banking_provider_bank,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

