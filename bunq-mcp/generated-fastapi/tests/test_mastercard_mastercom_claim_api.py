# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_mastercom_claim import MasterCardMastercomClaim  # noqa: F401
from openapi_server.models.master_card_mastercom_claim_create import MasterCardMastercomClaimCreate  # noqa: F401
from openapi_server.models.master_card_mastercom_claim_listing import MasterCardMastercomClaimListing  # noqa: F401
from openapi_server.models.master_card_mastercom_claim_read import MasterCardMastercomClaimRead  # noqa: F401
from openapi_server.models.master_card_mastercom_claim_update import MasterCardMastercomClaimUpdate  # noqa: F401


def test_c_reate_mastercard_mastercom_claim_for_mastercard_action(client: TestClient):
    """Test case for c_reate_mastercard_mastercom_claim_for_mastercard_action

    
    """
    master_card_mastercom_claim = {"amount":{"currency":"currency","value":"value"},"acquirer_reference_number":"acquirer_reference_number","clearing_id":"clearing_id","authorisation_id":"authorisation_id","close_reason":"close_reason","status":"status"}

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
    #    "/mastercard-action/{mastercard-actionID}/mastercard-mastercom-claim".format(mastercard-actionID=56),
    #    headers=headers,
    #    json=master_card_mastercom_claim,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_mastercard_mastercom_claim_for_mastercard_action(client: TestClient):
    """Test case for list_all_mastercard_mastercom_claim_for_mastercard_action

    
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
    #    "/mastercard-action/{mastercard-actionID}/mastercard-mastercom-claim".format(mastercard-actionID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_mastercard_mastercom_claim_for_mastercard_action(client: TestClient):
    """Test case for r_ead_mastercard_mastercom_claim_for_mastercard_action

    
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
    #    "/mastercard-action/{mastercard-actionID}/mastercard-mastercom-claim/{itemId}".format(mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_mastercard_mastercom_claim_for_mastercard_action(client: TestClient):
    """Test case for u_pdate_mastercard_mastercom_claim_for_mastercard_action

    
    """
    master_card_mastercom_claim = {"amount":{"currency":"currency","value":"value"},"acquirer_reference_number":"acquirer_reference_number","clearing_id":"clearing_id","authorisation_id":"authorisation_id","close_reason":"close_reason","status":"status"}

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
    #    "/mastercard-action/{mastercard-actionID}/mastercard-mastercom-claim/{itemId}".format(mastercard-actionID=56, itemId=56),
    #    headers=headers,
    #    json=master_card_mastercom_claim,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

