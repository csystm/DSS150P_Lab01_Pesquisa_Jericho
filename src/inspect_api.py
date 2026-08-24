import json
from datetime import datetime, timezone
from pathlib import Path

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

# Paths
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)
SNAPSHOT_PATH = RAW_DIR / "api_snapshot.json"
INVENTORY_PATH = Path("docs/source_inventory.md")

# Send GET request
print(f"Requesting: {API_URL}")
response = requests.get(API_URL, timeout=20)
response.raise_for_status()  # fail clearly if HTTP error

# Status and content type
print(f"HTTP status code: {response.status_code}")
print(f"Content-Type: {response.headers.get('Content-Type')}")

# Parse JSON
payload = response.json()

# Determine top-level structure
top_type = type(payload).__name__
print(f"Top-level JSON type: {top_type}")

# Print number of records if possible
if isinstance(payload, list):
    num_records = len(payload)
    print(f"Number of records: {num_records}")
    sample_record = payload[0] if num_records > 0 else None
elif isinstance(payload, dict):
    print("Top-level keys:", list(payload.keys()))
    # Try to find a list value inside the dict
    list_key = None
    for key, value in payload.items():
        if isinstance(value, list):
            list_key = key
            num_records = len(value)
            print(f"Number of records under key '{key}': {num_records}")
            sample_record = value[0] if num_records > 0 else None
            break
    if list_key is None:
        num_records = 1  # the object itself is one record
        sample_record = payload
else:
    num_records = "Unknown"
    sample_record = payload

if sample_record is not None:
    print("\nSample record:")
    print(json.dumps(sample_record, indent=2, ensure_ascii=False))
else:
    print("\nNo sample record available.")

# Save raw response exactly as parsed JSON (equivalent)
with open(SNAPSHOT_PATH, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print(f"\nSnapshot saved to: {SNAPSHOT_PATH}")

# Record retrieval timestamp in UTC
retrieved_at = datetime.now(timezone.utc).isoformat()
print(f"Retrieved at (UTC): {retrieved_at}")