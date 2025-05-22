# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.relation_user_company_ubo_batch_api_base import BaseRelationUserCompanyUboBatchApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.create1brn400_response import CREATE1brn400Response
from openapi_server.models.relation_user_company_ubo_batch import RelationUserCompanyUboBatch
from openapi_server.models.relation_user_company_ubo_batch_create import RelationUserCompanyUboBatchCreate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/user-company/{user-companyID}/relation-user-company-ubo-batch",
    responses={
        200: {"model": RelationUserCompanyUboBatchCreate, "description": "Manage the company person UBO details. apiApp:CREATE"},
        400: {"model": CREATE1brn400Response, "description": "This is how the error response looks like for 4XX response codes"},
    },
    tags=["relation-user-company-ubo-batch"],
    summary="",
    response_model_by_alias=True,
)
async def c_reate_relation_user_company_ubo_batch_for_user_company(
    user-companyID: StrictInt = Path(..., description=""),
    user_agent: Annotated[StrictStr, Field(description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header.")] = Header(None, description="The User-Agent header field should contain information about the user agent originating the request. There are no restrictions on the value of this header."),
    x_bunq_client_authentication: Annotated[StrictStr, Field(description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call")] = Header(None, description="The authentication token is used to authenticate the source of the API call. It is required by all API calls except for POST /v1/installation. It is important to note that the device and session calls are using the token from the response of the installation call, while all the other calls use the token from the response of the session-server call"),
    relation_user_company_ubo_batch: RelationUserCompanyUboBatch = Body(None, description=""),
    cache_control: Annotated[Optional[StrictStr], Field(description="The standard HTTP Cache-Control header is required for all signed requests.")] = Header(None, description="The standard HTTP Cache-Control header is required for all signed requests."),
    x_bunq_language: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US.")] = Header(None, description="The X-Bunq-Language header must contain a preferred language indication. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore. Currently only the languages en_US and nl_NL are supported. Anything else will default to en_US."),
    x_bunq_region: Annotated[Optional[StrictStr], Field(description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore.")] = Header(None, description="The X-Bunq-Region header must contain the region (country) of the client device. The value of this header is formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, separated by an underscore."),
    x_bunq_client_request_id: Annotated[Optional[StrictStr], Field(description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer.")] = Header(None, description="This header must specify an ID with each request that is unique for the logged in user. There are no restrictions for the format of this ID. However, the server will respond with an error when the same ID is used again on the same DeviceServer."),
    x_bunq_geolocation: Annotated[Optional[StrictStr], Field(description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued.")] = Header(None, description="This header must specify the geolocation of the device. The format of this value is longitude latitude altitude radius country. The country is expected to be formatted of an ISO 3166-1 alpha-2 country code. When no geolocation is available or known the header must still be included but can be zero valued."),
) -> RelationUserCompanyUboBatchCreate:
    """Manage the company person UBO details. apiApp:CREATE"""
    if not BaseRelationUserCompanyUboBatchApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRelationUserCompanyUboBatchApi.subclasses[0]().c_reate_relation_user_company_ubo_batch_for_user_company(user-companyID, user_agent, x_bunq_client_authentication, relation_user_company_ubo_batch, cache_control, x_bunq_language, x_bunq_region, x_bunq_client_request_id, x_bunq_geolocation)
