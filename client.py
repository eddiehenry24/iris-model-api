import json
from urllib.request import Request, urlopen

measurements = {"features": [5.1, 3.5, 1.4, 0.2]}
request = Request(
    "http://localhost:8000/predict",
    data=json.dumps(measurements).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request, timeout=10) as response:
    print(json.dumps(json.load(response)))
