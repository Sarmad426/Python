"""
Calls Github users api and stores the data in csv file
"""

import requests

github_user_search = input("Search for Github user with username: ")

api_url = f"https://api.github.com/users/{github_user_search}"


response = requests.get(api_url)
user = response.json()

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    print(user)
else:
    print("Error 401")
