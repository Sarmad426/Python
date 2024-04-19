"""
Calls Github users api and stores the data in csv file
"""

import requests


def get_github_user(username: str):
    """
    Gets the github user via api

    Parameters:
    username (str): Username of the github user

    Returns:
    user (json object): The github user's info as a json object. If not found, returns None
    """
    api_url = f"https://api.github.com/users/{username}"
    response = requests.get(api_url)
    user = response.json()
    if response.status_code == 200:
        return user
    return None


github_user_search = input("Search for Github user with username: ")

user = get_github_user(github_user_search)

if user:
    print(user)
else:
    print("No GitHub user found!")
