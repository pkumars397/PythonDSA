import requests
data={
    "name": "morpheus",
    "job": "zion resident"
}

response=requests.patch("https://reqres.in/api/users/2",data)
print(response.status_code)
print(response.json())