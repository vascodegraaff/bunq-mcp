# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile import BunqMeFundraiserProfile  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_create import BunqMeFundraiserProfileCreate  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_read import BunqMeFundraiserProfileRead  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_user import BunqMeFundraiserProfileUser  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_user_create import BunqMeFundraiserProfileUserCreate  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_user_listing import BunqMeFundraiserProfileUserListing  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_user_read import BunqMeFundraiserProfileUserRead  # noqa: F401
from openapi_server.models.bunq_me_fundraiser_profile_user_update import BunqMeFundraiserProfileUserUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_bunqme_fundraiser_profile(client: TestClient):
    """Test case for c_reate_bunqme_fundraiser_profile

    
    """
    bunq_me_fundraiser_profile = {"pointer":{"service":"service","name":"name","type":"type","value":"value"},"color":"color","attachment":{"content_type":"content_type","description":"description","uuid":"uuid"},"alias":{"country":"country","swift_bic":"swift_bic","is_light":1,"merchant_category_code":"merchant_category_code","iban":"iban","transferwise_bank_code":"transferwise_bank_code","label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"transferwise_account_number":"transferwise_account_number","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","bunq_me":{"service":"service","name":"name","type":"type","value":"value"},"swift_account_number":"swift_account_number"},"description":"description","currency":"currency","invite_profile_name":"invite_profile_name","merchant_available":[{"available":1,"merchant_type":"merchant_type"},{"available":1,"merchant_type":"merchant_type"}],"redirect_url":"redirect_url","status":"status"}

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
    #    "/bunqme-fundraiser-profile",
    #    headers=headers,
    #    json=bunq_me_fundraiser_profile,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_bunqme_fundraiser_profile_for_user(client: TestClient):
    """Test case for c_reate_bunqme_fundraiser_profile_for_user

    
    """
    bunq_me_fundraiser_profile_user = {"pointer":{"service":"service","name":"name","type":"type","value":"value"},"color":"color","attachment_public_uuid":"attachment_public_uuid","monetary_account_id":0,"description":"description","redirect_url":"redirect_url","status":"status"}

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
    #    "/user/{userID}/bunqme-fundraiser-profile".format(userID=56),
    #    headers=headers,
    #    json=bunq_me_fundraiser_profile_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_bunqme_fundraiser_profile_for_user(client: TestClient):
    """Test case for list_all_bunqme_fundraiser_profile_for_user

    
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
    #    "/user/{userID}/bunqme-fundraiser-profile".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_bunqme_fundraiser_profile(client: TestClient):
    """Test case for r_ead_bunqme_fundraiser_profile

    
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
    #    "/bunqme-fundraiser-profile/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_bunqme_fundraiser_profile_for_user(client: TestClient):
    """Test case for r_ead_bunqme_fundraiser_profile_for_user

    
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
    #    "/user/{userID}/bunqme-fundraiser-profile/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_bunqme_fundraiser_profile_for_user(client: TestClient):
    """Test case for u_pdate_bunqme_fundraiser_profile_for_user

    
    """
    bunq_me_fundraiser_profile_user = {"pointer":{"service":"service","name":"name","type":"type","value":"value"},"color":"color","attachment_public_uuid":"attachment_public_uuid","monetary_account_id":0,"description":"description","redirect_url":"redirect_url","status":"status"}

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
    #    "/user/{userID}/bunqme-fundraiser-profile/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=bunq_me_fundraiser_profile_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

