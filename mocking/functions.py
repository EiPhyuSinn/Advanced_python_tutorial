import requests 

def fetch_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}") 
    return response.json()["name"]

def greet_user(user_id):
    user_name = fetch_data(user_id)
    return f'Hello {user_name}'