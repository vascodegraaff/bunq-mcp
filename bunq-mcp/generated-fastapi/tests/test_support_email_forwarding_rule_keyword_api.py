# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.support_email_forwarding_rule_keyword import SupportEmailForwardingRuleKeyword  # noqa: F401
from openapi_server.models.support_email_forwarding_rule_keyword_create import SupportEmailForwardingRuleKeywordCreate  # noqa: F401
from openapi_server.models.support_email_forwarding_rule_keyword_listing import SupportEmailForwardingRuleKeywordListing  # noqa: F401
from openapi_server.models.support_email_forwarding_rule_keyword_read import SupportEmailForwardingRuleKeywordRead  # noqa: F401
from openapi_server.models.support_email_forwarding_rule_keyword_update import SupportEmailForwardingRuleKeywordUpdate  # noqa: F401


def test_c_reate_support_email_forwarding_rule_keyword_for_user(client: TestClient):
    """Test case for c_reate_support_email_forwarding_rule_keyword_for_user

    
    """
    support_email_forwarding_rule_keyword = {"destination_email":"destination_email","description":"description","destination_name":"destination_name","keyword":"keyword","status":"status"}

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
    #    "/user/{userID}/support-email-forwarding-rule-keyword".format(userID=56),
    #    headers=headers,
    #    json=support_email_forwarding_rule_keyword,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_support_email_forwarding_rule_keyword_for_user(client: TestClient):
    """Test case for d_elete_support_email_forwarding_rule_keyword_for_user

    
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
    #    "/user/{userID}/support-email-forwarding-rule-keyword/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_support_email_forwarding_rule_keyword_for_user(client: TestClient):
    """Test case for list_all_support_email_forwarding_rule_keyword_for_user

    
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
    #    "/user/{userID}/support-email-forwarding-rule-keyword".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_support_email_forwarding_rule_keyword_for_user(client: TestClient):
    """Test case for r_ead_support_email_forwarding_rule_keyword_for_user

    
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
    #    "/user/{userID}/support-email-forwarding-rule-keyword/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_support_email_forwarding_rule_keyword_for_user(client: TestClient):
    """Test case for u_pdate_support_email_forwarding_rule_keyword_for_user

    
    """
    support_email_forwarding_rule_keyword = {"destination_email":"destination_email","description":"description","destination_name":"destination_name","keyword":"keyword","status":"status"}

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
    #    "/user/{userID}/support-email-forwarding-rule-keyword/{itemId}".format(userID=56, itemId=56),
    #    headers=headers,
    #    json=support_email_forwarding_rule_keyword,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

