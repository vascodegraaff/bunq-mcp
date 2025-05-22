# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.session_server_api_base import BaseSessionServerApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.create1brn400_response import CREATE1brn400Response
from openapi_server.models.session_server import SessionServer
from openapi_server.models.session_server_create import SessionServerCreate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/session-server",
    responses={
        200: {"model": SessionServerCreate, "description": "Once you have created an Installation and a DeviceServer with that Installation, then you are ready to start a session! A session expires after the same amount of time you have set for Auto Logout in your user account. By default this is 1 week. If a request is made 30 seconds before a session expires, it will be extended from that moment by your auto logout time, but never by more than 5 minutes. apiAdmin:CREATE apiPublic:CREATE apiServiceInternal:CREATE apiProcess:CREATE apiTranslink:CREATE"},
        400: {"model": CREATE1brn400Response, "description": "This is how the error response looks like for 4XX response codes"},
    },
    tags=["session-server"],
    summary="",
    response_model_by_alias=True,
)
async def c_reate_session_server(
    user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")] = Header(None, description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header."),
    x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")] = Header(None, description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call"),
    session_server: SessionServer = Body(None, description=""),
    cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")] = Header(None, description="The standard HTTP Cache-Control header is required for all signed requests."),
    x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")] = Header(None, description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US."),
    x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")] = Header(None, description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore."),
    x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")] = Header(None, description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer."),
    x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")] = Header(None, description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued."),
) -> SessionServerCreate:
    """Create a new session for a DeviceServer. Provide the Installation token in the \&quot;X-Bunq-Client-Authentication\&quot; header. And don&#39;t forget to create the \&quot;X-Bunq-Client-Signature\&quot; header. The response contains a Session token that should be used for as the \&quot;X-Bunq-Client-Authentication\&quot; header for all future API calls. The ip address making this call needs to match the ip address bound to your API key."""
    if not BaseSessionServerApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseSessionServerApi.subclasses[0]().c_reate_session_server(user_agent, x_bunq_client_authentication, session_server, cache_control, x_bunq_language, x_bunq_region, x_bunq_client_request_id, x_bunq_geolocation)
