"""
Context managers.

Problem :

You want to create a temporary file, write some data into it, use it, and then delete 
it automatically after the operation is done. This is useful when you don't want to 
leave temporary files behind after your program finishes.
"""

import os
from contextlib import contextmanager


@contextmanager
def temporary_file(file_name):
    """
    Temporary file context manager.
    """
    try:
        # Step 1: Create the file
        print(f"Creating temporary file: {file_name}")
        with open(file_name, "w", encoding="utf-8") as file:
            yield file  # Step 2: Yield the file object to the 'with' block
        # File is automatically closed after exiting 'with' block
    finally:
        # Step 3: Delete the file after the block, even if an error occurs
        if os.path.exists(file_name):
            print(f"Deleting temporary file: {file_name}")
            # os.remove(file_name)


# Using the context manager to create, write to, and automatically delete a temporary file
TEMP_FILE_NAME = "temp_data.txt"

with temporary_file(TEMP_FILE_NAME) as temp_file:
    # Write some data to the temporary file
    print(f"Writing data to {TEMP_FILE_NAME}")
    temp_file.write("This is some temporary data.\n")
    temp_file.write("This file will be deleted after use.\n")


def delete_temp_file():
    """
    Function to delete the temporary file.
    """
    if os.path.exists(TEMP_FILE_NAME):
        print(f"Deleting temporary file: {TEMP_FILE_NAME}")
        os.remove(TEMP_FILE_NAME)


# Uncomment the following line to delete the temporary file
# delete_temp_file()

# Outside the 'with' block, the temporary file should be deleted
print("Temporary file operation complete.")
