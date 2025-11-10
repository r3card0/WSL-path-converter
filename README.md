# WSL Path Converter

A Python utility for converting Windows paths to WSL (Windows Subsystem for Linux) paths and viceversa.

## Overview
This project provides a simple and efficient way to convert between Windows-style paths (e.g., `C:\\Users\username\file.txt`) and WSL-style paths (e.g., `/mnt/c/Users/username/file.txt`). This is a particularly useful when working with files across both Windows and WSL environments.

## Features
* Convert Windows paths to  WSL paths.
* Lightweight and easy to integrate

## Installation

```
git install git+https://github.com/r3card0/WSL-path-converter.git@v0.1.0
```

## Usage

**Basic Example**

```python
from wsl_path_converter import PathConverter
```
**Convert from Windows to WSL**

```python
wsl_path = PathConverter("C:\\Users\\archivo.txt").to_wsl()
```

Output

```bash
/mnt/c/Users/archivo.txt
```

## Available Methdos
### `PathConverter(path).to_wsl()`

Convert a Window path to Windows Subsystem Linux path

**Parameters**
- `filepath` (str): Windows path format (e.g., `C:\\Users\\archivo.txt`)

**Returns**
- `str` :  Windows Subsystem Linux path (e.g., `/mnt/c/Users/archivo.txt`)

## Versions
- **v0.1.0** - Initial version

## Requirements
* Python 3.10 or higher
* Windows 10/11 with WSL installed

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License

## Acknowledgments

* Inspired by the need for seamless file path conversion when working with WSL
* Built for developers who frequently switch between Windows and Linux environments.

## Author
@[r3card0](https://github.com/r3card0)

Project Links: https://github.com/r3card0/WSL-path-converter

