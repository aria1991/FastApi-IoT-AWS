# FastApi-IoT-AWS
Using FASTAPI for sending patients vital signs real-time data from an IoT network to AWS cloud


#### Base code
```python
import boto3
from fastapi import FastAPI

app = FastAPI()

# Define a model for the patients' vital signs data being sent to the AWS cloud
class VitalSignsModel(BaseModel):
    patient_id: str
    heart_rate: int
    blood_pressure: int
    respiration_rate: int
    temperature: float

@app.post("/send-vital-signs")
def send_vital_signs(data: VitalSignsModel):
    # Connect to AWS cloud
    client = boto3.client('sns')

    # Publish the data to the specified topic
    response = client.publish(
        TopicArn='arn:aws:sns:us-east-1:123456789012:VitalSignsTopic',
        Message=data.json()
    )

    return response

```

This code creates a FastAPI app with a single endpoint that accepts a` POST` request with a JSON payload containing the patients' vital signs data to be sent to the AWS cloud. The `send_vital_signs` function uses the boto3 library to connect to the AWS cloud and publish the data to a specified SNS (Simple Notification Service) topic.

>  We can modify this base code modify it to suit our specific use case. For example, you may want to add authentication, validate the data being sent, or handle errors appropriately. For more info check `Dep.py` script.

You can then use this endpoint to send data from your IoT network to the AWS cloud in real-time by making `POST` requests to this endpoint with the data as the request payload.

#### Testing: 

```python
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

```

This code defines the data to be sent and makes a `POST` request to the endpoint with the data as the request payload and the API key as a header. The endpoint will validate the API key and the data, and if both are valid, will publish the data to the specified SNS topic in the AWS cloud.


> You can modify this code to suit our specific use case by changing the `endpoint URL`, the `data being sent`, and the `API key` as needed. Check the `Utest.py` for a detailed test script.
