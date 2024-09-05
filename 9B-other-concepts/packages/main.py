"""
Using python packages
"""
from write_user_to_csv import write_user_info, get_user_input


def main():
    name, email = get_user_input()
    user_info = [name, 20, email]  # Assuming age is fixed for this example
    write_user_info("user_info.csv", user_info)

if __name__ == "__main__":
    main()