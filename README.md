# Python Roadmap

Python is a versatile, high-level programming language known for its simplicity and readability, making it ideal for both beginners and experienced developers. Its vast ecosystem of libraries and frameworks supports a wide range of applications, from web development and automation to data science, artificial intelligence, and machine learning.

**Why Python:**

Python's demand has surged due to its pivotal role in emerging technologies like AI, big data, and cloud computing. Companies favor Python for its efficiency in rapid prototyping and scalability, making it a go-to language for startups and large enterprises alike. Learning Python opens doors to a broad spectrum of tech fields, ensuring relevance in the ever-evolving job market.

**Repository Content:**

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
11. [NumPy](/8-Numpy/)
12. [Pandas](/9-Pandas/)

## Object-Oriented Programming (OOP) with Python

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

## Install MyPy Extension

First install the MyPy extension in your editor. (vscode)
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

### Create and Activate Virtual Environment using `pip`

```bash
python -m venv venv
```

**Activate it:**

```bash
.\venv\Scripts\activate
```

Once activated, your command prompt will change to show the name of the virtual environment in parentheses, indicating that it's active. For example:

```bash
(venv) C:\path\to\your\project>
```

Verify activation

```bash
where python
```

Now you can install any package inside the virtual environment.

```bash
pip install requests
```

**Deactivating Virtual environment:**

```bash
deactivate
```

### Learn more

Learn **DSA** with python. <https://github.com/Sarmad426/DSA-Python>

Back end **API** development using **Fast API**. <https://github.com/Sarmad426/FastAPI>

Learn **AI** and **Data Science**. <https://github.com/Sarmad426/AI>

Learn **Generative AI**. <https://github.com/Sarmad426/Generative-AI>
