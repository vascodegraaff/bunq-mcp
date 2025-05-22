# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_comment_payment_investigation import AdminCommentPaymentInvestigation  # noqa: F401
from openapi_server.models.admin_comment_payment_investigation_create import AdminCommentPaymentInvestigationCreate  # noqa: F401
from openapi_server.models.admin_comment_payment_investigation_listing import AdminCommentPaymentInvestigationListing  # noqa: F401
from openapi_server.models.admin_comment_payment_investigation_read import AdminCommentPaymentInvestigationRead  # noqa: F401
from openapi_server.models.admin_comment_payment_investigation_update import AdminCommentPaymentInvestigationUpdate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_comment_payment_investigation_for_payment_investigation(client: TestClient):
    """Test case for c_reate_comment_payment_investigation_for_payment_investigation

    
    """
    admin_comment_payment_investigation = {"visibility":"visibility","text":"text","status":"status"}

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
    #    "/payment-investigation/{payment-investigationID}/comment-payment-investigation".format(payment-investigationID=56),
    #    headers=headers,
    #    json=admin_comment_payment_investigation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_comment_payment_investigation_for_payment_investigation(client: TestClient):
    """Test case for list_all_comment_payment_investigation_for_payment_investigation

    
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
    #    "/payment-investigation/{payment-investigationID}/comment-payment-investigation".format(payment-investigationID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_comment_payment_investigation_for_payment_investigation(client: TestClient):
    """Test case for r_ead_comment_payment_investigation_for_payment_investigation

    
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
    #    "/payment-investigation/{payment-investigationID}/comment-payment-investigation/{itemId}".format(payment-investigationID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_comment_payment_investigation_for_payment_investigation(client: TestClient):
    """Test case for u_pdate_comment_payment_investigation_for_payment_investigation

    
    """
    admin_comment_payment_investigation = {"visibility":"visibility","text":"text","status":"status"}

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
    #    "/payment-investigation/{payment-investigationID}/comment-payment-investigation/{itemId}".format(payment-investigationID=56, itemId=56),
    #    headers=headers,
    #    json=admin_comment_payment_investigation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

