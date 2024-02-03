import re

name = str(input("Enter Your name? ")).strip()

matches = re.search(r"^(.+), *(.+)$",name)

if matches:
    name = matches.group(2) + " " + matches.group(1)

print(f"Hi, {name}")