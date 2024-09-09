# erp_integration.py
import requests

class ERPIntegration:
    def __init__(self, api_url):
        self.api_url = api_url

    def send_data(self, data):
        response = requests.post(f"{self.api_url}/api/data", json=data)
        return response.status_code
