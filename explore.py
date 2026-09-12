import httpx

SERVICES = {
    "booking": 3000,
    "room": 3001,
    "branding": 3002,
    "auth": 3004,
    "report": 3005,
    "message": 3006,
}


def probe(name: str, port: int) -> None:
    paths = [f"/{name}/", f"/{name}", "/"]

    print(f"\n--- {name} (port {port}) ---")

    for path in paths:
        url = f"http://localhost:{port}{path}"
        try:
            response = httpx.get(url, timeout=5.0)
            print(f"  {response.status_code}  GET {path}")
        except httpx.RequestError as error:
            print(f"  ERROR GET {path}: {error}")


for service_name, service_port in SERVICES.items():
    probe(service_name, service_port)
