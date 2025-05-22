import os
import requests
import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode

from dotenv import load_dotenv

load_dotenv()

BUNQ_API_URL = os.getenv("BUNQ_API_BASE_URL", "https://public-api.sandbox.bunq.com/v1/")
API_KEY = os.getenv("BUNQ_API_KEY")
DEVICE_DESCRIPTION = os.getenv("BUNQ_DEVICE_DESCRIPTION", "FastAPI Device")

# Paths for storing keys and tokens (for demo purposes, use secure storage in prod)
PRIVATE_KEY_PATH = "/tmp/bunq_private_key.pem"
PUBLIC_KEY_PATH = "/tmp/bunq_public_key.pem"
INSTALLATION_TOKEN_PATH = "/tmp/bunq_installation_token.json"
DEVICE_RESPONSE_PATH = "/tmp/bunq_device_response.json"
SESSION_TOKEN_PATH = "/tmp/bunq_session_token.json"


def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # Store private key
    with open(PRIVATE_KEY_PATH, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    # Store public key
    with open(PUBLIC_KEY_PATH, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    return private_key, public_key


def get_public_key_pem():
    if not os.path.exists(PUBLIC_KEY_PATH):
        generate_key_pair()
    with open(PUBLIC_KEY_PATH, "rb") as f:
        return f.read().decode("utf-8")


def sign_payload(payload: str) -> str:
    """
    Signs the payload with the private key and returns a base64 signature string for X-Bunq-Client-Signature.
    """
    with open(PRIVATE_KEY_PATH, "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None, backend=default_backend())
    signature = private_key.sign(
        payload.encode("utf-8"),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return b64encode(signature).decode()


def create_installation():
    public_key_pem = get_public_key_pem()
    payload = json.dumps({"client_public_key": public_key_pem})
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "postman",
        "X-Bunq-Language": "en_US",
        "X-Bunq-Region": "nl_NL",
        "X-Bunq-Client-Request-Id": "install-req-1",
        "X-Bunq-Geolocation": "0 0 0 0 000",
        "X-Bunq-Client-Signature": sign_payload(payload)
    }
    resp = requests.post(
        BUNQ_API_URL + "installation",
        headers=headers,
        data=payload
    )
    resp.raise_for_status()
    response_json = resp.json()["Response"]
    installation_id = response_json[0]["Id"]["id"]
    token = response_json[1]["Token"]["token"]
    server_public_key = response_json[2]["ServerPublicKey"]["server_public_key"]
    installation = {
        "id": installation_id,
        "token": token,
        "server_public_key": server_public_key
    }
    # Save all details
    with open(INSTALLATION_TOKEN_PATH, "w") as f:
        json.dump(installation, f)
    return installation


def get_installation_token():
    if not os.path.exists(INSTALLATION_TOKEN_PATH):
        create_installation()
    with open(INSTALLATION_TOKEN_PATH, "r") as f:
        return json.load(f)["token"]


def register_device():
    token = get_installation_token()
    url = "https://public-api.sandbox.bunq.com/v1/device-server"

    payload = json.dumps({
        "description": "Postman",
        "secret": "sandbox_c97b368ac41b4e6db802580c4fdea0c5456ab1e10f7800aadad1381c",
        "permitted_ips": [
            "*"
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache',
        'User-Agent': 'postman',
        'X-Bunq-Language': 'en_US',
        'X-Bunq-Region': 'nl_NL',
        'X-Bunq-Client-Request-Id': 'hCsYmrGEBqcjXleTIbqI',
        'X-Bunq-Geolocation': '0 0 0 0 000',
        # 'X-Bunq-Client-Authentication': '3c777ea04fdbf4243dd80612bd2e9acaa08b599df6a081190742e6c3b7ecc633',
        # 'X-Bunq-Client-Signature': 'LsPq9HCLSFPmU8T3WmtbMujpnmWoNwbfVYaC0mNvZHHi/Q2jvT4BxSDJnsHMFf2E3UgxByB2RddoP9y9e8SUdRJT9ysoLPO2O59GMc6FqX/1ujCKkRMGxFgwtswVv1evNvdOMFM+03ELrO5SSaCl9gnQm/9eQ8L2drBzMRYebnp5VFhnVs5KKNPp9dB2f5bG4FDMSqvGfu60dpYNOQWuJ1r0n1iKXvWESFq4GWLmkqUBZChENqEzUGkwNYDGjb36EoN3nbKrgwuM7M+9gQPplB41npzCYnos5Hh0RLrDeS4NcEhAiTKdFQB/cTqA/dR9u6P+KzgU+FZG28VUZStNug=='
        "X-Bunq-Client-Authentication": token,
        "X-Bunq-Client-Signature": sign_payload(payload)
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    # payload = json.dumps({
    #     "secret": API_KEY,
    #     "description": DEVICE_DESCRIPTION,
    #     "permitted_ips": ["*"]
    # })
    # headers = {
    #     "Content-Type": "application/json",
    #     "Cache-Control": "no-cache",
    #     "User-Agent": "postman",
    #     "X-Bunq-Language": "en_US",
    #     "X-Bunq-Region": "nl_NL",
    #     "X-Bunq-Client-Request-Id": "device-req-1",
    #     "X-Bunq-Geolocation": "0 0 0 0 000",
    #     "X-Bunq-Client-Authentication": token,
    #     "X-Bunq-Client-Signature": sign_payload(payload)
    # }
    # resp = requests.post(BUNQ_API_URL + "device-server", headers=headers, data=payload)
    # resp.raise_for_status()
    device_response = response.json()
    with open(DEVICE_RESPONSE_PATH, "w") as f:
        json.dump(device_response, f)
    return device_response


def create_session():
    token = get_installation_token()
    payload = json.dumps({"secret": API_KEY})
    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "User-Agent": "postman",
        "X-Bunq-Language": "en_US",
        "X-Bunq-Region": "nl_NL",
        "X-Bunq-Client-Request-Id": "session-req-1",
        "X-Bunq-Geolocation": "0 0 0 0 000",
        "X-Bunq-Client-Authentication": token,
        "X-Bunq-Client-Signature": sign_payload(payload)
    }
    resp = requests.post(BUNQ_API_URL + "session-server", headers=headers, data=payload)
    resp.raise_for_status()
    response_json = resp.json()["Response"]
    # Session token is usually in Response[1]["Token"]["token"]
    session_token = response_json[1]["Token"]["token"]
    session_response = {
        "session_token": session_token,
        "full_response": resp.json()
    }
    with open(SESSION_TOKEN_PATH, "w") as f:
        json.dump(session_response, f)
    return session_response


def get_session_token():
    if not os.path.exists(SESSION_TOKEN_PATH):
        create_session()
    with open(SESSION_TOKEN_PATH, "r") as f:
        return json.load(f)["session_token"]


def ensure_authenticated():
    """
    Ensures that installation, device, and session are created and returns a valid session token.
    """
    if not os.path.exists(INSTALLATION_TOKEN_PATH):
        create_installation()
    register_device()
    if not os.path.exists(SESSION_TOKEN_PATH):
        create_session()
    return get_session_token()
