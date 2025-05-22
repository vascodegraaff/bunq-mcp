# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.investment_deposit import InvestmentDeposit  # noqa: F401
from openapi_server.models.investment_deposit_listing import InvestmentDepositListing  # noqa: F401
from openapi_server.models.investment_deposit_update import InvestmentDepositUpdate  # noqa: F401


def test_list_all_deposit_for_user_monetary_account_investment(client: TestClient):
    """Test case for list_all_deposit_for_user_monetary_account_investment

    
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
    #    "/user/{userID}/monetary-account-investment/{monetary-account-investmentID}/deposit".format(userID=56, monetary-account-investmentID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_deposit_for_user_monetary_account_investment(client: TestClient):
    """Test case for u_pdate_deposit_for_user_monetary_account_investment

    
    """
    investment_deposit = {"sub_status":"sub_status","status":"status"}

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
    #    "/user/{userID}/monetary-account-investment/{monetary-account-investmentID}/deposit/{itemId}".format(userID=56, monetary-account-investmentID=56, itemId=56),
    #    headers=headers,
    #    json=investment_deposit,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

