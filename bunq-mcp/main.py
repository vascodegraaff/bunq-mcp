import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from urllib.parse import urlencode
import httpx

app = FastAPI(title="bunq MCP Server")

BUNQ_CLIENT_ID = os.getenv("BUNQ_CLIENT_ID")
BUNQ_CLIENT_SECRET = os.getenv("BUNQ_CLIENT_SECRET")
BUNQ_REDIRECT_URI = os.getenv("BUNQ_REDIRECT_URI", "http://localhost:8000/callback")
OAUTH_AUTHORIZE_URL = "https://oauth.bunq.com/auth"
OAUTH_TOKEN_URL = "https://oauth.bunq.com/token"
API_BASE_URL = os.getenv("BUNQ_API_BASE_URL", "https://public-api.sandbox.bunq.com")

# In-memory token storage for demo purposes
access_token: str | None = None

@app.get("/login")
def login() -> RedirectResponse:
    if not BUNQ_CLIENT_ID:
        raise HTTPException(status_code=500, detail="BUNQ_CLIENT_ID not configured")
    params = {
        "client_id": BUNQ_CLIENT_ID,
        "redirect_uri": BUNQ_REDIRECT_URI,
        "response_type": "code",
    }
    return RedirectResponse(url=f"{OAUTH_AUTHORIZE_URL}?{urlencode(params)}")


@app.get("/callback")
async def oauth_callback(code: str):
    if not all([BUNQ_CLIENT_ID, BUNQ_CLIENT_SECRET]):
        raise HTTPException(status_code=500, detail="OAuth environment variables not set")
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": BUNQ_REDIRECT_URI,
        "client_id": BUNQ_CLIENT_ID,
        "client_secret": BUNQ_CLIENT_SECRET,
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(OAUTH_TOKEN_URL, data=data)
    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    token_payload = resp.json()
    global access_token
    access_token = token_payload.get("access_token")
    return JSONResponse(token_payload)


@app.get("/me")
async def get_me():
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    headers = {
        "X-Bunq-Client-Authentication": access_token,
        "User-Agent": "bunq-mcp-demo",
    }
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{API_BASE_URL}/v1/user", headers=headers)
    return JSONResponse(status_code=resp.status_code, content=resp.json())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
