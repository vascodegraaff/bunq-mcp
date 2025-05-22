# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.government_referral_portal_external_search_by_product import GovernmentReferralPortalExternalSearchByProduct  # noqa: F401
from openapi_server.models.government_referral_portal_external_search_by_product_create import GovernmentReferralPortalExternalSearchByProductCreate  # noqa: F401


def test_c_reate_opvragen_product(client: TestClient):
    """Test case for c_reate_opvragen_product

    
    """
    government_referral_portal_external_search_by_product = {"metadata":{"requester_full_name":"requester_full_name","question_type":"question_type","legal_basis":"legal_basis","data_time_stamp":1,"name_authoriser":"name_authoriser","requester_email":"requester_email","requester_organisation":"requester_organisation","vb_user_email":"vb_user_email","bank_identifier":"bank_identifier","authorised":1,"request_send_time_stamp":"request_send_time_stamp","question_identifier":"question_identifier","unique_reference_number":"unique_reference_number"},"search_parameters":{"address":{"country":"country","address_type":"address_type","city":"city","street":"street","house_number_suffix":"house_number_suffix","house_number":"house_number","postal_code":"postal_code","po_box":"po_box","other_address_data":"other_address_data"},"start_periode":"startPeriode","date_of_birth":"date_of_birth","start_period":"start_period","organisation_name":"organisation_name","productnummer":"productnummer","soort_product":"soortProduct","end_period":"end_period","product_number":"product_number","vraagtype":"vraagtype","eind_periode":"eindPeriode","product_type":"product_type","citizen_service_number":"citizen_service_number","name":{"initials":"initials","last_name":"last_name","other_initials":"other_initials","last_name_prefix":"last_name_prefix","first_name":"first_name","first_initial":"first_initial"},"chamber_of_commerce_number":"chamber_of_commerce_number"}}

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
    #    "/opvragen-product",
    #    headers=headers,
    #    json=government_referral_portal_external_search_by_product,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

