import requests

url = "http://localhost:5000/wallet/transact"

payload = "{\"recipient\":\"bar\",\"amount\":95}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
