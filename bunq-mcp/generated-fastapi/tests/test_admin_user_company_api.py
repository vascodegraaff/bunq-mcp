# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_user_company import AdminUserCompany  # noqa: F401
from openapi_server.models.admin_user_company_read import AdminUserCompanyRead  # noqa: F401
from openapi_server.models.admin_user_company_update import AdminUserCompanyUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_r_ead_admin_user_company(client: TestClient):
    """Test case for r_ead_admin_user_company

    
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
    #    "/admin-user-company/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_user_company(client: TestClient):
    """Test case for u_pdate_admin_user_company

    
    """
    admin_user_company = {"counter_bank_iban":"counter_bank_iban","country":"country","ubo":[{"nationality":"nationality","date_of_birth":"date_of_birth","name":"name"},{"nationality":"nationality","date_of_birth":"date_of_birth","name":"name"}],"sub_status":"sub_status","address_postal":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"legal_form":"legal_form","avatar_uuid":"avatar_uuid","daily_limit_without_confirmation_login":{"currency":"currency","value":"value"},"public_nick_name":"public_nick_name","name":"name","address_main":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"sector_of_industry":"sector_of_industry","chamber_of_commerce_number":"chamber_of_commerce_number","status":"status"}

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
    #    "/admin-user-company/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=admin_user_company,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

