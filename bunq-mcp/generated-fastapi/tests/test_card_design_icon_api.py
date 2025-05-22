# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.card_design_icon import CardDesignIcon  # noqa: F401
from openapi_server.models.card_design_icon_create import CardDesignIconCreate  # noqa: F401
from openapi_server.models.card_design_icon_listing import CardDesignIconListing  # noqa: F401
from openapi_server.models.card_design_icon_update import CardDesignIconUpdate  # noqa: F401


def test_c_reate_card_design_icon(client: TestClient):
    """Test case for c_reate_card_design_icon

    
    """
    card_design_icon = {"category_id":0,"rank_popularity":6,"attachment_svg_uuid":"attachment_svg_uuid","name":"name","attachment_pdf_uuid":"attachment_pdf_uuid"}

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
    #    "/card-design-icon",
    #    headers=headers,
    #    json=card_design_icon,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_d_elete_card_design_icon(client: TestClient):
    """Test case for d_elete_card_design_icon

    
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
    #    "/card-design-icon/{itemId}".format(itemId=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_card_design_icon(client: TestClient):
    """Test case for list_all_card_design_icon

    
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
    #    "/card-design-icon",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_card_design_icon(client: TestClient):
    """Test case for u_pdate_card_design_icon

    
    """
    card_design_icon = {"category_id":0,"rank_popularity":6,"attachment_svg_uuid":"attachment_svg_uuid","name":"name","attachment_pdf_uuid":"attachment_pdf_uuid"}

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
    #    "/card-design-icon/{itemId}".format(itemId=56),
    #    headers=headers,
    #    json=card_design_icon,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

