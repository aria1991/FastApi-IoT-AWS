import boto3
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from fastapi.security import APIKeyHeader

app = FastAPI()

# Define a model for the patients' vital signs data being sent to the AWS cloud
class VitalSignsModel(BaseModel):
    patient_id: str
    heart_rate: int
    blood_pressure: int
    respiration_rate: int
    temperature: float

# Define a function to validate the API key
def validate_api_key(api_key: str = Header(None)):
    if api_key != "my-secret-api-key":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/send-vital-signs")
def send_vital_signs(data: VitalSignsModel, api_key: str = Depends(validate_api_key)):
    # Validate the data being sent
    if data.heart_rate < 0 or data.heart_rate > 200:
        raise HTTPException(status_code=400, detail="Invalid heart rate value")
    if data.blood_pressure < 0 or data.blood_pressure > 300:
        raise HTTPException(status_code=400, detail="Invalid blood pressure value")
    if data.respiration_rate < 0 or data.respiration_rate > 100:
        raise HTTPException(status_code=400, detail="Invalid respiration rate value")
    if data.temperature < 34 or data.temperature > 42:
        raise HTTPException(status_code=400, detail="Invalid temperature value")

    # Connect to AWS cloud
    try:
        client = boto3.client('sns')
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error connecting to AWS cloud")

    # Publish the data to the specified topic
    try:
        response = client.publish(
            TopicArn='arn:aws:sns:us-east-1:123456789012:VitalSignsTopic',
            Message=data.json()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error publishing data to AWS cloud")

    return response
