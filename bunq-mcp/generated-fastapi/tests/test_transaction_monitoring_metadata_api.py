# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.transaction_monitoring_metadata import TransactionMonitoringMetadata  # noqa: F401
from openapi_server.models.transaction_monitoring_metadata_listing import TransactionMonitoringMetadataListing  # noqa: F401
from openapi_server.models.transaction_monitoring_metadata_read import TransactionMonitoringMetadataRead  # noqa: F401
from openapi_server.models.transaction_monitoring_metadata_update import TransactionMonitoringMetadataUpdate  # noqa: F401
from openapi_server.models.transaction_monitoring_metadata_user_listing import TransactionMonitoringMetadataUserListing  # noqa: F401


def test_list_all_transaction_monitoring_metadata(client: TestClient):
    """Test case for list_all_transaction_monitoring_metadata

    
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
    #    "/transaction-monitoring-metadata",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_transaction_monitoring_metadata_for_user(client: TestClient):
    """Test case for list_all_transaction_monitoring_metadata_for_user

    
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
    #    "/user/{userID}/transaction-monitoring-metadata".format(userID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_transaction_monitoring_metadata(client: TestClient):
    """Test case for r_ead_transaction_monitoring_metadata

    
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
    #    "/transaction-monitoring-metadata/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_transaction_monitoring_metadata(client: TestClient):
    """Test case for u_pdate_transaction_monitoring_metadata

    
    """
    transaction_monitoring_metadata = {"indicator":["indicator","indicator"],"date":"date","user_admin_id":0,"external_url":"external_url","user_id":"user_id","label_user_admin":{"country":"country","public_nick_name":"public_nick_name","avatar":{"anchor_uuid":"anchor_uuid","image":[{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1},{"content_type":"content_type","attachment_public_uuid":"attachment_public_uuid","width":5,"height":1}],"style":"style","uuid":"uuid"},"display_name":"display_name","uuid":"uuid"},"origin":["origin","origin"],"fiu_report_supported_reason":"fiu_report_supported_reason","description":"description","user_extension_type":"user_extension_type","status":"status"}

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
    #    "/transaction-monitoring-metadata/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=transaction_monitoring_metadata,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

