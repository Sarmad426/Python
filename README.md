# Python 3.12

Python 3.12 new Release features. New Typing and Jupyter.

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
Black
```
