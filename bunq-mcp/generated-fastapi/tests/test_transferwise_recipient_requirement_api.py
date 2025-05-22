# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transferwise_account_requirement import TransferwiseAccountRequirement  # noqa: F401
from openapi_server.models.transferwise_account_requirement_create import TransferwiseAccountRequirementCreate  # noqa: F401
from openapi_server.models.transferwise_account_requirement_listing import TransferwiseAccountRequirementListing  # noqa: F401


def test_c_reate_transferwise_recipient_requirement_for_user_transferwise_quote(client: TestClient):
    """Test case for c_reate_transferwise_recipient_requirement_for_user_transferwise_quote

    
    """
    transferwise_account_requirement = {"name_account_holder":"name_account_holder","country":"country","detail":[{"name":"name","value":"value","key":"key","group":{"validation_regexp":"validation_regexp","min_length":"min_length","values_allowed":{"name":"name","key":"key"},"display_format":"display_format","name":"name","validation_async":{"params":{"parameter_name":"parameter_name","key":"key","required":1},"url":"url"},"type":"type","key":"key","refresh_requirements_on_change":1,"required":1,"example":"example","max_length":"max_length"}},{"name":"name","value":"value","key":"key","group":{"validation_regexp":"validation_regexp","min_length":"min_length","values_allowed":{"name":"name","key":"key"},"display_format":"display_format","name":"name","validation_async":{"params":{"parameter_name":"parameter_name","key":"key","required":1},"url":"url"},"type":"type","key":"key","refresh_requirements_on_change":1,"required":1,"example":"example","max_length":"max_length"}}],"type":"type"}

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
    #    "/user/{userID}/transferwise-quote/{transferwise-quoteID}/transferwise-recipient-requirement".format(userID=56, transferwise-quoteID=56),
    #    headers=headers,
    #    json=transferwise_account_requirement,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_transferwise_recipient_requirement_for_user_transferwise_quote(client: TestClient):
    """Test case for list_all_transferwise_recipient_requirement_for_user_transferwise_quote

    
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
    #    "/user/{userID}/transferwise-quote/{transferwise-quoteID}/transferwise-recipient-requirement".format(userID=56, transferwise-quoteID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

