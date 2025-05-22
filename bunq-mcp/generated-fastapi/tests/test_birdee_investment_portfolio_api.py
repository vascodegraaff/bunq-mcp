# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.birdee_investment_portfolio import BirdeeInvestmentPortfolio  # noqa: F401
from openapi_server.models.birdee_investment_portfolio_create import BirdeeInvestmentPortfolioCreate  # noqa: F401
from openapi_server.models.birdee_investment_portfolio_read import BirdeeInvestmentPortfolioRead  # noqa: F401
from openapi_server.models.birdee_investment_portfolio_update import BirdeeInvestmentPortfolioUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_birdee_investment_portfolio_for_user_monetary_account_investment(client: TestClient):
    """Test case for c_reate_birdee_investment_portfolio_for_user_monetary_account_investment

    
    """
    birdee_investment_portfolio = {"investment_theme":"investment_theme","external_identifier":"external_identifier","goal":{"amount_target":{"currency":"currency","value":"value"},"time_end":"time_end"},"balance":{"amount_withdrawal_pending":{"currency":"currency","value":"value"},"amount_deposit_pending":{"currency":"currency","value":"value"},"amount_available":{"currency":"currency","value":"value"},"amount_profit":{"currency":"currency","value":"value"},"amount_withdrawal_total":{"currency":"currency","value":"value"},"amount_fee_total":{"currency":"currency","value":"value"},"amount_deposit_total":{"currency":"currency","value":"value"}},"allocations":[{"instrument_currency":"instrument_currency","amount":"amount","instrument_isin":"instrument_isin","quantity":"quantity","instrument_name":"instrument_name","instrument_asset_class":"instrument_asset_class","price":"price","weight":"weight","instrument_region_name":"instrument_region_name","instrument_key_information_document_uri":"instrument_key_information_document_uri","instrument_asset_class_name":"instrument_asset_class_name"},{"instrument_currency":"instrument_currency","amount":"amount","instrument_isin":"instrument_isin","quantity":"quantity","instrument_name":"instrument_name","instrument_asset_class":"instrument_asset_class","price":"price","weight":"weight","instrument_region_name":"instrument_region_name","instrument_key_information_document_uri":"instrument_key_information_document_uri","instrument_asset_class_name":"instrument_asset_class_name"}],"name":"name","number_of_strategy_change_annual_maximum":7,"number_of_strategy_change_annual_used":5,"risk_profile_type":"risk_profile_type","status":"status"}

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
    #    "/user/{userID}/monetary-account-investment/{monetary-account-investmentID}/birdee-investment-portfolio".format(userID=56, monetary-account-investmentID=56),
    #    headers=headers,
    #    json=birdee_investment_portfolio,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_birdee_investment_portfolio_for_user_monetary_account_investment(client: TestClient):
    """Test case for r_ead_birdee_investment_portfolio_for_user_monetary_account_investment

    
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
    #    "/user/{userID}/monetary-account-investment/{monetary-account-investmentID}/birdee-investment-portfolio/{itemId}".format(userID=56, monetary-account-investmentID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_birdee_investment_portfolio_for_user_monetary_account_investment(client: TestClient):
    """Test case for u_pdate_birdee_investment_portfolio_for_user_monetary_account_investment

    
    """
    birdee_investment_portfolio = {"investment_theme":"investment_theme","external_identifier":"external_identifier","goal":{"amount_target":{"currency":"currency","value":"value"},"time_end":"time_end"},"balance":{"amount_withdrawal_pending":{"currency":"currency","value":"value"},"amount_deposit_pending":{"currency":"currency","value":"value"},"amount_available":{"currency":"currency","value":"value"},"amount_profit":{"currency":"currency","value":"value"},"amount_withdrawal_total":{"currency":"currency","value":"value"},"amount_fee_total":{"currency":"currency","value":"value"},"amount_deposit_total":{"currency":"currency","value":"value"}},"allocations":[{"instrument_currency":"instrument_currency","amount":"amount","instrument_isin":"instrument_isin","quantity":"quantity","instrument_name":"instrument_name","instrument_asset_class":"instrument_asset_class","price":"price","weight":"weight","instrument_region_name":"instrument_region_name","instrument_key_information_document_uri":"instrument_key_information_document_uri","instrument_asset_class_name":"instrument_asset_class_name"},{"instrument_currency":"instrument_currency","amount":"amount","instrument_isin":"instrument_isin","quantity":"quantity","instrument_name":"instrument_name","instrument_asset_class":"instrument_asset_class","price":"price","weight":"weight","instrument_region_name":"instrument_region_name","instrument_key_information_document_uri":"instrument_key_information_document_uri","instrument_asset_class_name":"instrument_asset_class_name"}],"name":"name","number_of_strategy_change_annual_maximum":7,"number_of_strategy_change_annual_used":5,"risk_profile_type":"risk_profile_type","status":"status"}

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
    #    "/user/{userID}/monetary-account-investment/{monetary-account-investmentID}/birdee-investment-portfolio/{itemId}".format(userID=56, monetary-account-investmentID=56, itemId=56),
    #    headers=headers,
    #    json=birdee_investment_portfolio,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

