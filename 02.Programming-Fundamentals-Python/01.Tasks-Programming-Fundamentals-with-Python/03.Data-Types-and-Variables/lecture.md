# Data Types and Variables

This lecture introduces the concept of **data types and variables** in a deeper and more practical context.
It builds upon basic knowledge and focuses on how data is stored, manipulated, and used in more complex programming scenarios.

---

## 📚 What Are Variables?

A variable is a named container used to store a value in memory.

```python
name = "John"
age = 25
```

Variables allow programs to:

* store data
* reuse values
* perform calculations
* manage program state

---

## 🔢 Data Types

Different types of data are represented using different data types.

### Common Data Types in Python:

* `int` → integers (e.g. `10`, `-5`)
* `float` → decimal numbers (e.g. `3.14`, `-0.5`)
* `str` → text (e.g. `"Hello"`)
* `bool` → logical values (`True`, `False`)

---

## 🔄 Type Conversion (Casting)

Data can be converted from one type to another.

```python
number = int("10")
price = float("5.99")
text = str(100)
```

👉 This is essential when working with user input.

---

## 🧠 Working with Input

All input from `input()` is read as a string.

```python
value = input()
```

To use it numerically:

```python
number = int(input())
price = float(input())
```

---

## 🧮 Arithmetic Operations

Variables can be used in calculations:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## 📏 Integer vs Float Division

```python
print(5 / 2)   # 2.5
print(5 // 2)  # 2
```

* `/` → returns a float
* `//` → returns an integer (floor division)

---

## 🔢 Modulo Operator

The modulo operator returns the remainder:

```python
print(5 % 2)  # 1
```

👉 Common use:

* checking even/odd numbers
* cyclic operations

---

## 🔤 Working with Strings

Strings represent text data.

```python
text = "Python"
```

### String Operations:

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

---

## 🔄 String Formatting

Modern formatting:

```python
name = "John"
age = 25

print(f"{name} is {age} years old")
```

---

## 🔍 Character Handling

Access individual characters:

```python
text = "Python"
print(text[0])  # P
```

---

## 📐 ASCII Values

Each character has a numeric representation:

```python
print(ord('A'))  # 65
print(chr(65))   # A
```

---

## 🔢 Working with Numbers

Additional functions:

```python
abs(-5)   # 5
round(3.6)  # 4
```

---

## 🔄 Variable Reassignment

Variables can change value:

```python
x = 10
x = x + 5
```

---

## 🧩 Common Problem Types

---

### 1. Calculations

* performing arithmetic operations
* combining multiple values

---

### 2. Data Conversion

* converting input to correct type

---

### 3. Text Manipulation

* combining strings
* formatting output

---

### 4. Logical Checks

* using values in conditions

---

## 🪜 Problem-Solving Approach

### 1. Identify input types

* number, text, or mixed

---

### 2. Convert if necessary

---

### 3. Apply required operations

---

### 4. Store intermediate results

---

### 5. Output correctly formatted result

---

## 📏 Edge Cases

* division by zero
* invalid input types
* floating-point precision
* large numbers

---

## 🚫 Common Mistakes

### 1. Missing type conversion

```python
number = input()
print(number + 5)  # error
```

---

### 2. Mixing data types

---

### 3. Incorrect operator usage

---

### 4. Wrong formatting

---

### 5. Losing precision with floats

---

## 🧠 Skills Developed

* understanding data representation
* working with different data types
* converting and processing input
* performing calculations
* formatting output
* writing cleaner and more structured code

---

## 🔄 Connection to Previous Lecture

Previously:

* logic and control flow

Now:

* data handling and manipulation

👉 This enables writing more meaningful and functional programs.

---

## 🎯 Conclusion

Data types and variables are fundamental to all programming tasks.
They allow storing, processing, and transforming information effectively.

Mastering this topic is essential for working with more advanced structures such as lists, dictionaries, and functions.

---
