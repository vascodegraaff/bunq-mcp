# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.export_statement_card_csv import ExportStatementCardCsv  # noqa: F401
from openapi_server.models.export_statement_card_csv_create import ExportStatementCardCsvCreate  # noqa: F401
from openapi_server.models.export_statement_card_csv_listing import ExportStatementCardCsvListing  # noqa: F401
from openapi_server.models.export_statement_card_csv_read import ExportStatementCardCsvRead  # noqa: F401


def test_c_reate_export_statement_card_csv_for_user_card(client: TestClient):
    """Test case for c_reate_export_statement_card_csv_for_user_card

    
    """
    export_statement_card_csv = {"date_start":"date_start","regional_format":"regional_format","date_end":"date_end"}

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
    #    "/user/{userID}/card/{cardID}/export-statement-card-csv".format(userID=56, cardID=56),
    #    headers=headers,
    #    json=export_statement_card_csv,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_export_statement_card_csv_for_user_card(client: TestClient):
    """Test case for d_elete_export_statement_card_csv_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/export-statement-card-csv/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_export_statement_card_csv_for_user_card(client: TestClient):
    """Test case for list_all_export_statement_card_csv_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/export-statement-card-csv".format(userID=56, cardID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_r_ead_export_statement_card_csv_for_user_card(client: TestClient):
    """Test case for r_ead_export_statement_card_csv_for_user_card

    
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
    #    "/user/{userID}/card/{cardID}/export-statement-card-csv/{itemId}".format(userID=56, cardID=56, itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

