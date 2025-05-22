# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_person_risk_information import UserPersonRiskInformation  # noqa: F401
from openapi_server.models.user_person_risk_information_create import UserPersonRiskInformationCreate  # noqa: F401
from openapi_server.models.user_person_risk_information_listing import UserPersonRiskInformationListing  # noqa: F401
from openapi_server.models.user_person_risk_information_update import UserPersonRiskInformationUpdate  # noqa: F401
from openapi_server.models.user_risk_information import UserRiskInformation  # noqa: F401
from openapi_server.models.user_risk_information_create import UserRiskInformationCreate  # noqa: F401
from openapi_server.models.user_risk_information_listing import UserRiskInformationListing  # noqa: F401
from openapi_server.models.user_risk_information_update import UserRiskInformationUpdate  # noqa: F401


def test_c_reate_risk_information_for_user(client: TestClient):
    """Test case for c_reate_risk_information_for_user

    
    """
    user_risk_information = {"attachment_fund_source_id":0,"fund_sources":["fund_sources","fund_sources"],"account_purposes":["account_purposes","account_purposes"]}

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
    #    "/user/{userID}/risk-information".format(userID=56),
    #    headers=headers,
    #    json=user_risk_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_risk_information_for_user_person(client: TestClient):
    """Test case for c_reate_risk_information_for_user_person

    
    """
    user_person_risk_information = {"account_purpose":"account_purpose","expected_volume_transaction_monthly":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"expected_balance":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"fund_source_description":"fund_source_description","attachment_fund_source_id":0,"fund_sources":["fund_sources","fund_sources"],"account_purposes":["account_purposes","account_purposes"]}

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
    #    "/user-person/{user-personID}/risk-information".format(user-personID=56),
    #    headers=headers,
    #    json=user_person_risk_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_risk_information_for_user(client: TestClient):
    """Test case for list_all_risk_information_for_user

    
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
    #    "/user/{userID}/risk-information".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_risk_information_for_user_person(client: TestClient):
    """Test case for list_all_risk_information_for_user_person

    
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
    #    "/user-person/{user-personID}/risk-information".format(user-personID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_risk_information_for_user(client: TestClient):
    """Test case for u_pdate_risk_information_for_user

    
    """
    user_risk_information = {"attachment_fund_source_id":0,"fund_sources":["fund_sources","fund_sources"],"account_purposes":["account_purposes","account_purposes"]}

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
    #    "/user/{userID}/risk-information/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=user_risk_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_risk_information_for_user_person(client: TestClient):
    """Test case for u_pdate_risk_information_for_user_person

    
    """
    user_person_risk_information = {"account_purpose":"account_purpose","expected_volume_transaction_monthly":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"expected_balance":{"maximum":"maximum","currency":"currency","minimum":"minimum"},"fund_source_description":"fund_source_description","attachment_fund_source_id":0,"fund_sources":["fund_sources","fund_sources"],"account_purposes":["account_purposes","account_purposes"]}

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
    #    "/user-person/{user-personID}/risk-information/{itemId}".format(user-personID=56, itemId=56),
    #    headers=headers,
    #    json=user_person_risk_information,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

