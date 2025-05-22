from bunq_auth import ensure_authenticated

if __name__ == "__main__":
    token = ensure_authenticated()
    print(f"Session token: {token}")

