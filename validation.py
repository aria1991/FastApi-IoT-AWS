import requests

# Set the endpoint URL and the API key
endpoint_url = "http://localhost:8000/send-vital-signs"
api_key = "my-secret-api-key"

# Define the data to be sent
data = {
    "patient_id": "12345",
    "heart_rate": 80,
    "blood_pressure": 120,
    "respiration_rate": 20,
    "temperature": 37.5
}

# Make the POST request to the endpoint with the data and the API key
response = requests.post(endpoint_url, json=data, headers={"X-API-KEY": api_key})

# Print the response
print(response.status_code)
print(response.json())
