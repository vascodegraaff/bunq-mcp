# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_setting_interest_monetary_account import UserSettingInterestMonetaryAccount  # noqa: F401
from openapi_server.models.user_setting_interest_monetary_account_listing import UserSettingInterestMonetaryAccountListing  # noqa: F401
from openapi_server.models.user_setting_interest_monetary_account_read import UserSettingInterestMonetaryAccountRead  # noqa: F401
from openapi_server.models.user_setting_interest_monetary_account_update import UserSettingInterestMonetaryAccountUpdate  # noqa: F401


def test_list_all_user_setting_interest_monetary_account_for_user(client: TestClient):
    """Test case for list_all_user_setting_interest_monetary_account_for_user

    
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
    #    "/user/{userID}/user-setting-interest-monetary-account".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_user_setting_interest_monetary_account_for_user(client: TestClient):
    """Test case for r_ead_user_setting_interest_monetary_account_for_user

    
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
    #    "/user/{userID}/user-setting-interest-monetary-account/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_setting_interest_monetary_account_for_user(client: TestClient):
    """Test case for u_pdate_user_setting_interest_monetary_account_for_user

    
    """
    user_setting_interest_monetary_account = {"monetary_account_id":0}

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
    #    "/user/{userID}/user-setting-interest-monetary-account/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=user_setting_interest_monetary_account,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

