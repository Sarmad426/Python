"""
Practice Programs for lambda functions
"""

import csv
from typing import Any, List, Tuple, Union


type_user_data = Union[List[Tuple[str, str, int]], Any]


def write_csv(file_path: str, user_data: type_user_data) -> None:
    """
    Write User info to csv file

    It takes two parameters
        file_path : type string, refers to the csv file path
        user_data : type dictionary, refer to the user details
    """
    COLUMNS: List[str] = ["Name", "Email", "Age"]
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        writer.writerows(user_data)


def read_csv(file_path: str) -> type_user_data:
    """
    Reads the CSV file

    It takes one argument
    file_path: type string, refers to the csv file path
    returns a list of tuples
    """

    user_data: type_user_data = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            user_data.append((row[0], row[1], int(row[2])))

    return user_data


FILE_PATH: str = "./new_users.csv"

USER_DATA: type_user_data = [
    ("Sarmad", "sarmad@email.com", 19),
    ("Nawaz", "nawaz@email.com", 23),
    ("Mubashir", "mubashir@email.com", 17),
]


write_csv(FILE_PATH, USER_DATA)

data = read_csv(FILE_PATH)

for name, email, age in data:
    print(f"{name} with email ({email}) is {age} years old.")
