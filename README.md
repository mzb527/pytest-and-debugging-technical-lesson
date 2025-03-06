# Intro to Pytest and Debugging

## Introduction

This lesson covers fundamental testing concepts in Python, including:

- **Understanding the Terminal and Tracebacks** – How to navigate the terminal and interpret Python error messages.
- **Intro to Pytest** – Why Pytest is a popular framework for testing Python applications.
- **Unit Testing with Pytest** – Writing and organizing tests for a simple Calculator app.
- **Debugging with Python Tools** – Using built-in Python tools to diagnose and fix issues.

By the end of this lesson, you will know how to set up Pytest, write basic unit tests, interpret errors, and debug your code efficiently.

---

## Scenario: A Simple Calculator App

Imagine you have created a basic command-line Calculator application with functions for:

- Addition
- Subtraction
- Multiplication
- Division

Your goal is to ensure that each operation behaves correctly under various inputs. You also want to quickly diagnose any unexpected behavior using Python’s traceback messages and debugging tools.

## Tools and Resources

- **GitHub Repo**: [pytest-and-debugging-technical-lesson](https://github.com/learn-co-curriculum/pytest-and-debugging-technical-lesson)

---

## Instructions

### Set Up

Before we begin coding, let's complete the initial setup for this lesson:

#### **Fork and Clone**

1. Go to the provided GitHub repository link.
2. Fork the repository to your GitHub account.
3. Clone the forked repository to your local machine.

#### **Open and Run File**

1. Open the project in **VSCode**.
2. Run `pipenv install` to install all necessary dependencies.
3. Run `pipenv shell` to enter the virtual environment.

---

## Instructions

### Task 1: Define the Problem

Our Calculator works, but it is untested. Common issues we want to catch:

- **Incorrect Arithmetic** – Does each function return the expected result (e.g., `divide(4, 2) == 2`)?
- **Error Handling** – How does the app behave when dividing by zero or receiving unexpected input?
- **Maintenance** – Code changes might break existing features without warning, so we need automated tests.

### Task 2: Determine the Design

**What We Need to Implement:**

- **Pytest Setup** – To easily run tests.
- **Unit Tests** – Confirm each Calculator function behaves correctly with different input scenarios.
- **Traceback Familiarity** – Learn to interpret error messages when tests fail.
- **Debugging Tools** – Use Python’s built-in debugging to step through code and fix errors.

### Task 3: Develop the Code

#### Step 1: Create a New Git Feature Branch

```sh
git checkout -b feature-testing
```

#### Step 2: Examine the Existing Calculator Code

```python
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Intentionally ignoring divide-by-zero check for now
    return a / b

if __name__ == "__main__":
    print("Simple Calculator App")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"8 / 2 = {divide(8, 2)}")
```

> **Note:** The code might not handle edge cases like dividing by zero. Let’s see if our tests catch this issue!

#### Step 3: Understanding the Terminal & Tracebacks

Run the code in your terminal:

```sh
python3 calculator.py
```

Modify the `divide` function to introduce an error:

```python
def divide(a, b):
    return a // b + "error"  # This will cause a TypeError
```

Re-run the script and analyze the traceback to locate the error.

#### Step 4: Install and Set Up Pytest

```sh
pip install pytest
```

#### Step 5: Create a Test File

```sh
touch test_calculator.py
```

```python
# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide
```

#### Step 6: Write Unit Tests

**Test `add` function:**

```python
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
```

**Run the tests:**

```sh
pytest
```

**Test `subtract` function:**

```python
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5
```

**Test `multiply` function:**

```python
def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-1, 5) == -5
```

**Test `divide` function:**

```python
def test_divide():
    assert divide(8, 2) == 4
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

#### Step 7: Verify and Debug

Run the tests again:

```sh
pytest
```

If a test fails, Pytest prints a traceback with the exact line that failed.

#### Step 8: Debugging Tools

**Using `print()` debugging:**

```python
print("Debugging: ", variable_name)
```

**Using `pdb` for step-by-step debugging:**

```sh
python -m pdb calculator.py
```

**Using Pytest with debugging mode:**

```sh
pytest --pdb
```

#### Step 9: Improve Error Handling

Modify `divide` to handle zero division:

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```

Re-run `pytest` and confirm no tests fail.

---

### Task 4: Document and Maintain

#### **Commit and Push Changes**

```sh
git add .
git commit -m "Add unit tests with Pytest for Calculator app"
git push origin feature-testing
```

Create a Pull Request and merge your tested code into `main`.

---

## Considerations

### Performance
- Simple arithmetic is fast, but more complex logic might need performance benchmarks.

### Error Handling
- Defensive programming: Handle unexpected inputs gracefully.

### Code Coverage
- Use `coverage.py` to measure untested parts of your code.

### Scalability
- As your app grows, adopt structured approaches like CI/CD pipelines.

---

## Final Thoughts

- **Terminal & Tracebacks:** Quickly locate and fix issues.
- **Pytest:** A powerful framework for writing clean, maintainable tests.
- **Unit Testing:** Ensures each function works in isolation.
- **Debugging:** Use Python’s built-in tools to step through problem areas.

### Next Steps:

- Integrate `coverage.py` to measure code coverage.
- Explore advanced debugging tools.
- Implement more complex features (e.g., exponentiation, square root) and write additional tests.
