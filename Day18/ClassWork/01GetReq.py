import requests

response=requests.get("https://reqres.in/api/users?page=2") #Using this we fetch the response from server
requests.post("https://reqres.in/api/users")
print(response.status_code) #We get status code of our response
print(response.json()) #We get our response in printable format(json object)