CleanPy

<p align="center">
  <strong>Clean Python. Less noise.</strong>
  <br>
  A lightweight utility for stripping comments and docstrings from Python source files.
</p><p align="center">
  <img src="https://img.shields.io/badge/python-3.x-111111?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square">
  <img src="https://img.shields.io/badge/status-active-111111?style=flat-square">
</p>---

Overview

CleanPy removes unnecessary comments and docstrings from Python source code while keeping the executable code intact.

Instead of modifying your original file, CleanPy creates a separate cleaned copy:

script.py
    ↓
script_clean.py

Simple. Local. No dependencies.

---

✦ Features

- Removes Python docstrings
- Removes standalone comments
- Removes inline comments
- Preserves executable code
- Creates a separate output file
- Uses Python's built-in "ast" and "tokenize" modules
- No external dependencies
- Works entirely locally

---

Installation

Clone the repository:

git clone https://github.com/your-username/cleanpy.git
cd cleanpy

No package installation is required.

---

Usage

Run CleanPy against any Python file:

python cleaner.py script.py

The cleaned version will be generated beside the original:

script.py
script_clean.py

Example:

project/
├── cleaner.py
├── example.py
└── example_clean.py

---

Before

# Calculate the total

def calculate(a, b):
    """Return the sum of two values."""
    return a + b  # add the values

After

def calculate(a, b):
    return a + b

Your original source remains untouched.

---

How it works

CleanPy combines Python's built-in parsing tools to identify removable content.

AST parsing is used to locate docstrings inside modules, functions, asynchronous functions, and classes.

Tokenization is then used to identify comments without treating comment-like text inside strings as actual comments.

The cleaned source is finally written to a new file rather than overwriting the original.

---

Requirements

Python 3.x

That's it.

---

Project Structure

cleanpy/
│
├── cleaner.py
├── README.md
└── LICENSE

---

Philosophy

«Keep the code. Remove the noise.»

CleanPy is intentionally small.

No frameworks.
No dependencies.
No unnecessary configuration.

Just a focused utility that does one thing and does it locally.

---

License

Released under the MIT License.

See ""LICENSE"" (LICENSE) for details.

---

<p align="center">
  <sub>Built for clean source. ✦</sub>
</p>
