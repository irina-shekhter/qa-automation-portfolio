import httpx

PUBLIC_ENDPOINTS = [
    ("room", 3001, "/room/"),
    ("branding", 3002, "/branding/"),
    ("message", 3006, "/message/"),
]

if __name__ == "__main__":
    for name, port, path in PUBLIC_ENDPOINTS:
        response = httpx.get(f"http://localhost:{port}{path}", timeout=5.0)

        print(f"\n{'=' * 50}")
        print(f"{name}  {response.status_code}  {path}")
        print(f"{'=' * 50}")
        print(response.text[:800])
