# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.birdee_investment_portfolio_valuation_listing import BirdeeInvestmentPortfolioValuationListing  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_list_all_valuation_for_user_monetary_account_investment_birdee_investment_portfolio(client: TestClient):
    """Test case for list_all_valuation_for_user_monetary_account_investment_birdee_investment_portfolio

    
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
    #    "/user/{userID}/monetary-account-investment/{monetary-account-investmentID}/birdee-investment-portfolio/{birdee-investment-portfolioID}/valuation".format(userID=56, monetary-account-investmentID=56, birdee-investment-portfolioID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

