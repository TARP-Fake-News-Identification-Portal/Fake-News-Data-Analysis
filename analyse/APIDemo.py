import requests

payload = {"data": "hello world"}
response = requests.post("http://127.0.0.1:8080/predict", json=payload)
print(response.json())
