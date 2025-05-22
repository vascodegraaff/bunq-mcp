import os
import httpx
import logging

BUNQ_API_KEY = os.getenv("BUNQ_API_KEY")
BUNQ_API_BASE_URL = os.getenv("BUNQ_API_BASE_URL", "https://public-api.sandbox.bunq.com")
logger = logging.getLogger("bunq-mcp")

async def forward_to_bunq(method: str, endpoint: str, headers=None, json=None, params=None):
    url = f"{BUNQ_API_BASE_URL}{endpoint}"
    bunq_headers = {
        "X-Bunq-Client-Authentication": BUNQ_API_KEY,
        **(headers or {})
    }
    logger.info(f"Forwarding {method} request to {url}")
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method,
            url,
            headers=bunq_headers,
            json=json,
            params=params,
        )
    logger.info(f"bunq API response: {response.status_code}")
    return response
