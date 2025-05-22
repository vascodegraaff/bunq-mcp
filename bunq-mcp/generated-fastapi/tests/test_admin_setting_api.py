# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_admin_setting import UserAdminSetting  # noqa: F401
from openapi_server.models.user_admin_setting_create import UserAdminSettingCreate  # noqa: F401
from openapi_server.models.user_admin_setting_listing import UserAdminSettingListing  # noqa: F401
from openapi_server.models.user_admin_setting_update import UserAdminSettingUpdate  # noqa: F401


def test_c_reate_admin_setting_for_user_admin(client: TestClient):
    """Test case for c_reate_admin_setting_for_user_admin

    
    """
    user_admin_setting = {"play_sound_for_new_orphan":"play_sound_for_new_orphan","play_sound_for_new_user_approval":"play_sound_for_new_user_approval","display_monitoring_hits_in_sidebar":"display_monitoring_hits_in_sidebar","display_ticket_counts_in_homepage":"display_ticket_counts_in_homepage","display_open_chats_count_in_sidebar":"display_open_chats_count_in_sidebar"}

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
    #    "/user-admin/{user-adminID}/admin-setting".format(user-adminID=56),
    #    headers=headers,
    #    json=user_admin_setting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_list_all_admin_setting_for_user_admin(client: TestClient):
    """Test case for list_all_admin_setting_for_user_admin

    
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
    #    "/user-admin/{user-adminID}/admin-setting".format(user-adminID=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_u_pdate_admin_setting_for_user_admin(client: TestClient):
    """Test case for u_pdate_admin_setting_for_user_admin

    
    """
    user_admin_setting = {"play_sound_for_new_orphan":"play_sound_for_new_orphan","play_sound_for_new_user_approval":"play_sound_for_new_user_approval","display_monitoring_hits_in_sidebar":"display_monitoring_hits_in_sidebar","display_ticket_counts_in_homepage":"display_ticket_counts_in_homepage","display_open_chats_count_in_sidebar":"display_open_chats_count_in_sidebar"}

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
    #    "/user-admin/{user-adminID}/admin-setting/{itemId}".format(user-adminID=56, itemId=56),
    #    headers=headers,
    #    json=user_admin_setting,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

