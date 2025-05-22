# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.quality_assurance_test_card_physical import QualityAssuranceTestCardPhysical  # noqa: F401
from openapi_server.models.quality_assurance_test_card_physical_create import QualityAssuranceTestCardPhysicalCreate  # noqa: F401


def test_c_reate_quality_assurance_test_card_physical_for_user(client: TestClient):
    """Test case for c_reate_quality_assurance_test_card_physical_for_user

    
    """
    quality_assurance_test_card_physical = {"should_create_card_identification_assignment":1,"activation_code":"activation_code","sub_status":"sub_status","pin_assignment_routing_type":"pin_assignment_routing_type","expiry_date":"expiry_date","monetary_account_id":6,"limit_atm":"limit_atm","type":"type","sequence_number":"sequence_number","second_line":"second_line","order_status":"order_status","should_sync_billing_contract":1,"product_type":"product_type","pin":"pin","sub_type":"sub_type","limit_transaction":"limit_transaction","name":"name","limit":"limit","user_holder_id":0,"extension_type":"extension_type","all_country_permission":["all_country_permission","all_country_permission"],"status":"status"}

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
    #    "/user/{userID}/quality-assurance-test-card-physical".format(userID=56),
    #    headers=headers,
    #    json=quality_assurance_test_card_physical,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

