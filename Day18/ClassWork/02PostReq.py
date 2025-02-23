import requests
data={
    "name": "morpheus",
    "job": "leader"
}

response=requests.post("https://reqres.in/api/users",json=data)
data2={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
response2=requests.post("https://reqres.in/api/register",json=data2)

print(f"Response1 StatusCode: {response.status_code} Response2 StatusCode: {response2.status_code}")
print(f"Response1: {response.json()} Response2: {response2.json()}")