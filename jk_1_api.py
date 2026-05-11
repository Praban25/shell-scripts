import requests

base_url = "https://xkcd.com/info.0.json"

response = requests.get(url=base_url)
print(response.json())

for key,value in response.json().items():
    print(key,value)
    
if response.status_code == 200:
    data = response.json()
    print(data["alt"])