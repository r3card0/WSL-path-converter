# 🔄️ WSL Path Converter

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A Python utility for converting Windows paths to WSL (Windows Subsystem for Linux) paths and viceversa.

## 🧭 Overview
This project provides a simple and efficient way to convert between Windows-style paths (e.g., `C:\\Users\username\file.txt`) and WSL-style paths (e.g., `/mnt/c/Users/username/file.txt`). This is a particularly useful when working with files across both Windows and WSL environments.

## 🛠️ Features
* Convert Windows paths to WSL paths.
* Lightweight and easy to integrate

## ⚙️ Installation
### 1. Check the Requisites
* Python 3.10.12 or higher
* Install pip
* Windows 10/11 with WSL installed


### 2. Create a Python Virtual Environment

> ⚠️ Make sure you are using a WSL (Window Subsystem for Linux) terminal to run the package installation commands.

In a WSL terminal, run the following process

1. Create a virtual environment. Select the virtual environment's name; e.g. *venv_process* 

    ```bash
    python3 -m venv venv_process
    ```

2. Activate the virtual environment:

    ```bash
    source venv_process/bin/activate
    ```

### 3. 📦 Install WSL Path Converter Dependency

Once the virtual environment is installed and activated, install WSL Path Converter dependency by executing the following command:

```
pip install git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0
```
## ⚡ Class Methods

|Class Method|Objective|Parameter(s)|Result(s)|
|-|-|-|-|
|`to_wsl()`|Convert a Window path to Windows Subsystem Linux path| `filepath` (str): Windows path format (e.g., `C:\\Users\\archivo.txt`)| Return a string. `str` :  Windows Subsystem Linux path (e.g., `/mnt/c/Users/archivo.txt`)|

## Versions

|Version|Description|
|-|-|
|**v0.1.0**|Initial version|

## 🚗 Usage

**Basic Example**

```python
from wsl_path_converter import PathConverter

# Convert from Windows to WSL**
def run():
    wsl_path = PathConverter("C:\\Users\\archivo.txt").to_wsl()

    print(wsl_path)

if __name__ == "__main__":
    run()
```

Output

```bash
/mnt/c/Users/archivo.txt
```


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📃License

This project is licensed under the MIT License

## 🚀 Project Motivation

* Inspired by the need for seamless file path conversion when working with WSL
* Built for developers who frequently switch between Windows and Linux environments

## 🔗 References
**pathlib**

* [Python.org - pathlib](https://docs.python.org/3/library/pathlib.html)

**pyproject.toml file**

* [SetUpTools - Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)
* [SetUpTools - Package Discovery](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html)
* [Python Packaging User Guide - Writting your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
* [Python Packaging User Guide - src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
* [Rogger van der Geer - An Updated Guide to Setuptools and Pyproject.toml](https://xebia.com/blog/an-updated-guide-to-setuptools-and-pyproject-toml/)

# 👤 Author

* GitHub: [r3card0](https://github.com/r3card0)
* LinkedIn: [Ricardo](https://www.linkedin.com/in/ricardordzsaldivar/)