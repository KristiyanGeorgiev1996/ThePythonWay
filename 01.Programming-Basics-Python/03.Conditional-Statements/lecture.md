# Conditional Statements

This lecture introduces one of the most important concepts in programming — **decision-making**.
Up to this point, programs execute instructions sequentially from top to bottom. With conditional statements, programs can now determine **which action to take** based on specific conditions.

---

## 📚 What Are Conditional Statements?

Conditional statements allow a program to follow different execution paths depending on whether a condition is true or false.

The most commonly used constructs are:

* `if`
* `if-else`
* `if-elif-else`

These form the foundation of all logic related to validation, comparison, and decision-making.

---

## 🧠 Why Are They Important?

In real-world programming, it is often necessary to check:

* whether one number is greater than another
* whether a value falls within a specific range
* whether a password is correct
* whether a number is even or odd
* which formula to use based on a selected type
* which category a value belongs to

Without conditional statements, programs would not be able to react differently to different inputs.

---

## 🔹 `if` Statement

The simplest form of a conditional statement is `if`.

```python
number = int(input())

if number > 0:
    print("Positive number")
```

### How it works:

* the program reads a value
* checks whether the condition `number > 0` is true
* if true, the block under `if` is executed

If the condition is false, the block is skipped.

---

## 🔹 `if-else` Statement

When an action is required for both possible outcomes (true and false), `if-else` is used.

```python
number = int(input())

if number % 2 == 0:
    print("even")
else:
    print("odd")
```

### Behavior:

* if the number is divisible by 2 → `even`
* otherwise → `odd`

This structure is ideal when there are **exactly two possible outcomes**.

---

## 🔹 `if-elif-else` Statement

When more than two conditions need to be checked, `if-elif-else` is used.

```python
number = int(input())

if number < 100:
    print("Less than 100")
elif number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
```

### Logic:

* first condition is checked
* if false → next condition is checked
* continues until a true condition is found
* if none match → `else` executes

This is commonly used for:

* classification
* range-based evaluation
* multi-case decision logic

---

## 🔍 Boolean Expressions

Conditional statements rely on **boolean expressions**, which evaluate to:

* `True`
* `False`

Examples:

```python
5 > 3       # True
10 == 7     # False
8 != 2      # True
```

---

## ⚖️ Comparison Operators

Common operators used in conditions:

* `==` equal to
* `!=` not equal to
* `>` greater than
* `<` less than
* `>=` greater than or equal
* `<=` less than or equal

### Example:

```python
a = 10
b = 20

print(a < b)    # True
print(a == b)   # False
print(a != b)   # True
```

---

## 🔗 Logical Operators

Multiple conditions can be combined using:

* `and`
* `or`
* `not`

### `and`

Both conditions must be true:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted")
```

---

### `or`

At least one condition must be true:

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

### `not`

Reverses the condition:

```python
is_raining = False

if not is_raining:
    print("Go outside")
```

---

## 🧱 Indentation in Python

Python uses **indentation** to define code blocks instead of braces.

```python
number = 10

if number > 5:
    print("Greater than 5")
    print("Still inside the block")

print("Outside the block")
```

Everything indented under the `if` belongs to that block.

### Important:

* incorrect indentation → logical errors
* missing indentation → syntax errors

---

## 🧩 Common Problem Types

Conditional statements are typically applied in several key patterns.

---

### 1. Single Condition Check

Examples:

* checking a grade
* validating a password
* checking if a number is even

```python
grade = float(input())

if grade >= 5.50:
    print("Excellent!")
```

---

### 2. Two-Value Comparison

Examples:

* finding the greater number
* validating correct/incorrect input

```python
first = int(input())
second = int(input())

if first > second:
    print(first)
else:
    print(second)
```

---

### 3. Range Classification

```python
value = int(input())

if value < 100:
    print("Less than 100")
elif value <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
```

---

### 4. Multi-Range Categorization

```python
speed = float(input())

if speed <= 10:
    print("slow")
elif speed <= 50:
    print("average")
elif speed <= 150:
    print("fast")
elif speed <= 1000:
    print("ultra fast")
else:
    print("extremely fast")
```

---

### 5. Choosing Logic Based on Type

```python
figure_type = input()

if figure_type == "square":
    side = float(input())
    area = side * side
elif figure_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure_type == "circle":
    radius = float(input())
    area = 3.14159 * radius * radius
elif figure_type == "triangle":
    base = float(input())
    height = float(input())
    area = base * height / 2

print(f"{area:.3f}")
```

---

## 🪜 Problem-Solving Strategy

A structured approach helps significantly:

1. Understand what needs to be checked
2. Identify input types
3. Choose the correct conditional structure
4. Order conditions correctly
5. Test with multiple cases

---

## 📏 Edge Cases

Boundary values are critical:

* values exactly at limits (e.g. 100, 200)
* minimum/maximum values

Example:

```python
if number < 100:
```

vs

```python
if number <= 100:
```

A single symbol can change the entire logic.

---

## 🧮 Comparing Numbers vs Strings

### Numbers:

```python
if number > 5:
```

### Strings:

```python
password = input()

if password == "s3cr3t":
    print("Welcome")
```

Important:

* comparisons are exact
* case-sensitive
* spaces matter

---

## 🛠 Practical Template

```python
value = input()

if condition:
    action
elif another_condition:
    another_action
else:
    fallback_action
```

---

## 🚫 Common Mistakes

### 1. Using `=` instead of `==`

```python
if number = 5:   # wrong
```

---

### 2. Wrong condition order

---

### 3. Missing edge cases

---

### 4. Type mismatch

---

### 5. Incorrect indentation

---

## 🧠 Skills Developed

* Logical thinking
* Decision-making in code
* Working with boolean logic
* Value classification
* Choosing correct execution paths
* Attention to detail

---

## 🔄 Connection to Previous Lecture

Previously:

* input/output
* variables
* calculations

Now:

* decision-making based on values

---

## 🎯 Conclusion

Conditional statements are essential for building dynamic and intelligent programs.
They enable programs to evaluate data, make decisions, and execute the correct logic.

Mastering `if`, `if-else`, and `if-elif-else` is a critical step toward writing more complex and functional software.

---
