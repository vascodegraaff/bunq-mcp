# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.bunq_me_fundraiser_profile_entry_payment_create import BunqMeFundraiserProfileEntryPaymentCreate
from openapi_server.models.bunq_me_tab_entry_payment import BunqMeTabEntryPayment
from openapi_server.models.bunq_me_tab_entry_payment_create import BunqMeTabEntryPaymentCreate
from openapi_server.models.create1brn400_response import CREATE1brn400Response
from openapi_server.models.credit_line_repayment_payment_listing import CreditLineRepaymentPaymentListing
from openapi_server.models.payment import Payment
from openapi_server.models.payment_create import PaymentCreate
from openapi_server.models.payment_listing import PaymentListing
from openapi_server.models.payment_read import PaymentRead
from openapi_server.models.payment_update import PaymentUpdate


class BasePaymentApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePaymentApi.subclasses = BasePaymentApi.subclasses + (cls,)
    async def c_reate_payment_for_user_monetary_account(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        payment: Payment,
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> PaymentCreate:
        """Create a new Payment."""
        ...


    async def c_reate_payment_for_user_monetary_account_bunqme_fundraiser_profile_entry(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        bunqme-fundraiser-profile-entryID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        body: Dict[str, Any],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> BunqMeFundraiserProfileEntryPaymentCreate:
        """payment to a bunq.me public profile. apiApp:CREATE"""
        ...


    async def c_reate_payment_for_user_monetary_account_bunqme_tab_entry(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        bunqme-tab-entryID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        bunq_me_tab_entry_payment: BunqMeTabEntryPayment,
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> BunqMeTabEntryPaymentCreate:
        """Used to pay a bunq.me tab entry. apiApp:CREATE"""
        ...


    async def list_all_payment_for_user_activity_map_place(
        self,
        userID: StrictInt,
        activity-map-placeID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> List[object]:
        """Returns payments for a place. apiApp:LISTING"""
        ...


    async def list_all_payment_for_user_credit_line_repayment(
        self,
        userID: StrictInt,
        credit-lineID: StrictInt,
        repaymentID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> List[CreditLineRepaymentPaymentListing]:
        """Get the payments made to repay this credit line repayment. apiAdmin:LISTING apiApp:LISTING"""
        ...


    async def list_all_payment_for_user_monetary_account(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> List[PaymentListing]:
        """Get a listing of all Payments performed on a given MonetaryAccount (incoming and outgoing)."""
        ...


    async def list_all_payment_for_user_monetary_account_mastercard_action(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        mastercard-actionID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> List[object]:
        """MasterCard transaction view. apiAdmin:LISTING apiApp:LISTING apiPublic:LISTING apiServiceInternal:LISTING"""
        ...


    async def r_ead_payment_for_user_monetary_account(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        itemId: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> PaymentRead:
        """Get a specific previous Payment."""
        ...


    async def u_pdate_payment_for_user_monetary_account(
        self,
        userID: StrictInt,
        monetary-accountID: StrictInt,
        itemId: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        payment: Payment,
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> PaymentUpdate:
        """Using Payment, you can send payments to bunq and non-bunq users from your bunq MonetaryAccounts. This can be done using bunq Aliases or IBAN Aliases. When transferring money to other bunq MonetaryAccounts you can also refer to Attachments. These will be received by the counter-party as part of the Payment. You can also retrieve a single Payment or all executed Payments of a specific monetary account. apiAdmin:READ/UPDATE/LISTING apiApp:CREATE/READ/UPDATE/LISTING apiPublic:CREATE/READ/LISTING apiServiceInternal:READ/UPDATE/LISTING"""
        ...
