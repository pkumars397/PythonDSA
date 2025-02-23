import requests
data={
    "name": "morpheus",
    "job": "zion resident"
}
response=requests.put("https://reqres.in/api/users/2",json=data)
print(response.status_code)
print(response.json())