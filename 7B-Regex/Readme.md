# REGEX

Regex, short for Regular Expression, is a powerful tool used for pattern matching and manipulation of strings. It provides a concise and flexible syntax for describing text patterns, allowing you to search, match, and manipulate text based on specific criteria.

## Basic Concepts

### 1. Literal Characters

Match the exact characters specified in the pattern.
   - Example: The regex `apple` would match the string "apple" in a text.

### 2. Meta-characters 

These are special characters with a specific meaning.

   - `.`:   any character except a newline.
   - `*`:   Matches 0 or more occurrences of the preceding character or group.
   - `+`:   Matches 1 or more occurrences of the preceding character or group.
   - `?`:   Matches 0 or 1 occurrence of the preceding character or group.
   - `^`:   matches the beginning of the string.
   - `$`:   matches the end of the string or just before the newline at the end of the string.
   - `\`:   Escapes a meta-character, treating it as a literal character.
   - `{m}`:    m repetitions
   - `{m,n}`:  m-n repetitions
   - `A|B`:    either A or B
   - `(...)`:  a group
   - `(?:...)`:   non-capturing version
   - `[]`:       set of Characters
   - `[^]`: Complementing of Set
   - `\d`: Decimal digit
   - `\D`: not a decimal digit
   - `\s`: whitespace character
   - `\S`: not a whitespace character
   - `\w`: word character as well as numbers and the underscore
   - `\W`: not a word character


## Python Code Example for REGEX

```python
import re

# Example 1: Matching a specific word
pattern = re.compile(r'apple')
result = pattern.match('apple pie')
print(result.group())  # Output: apple

# Example 2: Matching any digit
pattern = re.compile(r'\d+')
result = pattern.findall('There are 25 apples and 30 bananas.')
print(result)  # Output: ['25', '30']

# Example 3: Matching an email address
pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
text = 'Contact support@example.com for assistance.'
result = pattern.search(text)
print(result.group())  # Output: support@example.com
```

In these examples:

- `re.compile()` is used to create a regex pattern.
- `match()` is used to find a match at the beginning of a string.
- `findall()` is used to find all occurrences of the pattern in a string.
- `search()` is used to search for the pattern anywhere in the string.
