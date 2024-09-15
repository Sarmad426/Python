"""
Calls Simple FastAPI api using requests library
"""

import requests

# First run the FastAPI app using uvicorn [`uvicorn main:app --reload`]


def greet_user(name: str):
    """
    Calls FastAPI api

    Parameters:
    name (str): Name to greet

    Returns:
    (json object): Greet message
    """
    API_URL = f"http://127.0.0.1:8000/{name}"
    response = requests.get(API_URL)
    msg = response.json()
    if response.status_code == 200:
        return msg
    return None


greet_name = input("Greet user with name: ")

greet_msg = greet_user(greet_name)

if greet_msg:
    print(greet_msg)
else:
    print("Something went wrong!")
