# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_top_up_method_configuration import BunqMeMerchantRequestTopUpMethodConfiguration  # noqa: F401
from openapi_server.models.bunq_me_merchant_request_top_up_method_configuration_create import BunqMeMerchantRequestTopUpMethodConfigurationCreate  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401


def test_c_reate_bunqme_merchant_request_top_up_method_configuration(client: TestClient):
    """Test case for c_reate_bunqme_merchant_request_top_up_method_configuration

    
    """
    bunq_me_merchant_request_top_up_method_configuration = {"bunqme_type":"bunqme_type","amount_requested":{"currency":"currency","value":"value"},"bunqme_uuid":"bunqme_uuid"}

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
    #    "/bunqme-merchant-request-top-up-method-configuration",
    #    headers=headers,
    #    json=bunq_me_merchant_request_top_up_method_configuration,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

