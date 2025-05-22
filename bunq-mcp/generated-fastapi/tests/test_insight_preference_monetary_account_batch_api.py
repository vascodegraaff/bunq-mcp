# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.insight_preference_monetary_account_batch import InsightPreferenceMonetaryAccountBatch  # noqa: F401
from openapi_server.models.insight_preference_monetary_account_batch_create import InsightPreferenceMonetaryAccountBatchCreate  # noqa: F401


def test_c_reate_insight_preference_monetary_account_batch_for_user(client: TestClient):
    """Test case for c_reate_insight_preference_monetary_account_batch_for_user

    
    """
    insight_preference_monetary_account_batch = {"all_decree_insight_preference_monetary_account":[{"monetary_account_id":0,"category":"category"},{"monetary_account_id":0,"category":"category"}]}

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
    #    "/user/{userID}/insight-preference-monetary-account-batch".format(userID=56),
    #    headers=headers,
    #    json=insight_preference_monetary_account_batch,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

