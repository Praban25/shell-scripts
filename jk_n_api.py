import requests

base_url = "https://icanhazdadjoke.com/"
headers = {
    "Accept": "application/json"
}

response = requests.get(url=base_url)
print(dir(response))
print(type(headers))

def dad_jk():
    response = requests.get(base_url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(data["joke"])
    else:
        print(f"Failed to joke. Check Status {response.status_code}")
        
dad_jk()




