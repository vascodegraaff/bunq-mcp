# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.billing_contract_subscription import BillingContractSubscription  # noqa: F401
from openapi_server.models.billing_contract_subscription_create import BillingContractSubscriptionCreate  # noqa: F401
from openapi_server.models.billing_contract_subscription_listing import BillingContractSubscriptionListing  # noqa: F401
from openapi_server.models.billing_contract_subscription_read import BillingContractSubscriptionRead  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_billing_contract_subscription_for_user(client: TestClient):
    """Test case for c_reate_billing_contract_subscription_for_user

    
    """
    billing_contract_subscription = {"contract_version":7,"sub_status":"sub_status","created":"created","contract_date_end":"contract_date_end","subscription_type":"subscription_type","id":6,"contract_date_start":"contract_date_start","subscription_type_downgrade":"subscription_type_downgrade","updated":"updated","status":"status"}

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
    #    "/user/{userID}/billing-contract-subscription".format(userID=56),
    #    headers=headers,
    #    json=billing_contract_subscription,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_billing_contract_subscription_for_user(client: TestClient):
    """Test case for list_all_billing_contract_subscription_for_user

    
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
    #    "/user/{userID}/billing-contract-subscription".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_billing_contract_subscription_for_user(client: TestClient):
    """Test case for r_ead_billing_contract_subscription_for_user

    
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
    #    "/user/{userID}/billing-contract-subscription/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

