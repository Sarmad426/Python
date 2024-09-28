"""
Function to split the string
"""

STRING = "Sarmad is my  best  Friend "


def append_to_list(words: list[str], word: str) -> tuple[list[str], str]:
    """
    Appends the splitted word to the list
    """
    words.append(word)
    word = ""
    return words, word


def split(string: str) -> list[str]:
    """
    Split function, returns the splitted version of the string
    """
    splitted_list: list[str] = []
    word, i = "", 0
    for char in string:
        i += 1
        if char != " ":
            word += char
            if i == len(string):
                splitted_list, word = append_to_list(splitted_list, word)
        else:
            if word != "":
                splitted_list, word = append_to_list(splitted_list, word)
    return splitted_list


# comparison
print(split(STRING))
print(STRING.split())
