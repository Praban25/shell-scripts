import requests
base_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=base_url)
print(dir(response))
print(response.json())
for key,value in response.json().items():
    print(key,value)

for key,value in response.json().items():    
    if key == "completed":
        if value == False:
            print("The data is incomplete")

for key,value in response.json().items():            
    if key == "userId":
        if value in [1,2,3,4]:
            print("User found")        
            
            
        
