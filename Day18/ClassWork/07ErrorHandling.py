import requests
try:
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1000")()
    response.raise_for_status() #raise exception fro http errors
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")