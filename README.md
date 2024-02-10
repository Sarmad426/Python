# Python Roadmap

1. [Data Types](/1-Data-types/)
2. [Conditions](/2-Conditions)
3. [Loops](/2A-Loops/)
4. [Functions](/3-Functions/)
5. [Exceptions](/4-Exceptions/)
6. [Libraries](/5-Libraries/)
7. [Unit Tests](/5A-unit-tests/)
8. [File Handling](/6-File-IO/)
9. [Regular Expression (REGEX)](/6A-Regex/)
10. [OOP](/7-OOP/)
11. [Numpy](/8-Numpy/)
12. [Pandas](/9-Pandas/)

## Object-Oriented Programming (OOP) with Python Course Roadmap

## Pillars of OOP

- [Inheritance](/7-OOP/inheritance/)
- [Abstraction](/7-OOP/Abstraction/)
- [Polymorphism](/7-OOP/Polymorphism)
- [Encapsulation](/7-OOP/Encapsulation)

### Inheritance

- Multiple inheritance
- Multi-level inheritance

## Other Topics of OOP

- Classes and objects
- Constructor
- decorators
- Getters and setters
- Methods (class functions)
- Duck Typing
- Operator overloading

## Projects

- **[Library Management System](/Final-project/)** (OOP) program
- Python **[GUI Calculator](/GUI-calculator/)**

## Python 3.12 Project Setup

Python 3.12 type hinting. Basics and Advanced Object Oriented Programming.

## Install Mypy Extension

First install the Mypy extension in your editor. (vscode)
Also install `pip` package.

``` pip
pip install mypy
```

This extension and package will check the typing errors in python file much like Typescript.

## Update Conda to Python 3.12 by creating Virtual Environment

```bash
conda create -n py_12 python==3.12 -y
```

This will create a virtual Environment.
`-n` means name of the virtual env.
`-y` is yes for all installation questions.

## Activate Virtual Env

```bash
conda env list
```

Check the Available virtual env list.

```bash
conda activate py_12
```

Check Python Version

```bash
python --version
```

### Python installation for vscode

```pip
Pylance
Pylint
MyPy Type checker
MyPy
Jupyter
Jupyter Slideshow
Jupyter Keymap
Jupyter Notebook Renderers
Jupyter Cell Tags
Black Formatter
```
