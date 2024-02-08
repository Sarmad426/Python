characters: dict[str, str] = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

output = ""

user_input = input("Phone Number: ")

for ch in user_input:
    output += characters.get(ch, "") + " "
print(output)
