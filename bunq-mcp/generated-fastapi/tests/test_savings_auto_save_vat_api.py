# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.savings_auto_save_vat import SavingsAutoSaveVat  # noqa: F401
from openapi_server.models.savings_auto_save_vat_create import SavingsAutoSaveVatCreate  # noqa: F401
from openapi_server.models.savings_auto_save_vat_listing import SavingsAutoSaveVatListing  # noqa: F401
from openapi_server.models.savings_auto_save_vat_read import SavingsAutoSaveVatRead  # noqa: F401
from openapi_server.models.savings_auto_save_vat_update import SavingsAutoSaveVatUpdate  # noqa: F401


def test_c_reate_savings_auto_save_vat_for_user(client: TestClient):
    """Test case for c_reate_savings_auto_save_vat_for_user

    
    """
    savings_auto_save_vat = {"monetary_account_id":0,"vat":"vat","pointer_investment_instrument":"pointer_investment_instrument","monetary_account_preferences_monetary_account_id":[{"id":0},{"id":0}],"status":"status","direction":"direction"}

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
    #    "/user/{userID}/savings-auto-save-vat".format(userID=56),
    #    headers=headers,
    #    json=savings_auto_save_vat,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_savings_auto_save_vat_for_user(client: TestClient):
    """Test case for list_all_savings_auto_save_vat_for_user

    
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
    #    "/user/{userID}/savings-auto-save-vat".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_savings_auto_save_vat_for_user(client: TestClient):
    """Test case for r_ead_savings_auto_save_vat_for_user

    
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
    #    "/user/{userID}/savings-auto-save-vat/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_savings_auto_save_vat_for_user(client: TestClient):
    """Test case for u_pdate_savings_auto_save_vat_for_user

    
    """
    savings_auto_save_vat = {"monetary_account_id":0,"vat":"vat","pointer_investment_instrument":"pointer_investment_instrument","monetary_account_preferences_monetary_account_id":[{"id":0},{"id":0}],"status":"status","direction":"direction"}

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
    #    "/user/{userID}/savings-auto-save-vat/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=savings_auto_save_vat,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

