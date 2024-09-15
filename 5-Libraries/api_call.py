"""
Calls Simple FastAPI api using requests library
"""

import requests

from requests.exceptions import RequestException

# First run the FastAPI app using uvicorn [`uvicorn main:app --reload`]


def greet_user(name: str):
    """
    Calls FastAPI api. Greets user with name

    Parameters:
    name (str): Name to greet

    Returns:
    (json object): Greet message
    """
    try:
        api_url = f"http://127.0.0.1:8000/{name}"
        response = requests.get(api_url, timeout=5)
        msg = response.json()
        if response.status_code == 200:
            return msg
    except RequestException as req_err:
        print(f"Connection error: {req_err}")
        return None


greet_name = input("Greet user with name: ").strip()

greet_msg = greet_user(greet_name)

if greet_msg:
    print(greet_msg)
else:
    print("Something went wrong!")
