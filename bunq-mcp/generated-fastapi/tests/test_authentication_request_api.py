# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.create1brn400_response import CREATE1brn400Response  # noqa: F401
from openapi_server.models.master_card_identity_check_authentication_request import MasterCardIdentityCheckAuthenticationRequest  # noqa: F401
from openapi_server.models.master_card_identity_check_authentication_request_create import MasterCardIdentityCheckAuthenticationRequestCreate  # noqa: F401


def test_c_reate_authentication_request(client: TestClient):
    """Test case for c_reate_authentication_request

    
    """
    master_card_identity_check_authentication_request = {"message_category":"messageCategory","mcc":"mcc","merchant_name":"merchantName","merchant_risk_indicator":["merchantRiskIndicator","merchantRiskIndicator"],"three_ds_requestor_authentication_ind":"threeDSRequestorAuthenticationInd","addr_match":"addrMatch","message_type":"messageType","sdk_reference_number":"sdkReferenceNumber","three_ds_requestor_name":"threeDSRequestorName","acquirer_merchant_id":"acquirerMerchantID","sdk_app_id":"sdkAppID","ship_addr_post_code":"shipAddrPostCode","message_extension":["messageExtension","messageExtension"],"bill_addr_country":"billAddrCountry","broad_info":{"message":"message"},"home_phone":["homePhone","homePhone"],"pay_token_ind":1,"bill_addr_line2":"billAddrLine2","bill_addr_line3":"billAddrLine3","device_channel":"deviceChannel","device_info":"deviceInfo","bill_addr_line1":"billAddrLine1","ds_reference_number":"dsReferenceNumber","acct_info":["acctInfo","acctInfo"],"purchase_exponent":"purchaseExponent","mobile_phone":["mobilePhone","mobilePhone"],"ship_addr_city":"shipAddrCity","trans_type":"transType","three_ds_requestor_authentication_info":["threeDSRequestorAuthenticationInfo","threeDSRequestorAuthenticationInfo"],"ds_trans_id":"dsTransID","acct_type":"acctType","ship_addr_country":"shipAddrCountry","three_ds_requestor_prior_authentication_info":["threeDSRequestorPriorAuthenticationInfo","threeDSRequestorPriorAuthenticationInfo"],"three_ds_server_trans_id":"threeDSServerTransID","purchase_date":"purchaseDate","recurring_frequency":"recurringFrequency","merchant_country_code":"merchantCountryCode","three_ds_server_ref_number":"threeDSServerRefNumber","bill_addr_state":"billAddrState","acct_id":"acctID","purchase_currency":"purchaseCurrency","card_expiry_date":"cardExpiryDate","sdk_ephem_pub_key":["sdkEphemPubKey","sdkEphemPubKey"],"ship_addr_state":"shipAddrState","recurring_expiry":"recurringExpiry","ship_addr_line3":"shipAddrLine3","ship_addr_line2":"shipAddrLine2","three_ds_requestor_url":"threeDSRequestorURL","acct_number":"acctNumber","ship_addr_line1":"shipAddrLine1","ds_url":"dsURL","message_version":"messageVersion","bill_addr_post_code":"billAddrPostCode","sdk_trans_id":"sdkTransID","email":"email","sdk_max_timeout":"sdkMaxTimeout","purchase_instal_data":"purchaseInstalData","three_ds_requestor_id":"threeDSRequestorID","acquirer_bin":"acquirerBIN","bill_addr_city":"billAddrCity","device_render_options":["deviceRenderOptions","deviceRenderOptions"],"purchase_amount":"purchaseAmount","three_ds_requestor_challenge_ind":"threeDSRequestorChallengeInd","cardholder_name":"cardholderName","pay_token_source":"payTokenSource","three_ds_server_operator_id":"threeDSServerOperatorID","work_phone":["workPhone","workPhone"],"three_ds_server_url":"threeDSServerURL"}

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
    #    "/authentication-request",
    #    headers=headers,
    #    json=master_card_identity_check_authentication_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

