# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.user_review_value_text import UserReviewValueText  # noqa: F401
from openapi_server.models.user_review_value_text_update import UserReviewValueTextUpdate  # noqa: F401


def test_u_pdate_value_text_for_user_review_check(client: TestClient):
    """Test case for u_pdate_value_text_for_user_review_check

    
    """
    user_review_value_text = {"content":"content"}

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
    #    "/user/{userID}/review/{reviewID}/check/{checkID}/value-text/{itemId}".format(userID=56, reviewID=56, checkID=56, itemId=56),
    #    headers=headers,
    #    json=user_review_value_text,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

