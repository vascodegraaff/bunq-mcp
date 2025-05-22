# bunq MCP Server

This project provides a minimal FastAPI server that demonstrates how to start an OAuth flow with bunq and call a single API endpoint.

## Usage

1. Install dependencies (from the `generated-fastapi/requirements.txt`).
2. Export the following environment variables:

```bash
export BUNQ_CLIENT_ID=<your client id>
export BUNQ_CLIENT_SECRET=<your client secret>
# Optional: specify a redirect url for OAuth callbacks
export BUNQ_REDIRECT_URI=http://localhost:8000/callback
```

3. Run the server:

```bash
uvicorn main:app --reload
```

4. Open `http://localhost:8000/login` in your browser to start the OAuth flow. After authorizing, bunq will redirect back to `/callback`. The access token is stored in memory for demo purposes.

5. Call `/me` to fetch the currently authenticated user from bunq's API.

This is a starting point. The rest of the bunq API can be generated using the provided swagger file in `swagger.json`.
