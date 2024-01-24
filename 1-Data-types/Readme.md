# Python 3.12 Typings

## Variable Typings

<table>
    <thead>
        <th>Type</th>
        <th>Syntax</th>
    </thead>
    <tbody>
        <tr>
            <td>
            String
            </td>
            <td>
                str
            </td>
        </tr>
        <tr>
            <td>
            Number
            </td>
            <td>
            int
            </td>
        </tr>
        <tr>
            <td>
            Float
            </td>
            <td>
            float
            </td>
        </tr>
        <tr>
            <td>
            Boolean
            </td>
            <td>
            bool
            </td>
        </tr>
    </tbody>
</table>

```py
name : str = "Sarmad"
print(type (name)) # class
print(id(name)) # address
print(dir(name)) # Gives the available operations
```

## Another Example

```py
name: str = "Sarmad"
age: int = 19
married: bool = False
print(name)
```

## List Typing

``` py
vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
odds: list[int] = [1, 3, 5, 7, 9]

print(vowels)

```

## Tuple Typing

```py
props: tuple[(str, str, int, bool)] = ("Sarmad", "sarmad@gmail.com", 19, True)

print(props)
```

## Set Typing

```py
details: set[str] = {"Sarmad", "sarmad@gmail.com"}

print(details)

```
