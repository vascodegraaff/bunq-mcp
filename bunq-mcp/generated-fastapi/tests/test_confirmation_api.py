# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.confirmation_alias_device import ConfirmationAliasDevice  # noqa: F401
from openapi_server.models.confirmation_alias_device_create import ConfirmationAliasDeviceCreate  # noqa: F401
from openapi_server.models.confirmation_alias_device_read import ConfirmationAliasDeviceRead  # noqa: F401
from openapi_server.models.confirmation_alias_device_update import ConfirmationAliasDeviceUpdate  # noqa: F401
from openapi_server.models.confirmation_alias_installation import ConfirmationAliasInstallation  # noqa: F401
from openapi_server.models.confirmation_alias_installation_create import ConfirmationAliasInstallationCreate  # noqa: F401
from openapi_server.models.confirmation_alias_installation_read import ConfirmationAliasInstallationRead  # noqa: F401
from openapi_server.models.confirmation_alias_installation_update import ConfirmationAliasInstallationUpdate  # noqa: F401
from openapi_server.models.confirmation_alias_monetary_account import ConfirmationAliasMonetaryAccount  # noqa: F401
from openapi_server.models.confirmation_alias_monetary_account_create import ConfirmationAliasMonetaryAccountCreate  # noqa: F401
from openapi_server.models.confirmation_alias_monetary_account_read import ConfirmationAliasMonetaryAccountRead  # noqa: F401
from openapi_server.models.confirmation_alias_monetary_account_update import ConfirmationAliasMonetaryAccountUpdate  # noqa: F401
from openapi_server.models.confirmation_alias_pointer import ConfirmationAliasPointer  # noqa: F401
from openapi_server.models.confirmation_alias_pointer_create import ConfirmationAliasPointerCreate  # noqa: F401
from openapi_server.models.confirmation_alias_pointer_read import ConfirmationAliasPointerRead  # noqa: F401
from openapi_server.models.confirmation_alias_pointer_update import ConfirmationAliasPointerUpdate  # noqa: F401
from openapi_server.models.confirmation_alias_user import ConfirmationAliasUser  # noqa: F401
from openapi_server.models.confirmation_alias_user_create import ConfirmationAliasUserCreate  # noqa: F401
from openapi_server.models.confirmation_alias_user_read import ConfirmationAliasUserRead  # noqa: F401
from openapi_server.models.confirmation_alias_user_update import ConfirmationAliasUserUpdate  # noqa: F401


def test_c_reate_confirmation(client: TestClient):
    """Test case for c_reate_confirmation

    
    """
    confirmation_alias_pointer = {"pointer":{"service":"service","name":"name","type":"type","value":"value"},"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/confirmation",
    #    headers=headers,
    #    json=confirmation_alias_pointer,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_confirmation_for_alias_device(client: TestClient):
    """Test case for c_reate_confirmation_for_alias_device

    
    """
    confirmation_alias_device = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/alias-device/{alias-deviceID}/confirmation".format(alias-deviceID=56),
    #    headers=headers,
    #    json=confirmation_alias_device,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_confirmation_for_alias_installation(client: TestClient):
    """Test case for c_reate_confirmation_for_alias_installation

    
    """
    confirmation_alias_installation = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/alias-installation/{alias-installationID}/confirmation".format(alias-installationID=56),
    #    headers=headers,
    #    json=confirmation_alias_installation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_confirmation_for_user_alias_user(client: TestClient):
    """Test case for c_reate_confirmation_for_user_alias_user

    
    """
    confirmation_alias_user = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type","status":"status"}

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
    #    "/user/{userID}/alias-user/{alias-userID}/confirmation".format(userID=56, alias-userID=56),
    #    headers=headers,
    #    json=confirmation_alias_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_c_reate_confirmation_for_user_monetary_account_alias_monetary_account(client: TestClient):
    """Test case for c_reate_confirmation_for_user_monetary_account_alias_monetary_account

    
    """
    confirmation_alias_monetary_account = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/alias-monetary-account/{alias-monetary-accountID}/confirmation".format(userID=56, monetary-accountID=56, alias-monetary-accountID=56),
    #    headers=headers,
    #    json=confirmation_alias_monetary_account,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_confirmation(client: TestClient):
    """Test case for r_ead_confirmation

    
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
    #    "/confirmation/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_confirmation_for_alias_device(client: TestClient):
    """Test case for r_ead_confirmation_for_alias_device

    
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
    #    "/alias-device/{alias-deviceID}/confirmation/{itemId}".format(alias-deviceID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_confirmation_for_alias_installation(client: TestClient):
    """Test case for r_ead_confirmation_for_alias_installation

    
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
    #    "/alias-installation/{alias-installationID}/confirmation/{itemId}".format(alias-installationID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_confirmation_for_user_alias_user(client: TestClient):
    """Test case for r_ead_confirmation_for_user_alias_user

    
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
    #    "/user/{userID}/alias-user/{alias-userID}/confirmation/{itemId}".format(userID=56, alias-userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_confirmation_for_user_monetary_account_alias_monetary_account(client: TestClient):
    """Test case for r_ead_confirmation_for_user_monetary_account_alias_monetary_account

    
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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/alias-monetary-account/{alias-monetary-accountID}/confirmation/{itemId}".format(userID=56, monetary-accountID=56, alias-monetary-accountID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_confirmation(client: TestClient):
    """Test case for u_pdate_confirmation

    
    """
    confirmation_alias_pointer = {"pointer":{"service":"service","name":"name","type":"type","value":"value"},"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/confirmation/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=confirmation_alias_pointer,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_confirmation_for_alias_device(client: TestClient):
    """Test case for u_pdate_confirmation_for_alias_device

    
    """
    confirmation_alias_device = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/alias-device/{alias-deviceID}/confirmation/{itemId}".format(alias-deviceID=56, itemId=56),
    #    headers=headers,
    #    json=confirmation_alias_device,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_confirmation_for_alias_installation(client: TestClient):
    """Test case for u_pdate_confirmation_for_alias_installation

    
    """
    confirmation_alias_installation = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/alias-installation/{alias-installationID}/confirmation/{itemId}".format(alias-installationID=56, itemId=56),
    #    headers=headers,
    #    json=confirmation_alias_installation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_confirmation_for_user_alias_user(client: TestClient):
    """Test case for u_pdate_confirmation_for_user_alias_user

    
    """
    confirmation_alias_user = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type","status":"status"}

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
    #    "/user/{userID}/alias-user/{alias-userID}/confirmation/{itemId}".format(userID=56, alias-userID=56, itemId=56),
    #    headers=headers,
    #    json=confirmation_alias_user,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_confirmation_for_user_monetary_account_alias_monetary_account(client: TestClient):
    """Test case for u_pdate_confirmation_for_user_monetary_account_alias_monetary_account

    
    """
    confirmation_alias_monetary_account = {"confirmation_code":"confirmation_code","confirmation_type":"confirmation_type"}

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
    #    "/user/{userID}/monetary-account/{monetary-accountID}/alias-monetary-account/{alias-monetary-accountID}/confirmation/{itemId}".format(userID=56, monetary-accountID=56, alias-monetary-accountID=56, itemId=56),
    #    headers=headers,
    #    json=confirmation_alias_monetary_account,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

