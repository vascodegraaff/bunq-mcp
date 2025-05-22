# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.quality_assurance_test_user_person import QualityAssuranceTestUserPerson  # noqa: F401
from openapi_server.models.quality_assurance_test_user_person_create import QualityAssuranceTestUserPersonCreate  # noqa: F401


def test_c_reate_quality_assurance_test_user_person(client: TestClient):
    """Test case for c_reate_quality_assurance_test_user_person

    
    """
    quality_assurance_test_user_person = {"country":"country","should_create_branch_switch":1,"should_create_video_onboarding":1,"language":"language","all_tag_user":["all_tag_user","all_tag_user"],"identification_document_date_expiry":"identification_document_date_expiry","interest_preference_receive_interest":"interest_preference_receive_interest","address_main":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"should_create_identity_verification":1,"identification_document_country":"identification_document_country","all_user_exposure":"all_user_exposure","vital_status":"vital_status","time_user_creation":"time_user_creation","should_create_address_postal":1,"approval_status":"approval_status","should_create_alias_phone_number":1,"income_source_type":"income_source_type","should_create_alias_email":1,"display_name":"display_name","all_tax_identification_number":[{"country":"country","tax_number":"tax_number","id":0,"status":"status"},{"country":"country","tax_number":"tax_number","id":0,"status":"status"}],"should_create_risk_information":1,"setting_zero_fx":"setting_zero_fx","public_nick_name":"public_nick_name","should_create_flarum_user_profile":1,"phone_number":"phone_number","identification_document_number":"identification_document_number","region":"region","should_complete_invite":1,"initial_balance":1,"postal_code_of_birth":"postal_code_of_birth","status":"status","setting_card_country_permission_auto_select":"setting_card_country_permission_auto_select","living_situation_type":"living_situation_type","gender":"gender","city":"city","address_postal":{"country":"country","is_user_address_updated":1,"province":"province","city":"city","mailbox_name":"mailbox_name","street":"street","extra":"extra","house_number":"house_number","po_box":"po_box","postal_code":"postal_code"},"should_create_address_main":1,"should_create_support_user_validation":1,"date_of_birth":"date_of_birth","all_monetary_account_definition":[{"sub_status":"sub_status","balance":{"currency":"currency","value":"value"},"country_iban":"country_iban","currency":"currency","type":"type","all_co_owner_definition":["all_co_owner_definition","all_co_owner_definition"],"all_pointer":["all_pointer","all_pointer"],"status":"status"},{"sub_status":"sub_status","balance":{"currency":"currency","value":"value"},"country_iban":"country_iban","currency":"currency","type":"type","all_co_owner_definition":["all_co_owner_definition","all_co_owner_definition"],"all_pointer":["all_pointer","all_pointer"],"status":"status"}],"marital_status_type":"marital_status_type","verification_status":"verification_status","should_create_user_identification_verification":1,"login_code":"login_code","setting_communication_marketing":"setting_communication_marketing","should_sync_fulfillment":1,"employment_status_type":"employment_status_type","country_of_birth":"country_of_birth","currency":"currency","first_name":"first_name","email":"email","all_billing_subscription_type":["all_billing_subscription_type","all_billing_subscription_type"],"should_create_credential":1,"should_create_all_identification_attachment":1,"sub_status":"sub_status","risk_score":"risk_score","last_name":"last_name","should_create_all_identification_document":1,"all_nationality":["all_nationality","all_nationality"],"country_of_banking_license":"country_of_banking_license","risk_fraud_label":"risk_fraud_label","all_investment_type":["all_investment_type","all_investment_type"],"identification_document_type":"identification_document_type","should_create_user_visited_ip":1,"device_definition":{"user_agent_phone":"user_agent_phone","ip":"ip","description":"description","user_agent_browser":"user_agent_browser","language":"language","type":"type","region":"region","uuid":"uuid","status":"status"},"setting_local_currency":"setting_local_currency","should_create_all_notification_filter":1,"age":6,"city_of_birth":"city_of_birth"}

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
    #    "/quality-assurance-test-user-person",
    #    headers=headers,
    #    json=quality_assurance_test_user_person,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

