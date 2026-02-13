import requests

BASE_URL = "http://127.0.0.1:5000"

# -----------------------
# TEST GET /hello
# -----------------------
response = requests.get(f"{BASE_URL}/hello")
print("GET /hello")
print("Status Code:", response.status_code)
print("Response:", response.json())
print()

# -----------------------
# TEST POST /hello
# -----------------------
response = requests.post(
    f"{BASE_URL}/hello",
    json={"name": "Carlos"}
)
print("POST /hello")
print("Status Code:", response.status_code)
print("Response:", response.json())
print()

# -----------------------
# TEST GET /data
# -----------------------
response = requests.get(f"{BASE_URL}/data")
print("GET /data")
print("Status Code:", response.status_code)
print("Response:", response.json())
print()

# -----------------------
# TEST POST /data
# -----------------------
response = requests.post(
    f"{BASE_URL}/data",
    json={"name": "Maria", "role": "Tester"}
)
print("POST /data")
print("Status Code:", response.status_code)
print("Response:", response.json())
print()
