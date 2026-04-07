# Methods (Functions)

This lecture introduces the concept of **methods (functions)**, which are essential for writing structured, reusable, and maintainable code.

Functions allow breaking down complex problems into smaller, manageable pieces, improving both readability and efficiency.

---

## 📚 What is a Function?

A function is a reusable block of code that performs a specific task.

```python
def greet():
    print("Hello!")
```

👉 The function is defined once and can be called multiple times.

---

## 🔁 Calling a Function

```python
greet()
```

👉 Executes the code inside the function.

---

## 🧠 Why Use Functions?

Functions help to:

* avoid code duplication
* improve readability
* organize code into logical units
* simplify debugging and maintenance

---

## 🔢 Functions with Parameters

Functions can accept input values (parameters):

```python
def greet(name):
    print(f"Hello, {name}")
```

```python
greet("John")
```

---

## 🔄 Returning Values

Functions can return results using `return`:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

---

## 🔁 Multiple Parameters

```python
def multiply(a, b):
    return a * b
```

---

## 🔄 Functions Without Return

```python
def print_message():
    print("This is a message")
```

👉 These functions perform actions but do not return values.

---

## 🔄 Local vs Global Scope

### Local variables:

```python
def example():
    x = 10
```

👉 Accessible only inside the function

---

### Global variables:

```python
x = 5

def print_x():
    print(x)
```

👉 Accessible throughout the program

---

## 🔁 Reusability

Functions can be reused multiple times:

```python
def square(n):
    return n * n

print(square(2))
print(square(4))
```

---

## 🧩 Common Use Cases

---

### 1. Performing Calculations

```python
def calculate_area(a, b):
    return a * b
```

---

### 2. Validating Input

```python
def is_even(number):
    return number % 2 == 0
```

---

### 3. Formatting Output

```python
def format_name(name):
    return name.capitalize()
```

---

### 4. Breaking Down Logic

Instead of writing everything in one place:

```python
def process_data():
    read_input()
    calculate()
    print_result()
```

---

## 🪜 Problem-Solving Approach

### 1. Identify repeated logic

👉 extract into a function

---

### 2. Define clear purpose

👉 each function should do one thing

---

### 3. Choose parameters

👉 what input is needed

---

### 4. Decide return value

👉 what output is expected

---

### 5. Use functions in main logic

---

## 📏 Good Practices

* use meaningful function names
* keep functions short and focused
* avoid duplicating code
* use return values when needed

---

## 🚫 Common Mistakes

### 1. Forgetting to return a value

```python
def add(a, b):
    a + b  # missing return
```

---

### 2. Incorrect parameter usage

---

### 3. Overcomplicated functions

---

### 4. Using global variables unnecessarily

---

### 5. Not reusing functions

---

## 🔄 Connection to Previous Lectures

Previously:

* writing code in a single block

Now:

* organizing code into reusable units

👉 This is a major step toward professional programming.

---

## 🧠 Skills Developed

* writing modular code
* improving readability
* structuring solutions
* reducing duplication
* building reusable logic

---

## 🎯 Conclusion

Functions are one of the most important concepts in programming.
They enable writing clean, structured, and reusable code, making programs easier to understand and maintain.

Mastering functions is essential for advancing to more complex topics such as data structures, object-oriented programming, and larger-scale applications.

---
