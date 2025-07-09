
"""
Replay a saved webhook payload against your local Operator endpoint.
"""
import os, json, requests

OPERATOR_URL = os.getenv("OPERATOR_URL", "http://localhost:8080/webhook")
with open(os.path.join(os.path.dirname(__file__), "sample_payload.json")) as f:
    data = json.load(f)

resp = requests.post(OPERATOR_URL, json=data, timeout=5)
print("Status:", resp.status_code)
print("Body:", resp.text)
