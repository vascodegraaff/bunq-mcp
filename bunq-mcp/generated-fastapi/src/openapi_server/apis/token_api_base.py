# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server.models.create1brn400_response import CREATE1brn400Response
from openapi_server.models.master_card_wallet_token import MasterCardWalletToken
from openapi_server.models.master_card_wallet_token_create import MasterCardWalletTokenCreate
from openapi_server.models.master_card_wallet_token_listing import MasterCardWalletTokenListing
from openapi_server.models.master_card_wallet_token_read import MasterCardWalletTokenRead
from openapi_server.models.master_card_wallet_token_update import MasterCardWalletTokenUpdate
from openapi_server.models.oauth_token_create import OauthTokenCreate
from openapi_server.models.token_listing import TokenListing


class BaseTokenApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTokenApi.subclasses = BaseTokenApi.subclasses + (cls,)
    async def c_reate_token(
        self,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        body: Dict[str, Any],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> OauthTokenCreate:
        """Used to get API keys from Authorization Codes. apiOauth:CREATE"""
        ...


    async def c_reate_token_for_user_wallet(
        self,
        userID: StrictInt,
        walletID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        master_card_wallet_token: MasterCardWalletToken,
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> MasterCardWalletTokenCreate:
        """Initiate tokenization for a card."""
        ...


    async def list_all_token_for_user_card(
        self,
        userID: StrictInt,
        cardID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> List[TokenListing]:
        """Endpoint for retrieving details about the card required for tokenisation. apiApp:LISTING"""
        ...


    async def list_all_token_for_user_wallet(
        self,
        userID: StrictInt,
        walletID: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> List[MasterCardWalletTokenListing]:
        """List the tokens for the wallet."""
        ...


    async def r_ead_token_for_user_wallet(
        self,
        userID: StrictInt,
        walletID: StrictInt,
        itemId: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> MasterCardWalletTokenRead:
        """Manage the tokens in a wallet app. apiAdmin:LISTING/READ/UPDATE apiApp:CREATE/UPDATE/LISTING/READ apiServiceInternal:LISTING/READ/UPDATE"""
        ...


    async def u_pdate_token_for_user_wallet(
        self,
        userID: StrictInt,
        walletID: StrictInt,
        itemId: StrictInt,
        user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")],
        x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")],
        master_card_wallet_token: MasterCardWalletToken,
        cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")],
        x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")],
        x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")],
        x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")],
        x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")],
    ) -> MasterCardWalletTokenUpdate:
        """Update tokenization status and settings for a card."""
        ...
