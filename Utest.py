import unittest
import requests

class TestSendVitalSigns(unittest.TestCase):
    def setUp(self):
        # Set the endpoint URL and the API key
        self.endpoint_url = "http://localhost:8000/send-vital-signs"
        self.api_key = "my-secret-api-key"

    def test_send_vital_signs(self):
        # Define the data to be sent
        data = {
            "patient_id": "12345",
            "heart_rate": 80,
            "blood_pressure": 120,
            "respiration_rate": 20,
            "temperature": 37.5
        }

        # Make the POST request to the endpoint with the data and the API key
        response = requests.post(self.endpoint_url, json=data, headers={"X-API-KEY": self.api_key})

        # Assert that the request was successful
        self.assertEqual(response.status_code, 200)

    def test_invalid_api_key(self):
        # Define the data to be sent
        data = {
            "patient_id": "12345",
            "heart_rate": 80,
            "blood_pressure": 120,
            "respiration_rate": 20,
            "temperature": 37.5
        }

        # Make the POST request to the endpoint with the data and an invalid API key
        response = requests.post(self.endpoint_url, json=data, headers={"X-API-KEY": "invalid-api-key"})

        # Assert that the request returned a 401 status code
        self.assertEqual(response.status_code, 401)

    def test_invalid_data(self):
        # Define the data to be sent with an invalid heart rate value
        data = {
            "patient_id": "12345",
            "heart_rate": 300,
            "blood_pressure": 120,
            "respiration_rate": 20,
            "temperature": 37.5
        }

        # Make the POST request to the endpoint with the data and the API key
        response = requests.post(self.endpoint_url, json=data, headers={"X-API-KEY": self.api_key})

        # Assert that the request returned a 400 status code
        self.assertEqual(response.status_code, 400)

    def test_missing_api_key(self):
        # Define the data to be sent
        data = {
            "patient_id": "12345",
            "heart_rate": 80,
            "blood_pressure": 120,
            "respiration_rate": 20,
            "temperature": 37.5
        }

        # Make the POST request to the endpoint with the data and no API key
        response = requests.post(self.endpoint_url, json=data)

        # Assert that the request returned a 401 status code
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
