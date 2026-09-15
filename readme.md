<div align="center">"cleanpy"

Strip the noise. Keep the code.

A lightweight Python utility for removing comments and docstrings from ".py" files — without touching the original source.

<br><img src="https://img.shields.io/badge/Python-3.x-18181B?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Dependencies-None-18181B?style=flat-square" alt="Dependencies">
<img src="https://img.shields.io/badge/License-MIT-18181B?style=flat-square" alt="License"><br><br>

              source.py
                  │
                  ▼
        ┌───────────────────┐
        │      cleanpy      │
        │                   │
        │  comments    ×    │
        │  docstrings  ×    │
        │  code        ✓    │
        └─────────┬─────────┘
                  │
                  ▼
           source_clean.py

<br>"Usage" (#usage) · "How it works" (#how-it-works) · "Examples" (#examples) · "License" (#license)

</div>"01" — The idea

Python source files naturally collect comments, documentation strings, and other pieces of descriptive text during development.

Sometimes you simply want the source without that extra layer.

That's where "cleanpy" comes in.

BEFORE                         AFTER

# explanation                 def calculate(a, b):
                              │
def calculate(a, b):          │   return a + b
    """..."""                 │
    return a + b  # ...       │

The original file is never overwritten.

If the input is:

example.py

the output becomes:

example_clean.py

"02" — What gets removed

Element| Result
Module docstrings| Removed
Function docstrings| Removed
Async function docstrings| Removed
Class docstrings| Removed
Standalone comments| Removed
Inline comments| Removed
Executable code| Preserved
Original file| Preserved

CleanPy uses Python's "ast" module to identify docstrings and "tokenize" to identify comments.

"03" — Usage

There is nothing to install.

No package manager.

No external dependencies.

Just Python.

Run

python cleaner.py example.py

Result

example.py
example_clean.py

CleanPy automatically creates the cleaned file beside the original.

CLI

python cleaner.py <python_file>

The utility expects exactly one Python file as its argument.

"04" — Example

Before

# Calculate the total

def calculate(a, b):
    """Return the sum of two values."""
    return a + b  # add the values

After

def calculate(a, b):
    return a + b

The transformation focuses on removing the descriptive layer while retaining the executable source.

"05" — How it works

CleanPy doesn't blindly search for strings such as "#" or """"".

It parses the source first.

                   Python file
                       │
                       ▼
                 Python AST
                       │
                       ├──── module docstring
                       ├──── class docstring
                       ├──── function docstring
                       └──── async function docstring
                       │
                       ▼
                  Tokenization
                       │
                       ├──── standalone comments
                       └──── inline comments
                       │
                       ▼
                 Cleaned source
                       │
                       ▼
                *_clean.py

Docstrings are discovered through the Python AST, while comment tokens are identified through Python's tokenizer.

This allows the cleaner to work with Python syntax rather than relying on simple text replacement.

"06" — Output behavior

CleanPy follows a deliberately safe output model.

                  ┌─────────────────┐
                  │    example.py   │
                  └────────┬────────┘
                           │
                           ▼
                       cleanpy
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       original stays             new file created
          untouched               example_clean.py

The output filename is generated from the original filename by adding "_clean" before ".py".

"07" — Built around Python

CleanPy intentionally keeps its implementation small.

Its core relies on Python's standard library:

import ast
import io
import sys
import tokenize
from pathlib import Path

No third-party runtime packages are required.

That means the project can stay lightweight and portable.

"08" — Project structure

cleanpy/
│
├── cleaner.py
├── README.md
└── LICENSE

The main executable logic lives in "cleaner.py".

"09" — Error handling

CleanPy handles common input and processing failures instead of silently continuing.

invalid path       → File not found
non-Python file    → Invalid input type
invalid Python     → Syntax error
encoding problem   → Unicode error
filesystem issue   → OS error

The CLI catches these errors and reports them to the user.

"10" — Design principles

Small

One focused utility.

Local

Your source stays on your machine.

Non-destructive

The input file is not replaced.

Dependency-free

Built with Python's standard library.

Predictable

Input:

file.py

Output:

file_clean.py

"11" — Requirements

Python 3.x

Nothing else.

"12" — Why clean source?

Comments and docstrings are valuable during development.

But there are situations where a cleaner representation of the source is useful — inspection, transformation pipelines, experimentation, or simply reducing visual noise.

CleanPy doesn't try to decide what your code should look like.

It simply gives you another copy.

your source
     │
     ├── original
     │
     └── cleaned

Both can coexist.

"13" — Safety first

CleanPy writes to a new file instead of replacing the source file.

That means you can compare:

original.py
original_clean.py

before deciding what to keep.

No destructive overwrite is part of the normal workflow.

"14" — License

Released under the MIT License.

See ""LICENSE"" (LICENSE) for the complete license text.

<br><div align="center">cleanpy

less noise
same code

<br>Built small. Built deliberately.

</div>
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
