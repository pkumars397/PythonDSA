import requests
headers={
    "Authorization":"Bearer Your_Token",
}

params={
    "userId":1
}

response=requests.get("https://jsonplaceholder.typicode.com/posts",headers=headers,params=params)
print(response.json())