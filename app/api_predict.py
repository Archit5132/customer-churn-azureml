import requests
import json

input_payload = json.dumps({
  "data": [{
    "Gender": 1,
    "Age": 35,
    "MonthlyCharges": 85.0,
    "TotalCharges": 2300.0
  }]
})

url = "https://<your-azure-endpoint>.azurewebsites.net/score"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <token>"
}

response = requests.post(url, data=input_payload, headers=headers)
print(response.json())
