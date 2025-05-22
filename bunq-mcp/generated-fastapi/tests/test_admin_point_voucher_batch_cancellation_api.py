# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.admin_point_voucher_batch_cancellation import AdminPointVoucherBatchCancellation  # noqa: F401
from openapi_server.models.admin_point_voucher_batch_cancellation_create import AdminPointVoucherBatchCancellationCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_admin_point_voucher_batch_cancellation(client: TestClient):
    """Test case for c_reate_admin_point_voucher_batch_cancellation

    
    """
    admin_point_voucher_batch_cancellation = {"point_prize_id":0,"all_voucher":[{"voucher":"voucher"},{"voucher":"voucher"}]}

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
    #    "/admin-point-voucher-batch-cancellation",
    #    headers=headers,
    #    json=admin_point_voucher_batch_cancellation,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

