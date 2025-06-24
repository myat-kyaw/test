# test

This repository provides an advanced calculator implemented in Python.

## Usage

Run the script with a mathematical expression:

```bash
python advanced_calculator.py "2 + 3 * 4"
```

You may also use functions from the `math` module:

```bash
python advanced_calculator.py "sin(pi / 2) + log(10)"
```

The calculator safely evaluates the expression using Python's AST module, supporting common arithmetic operators and all standard math functions.

## Web Interface

Install dependencies and run the web application:

```bash
pip install -r requirements.txt
python web_app.py
```

Open `http://localhost:5000` in your browser to use the calculator with a modern web UI.
