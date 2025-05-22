# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_company import UserCompany  # noqa: F401
from openapi_server.models.user_company_read import UserCompanyRead  # noqa: F401
from openapi_server.models.user_company_update import UserCompanyUpdate  # noqa: F401


def test_d_elete_user_company(client: TestClient):
    """Test case for d_elete_user_company

    
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
    #    "DELETE",
    #    "/user-company/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_user_company(client: TestClient):
    """Test case for r_ead_user_company

    
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
    #    "/user-company/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_user_company(client: TestClient):
    """Test case for u_pdate_user_company

    
    """
    user_company = {"country":"country","ubo":[{"nationality":"nationality","date_of_birth":"date_of_birth","name":"name"},{"nationality":"nationality","date_of_birth":"date_of_birth","name":"name"}],"notification_filters":[{"notification_target":"notification_target","category":"category","notification_delivery_method":"notification_delivery_method"},{"notification_target":"notification_target","category":"category","notification_delivery_method":"notification_delivery_method"}],"address_postal":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"directors":[{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"}],"language":"language","legal_form":"legal_form","deny_reason":"deny_reason","avatar_uuid":"avatar_uuid","version_terms_of_service":"version_terms_of_service","address_main":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"alias":[{"service":"service","name":"name","type":"type","value":"value"},{"service":"service","name":"name","type":"type","value":"value"}],"sector_of_industry":"sector_of_industry","id":7,"counter_bank_iban":"counter_bank_iban","billing_contract":[{"contract_version":7,"sub_status":"sub_status","created":"created","contract_date_end":"contract_date_end","subscription_type":"subscription_type","id":6,"contract_date_start":"contract_date_start","subscription_type_downgrade":"subscription_type_downgrade","updated":"updated","status":"status"},{"contract_version":7,"sub_status":"sub_status","created":"created","contract_date_end":"contract_date_end","subscription_type":"subscription_type","id":6,"contract_date_start":"contract_date_start","subscription_type_downgrade":"subscription_type_downgrade","updated":"updated","status":"status"}],"sub_status":"sub_status","created":"created","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","tax_resident":[{"country":"country","tax_number":"tax_number","id":0,"status":"status"},{"country":"country","tax_number":"tax_number","id":0,"status":"status"}],"daily_limit_without_confirmation_login":{"currency":"currency","value":"value"},"public_uuid":"public_uuid","public_nick_name":"public_nick_name","customer_limit":{"limit_card_debit_maestro":4,"limit_card_wildcard":1,"spent_amount_monthly":{"currency":"currency","value":"value"},"limit_monetary_account":3,"limit_amount_monthly":{"currency":"currency","value":"value"},"limit_card_replacement":1,"limit_card_debit_mastercard":7,"limit_card_debit_wildcard":1,"limit_monetary_account_remaining":2},"name":"name","chamber_of_commerce_number":"chamber_of_commerce_number","type_of_business_entity":"type_of_business_entity","region":"region","relations":[{"user_status":"user_status","all_company_employee_card":[{"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"},{"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"}],"user_id":"user_id","counter_user_id":"counter_user_id","counter_label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"company_employee_setting_adyen_card_transaction":{"monetary_account_payout_id":0,"pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"},"relationship":"relationship","counter_user_status":"counter_user_status","status":"status"},{"user_status":"user_status","all_company_employee_card":[{"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"},{"employee_preferred_name_on_card":"employee_preferred_name_on_card","employee_name_on_card":"employee_name_on_card","pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"type":"type","number_of_company_employee_card_receipt_pending":4,"amount_limit_monthly":{"currency":"currency","value":"value"},"product_type":"product_type","company_name_on_card":"company_name_on_card","amount_spent_monthly":{"currency":"currency","value":"value"},"pointer_monetary_account":{"service":"service","name":"name","type":"type","value":"value"},"company_employee_card_limit":{"amount_limit_monthly":{"currency":"currency","value":"value"},"user_employee_id":7,"amount_spent_monthly":{"currency":"currency","value":"value"},"user_company_id":8},"status":"status"}],"user_id":"user_id","counter_user_id":"counter_user_id","counter_label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"label_user":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"company_employee_setting_adyen_card_transaction":{"monetary_account_payout_id":0,"pointer_counter_user":{"service":"service","name":"name","type":"type","value":"value"},"status":"status"},"relationship":"relationship","counter_user_status":"counter_user_status","status":"status"}],"updated":"updated","session_timeout":2,"status":"status","address_shipping":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"customer":{"invoice_notification_preference":"invoice_notification_preference","created":"created","billing_account_id":"billing_account_id","id":9,"updated":"updated"}}

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
    #    "/user-company/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=user_company,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

