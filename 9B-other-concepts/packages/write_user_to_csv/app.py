"""
Python package for writing user info in a csv file
"""
import csv, re

def write_user_info(filename, user_info):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Email"])
        writer.writerow(user_info)

def is_valid_name(name):
    # Allow spaces in the name but ensure it contains only alphabetic characters
    return all(part.isalpha() for part in name.split())

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

def get_user_input():
    while True:
        name = input("Enter your name: ").strip()
        if not is_valid_name(name):
            print("Invalid name. Please enter a valid name containing only English characters.")
            continue
        
        email = input("Enter your email: ").strip()
        if not is_valid_email(email):
            print("Invalid email. Please enter a valid email address.")
            continue
        
        return name, email
