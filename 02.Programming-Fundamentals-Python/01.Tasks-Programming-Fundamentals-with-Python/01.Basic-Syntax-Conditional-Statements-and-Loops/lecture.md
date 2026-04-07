# Basic Syntax, Conditional Statements and Loops

This lecture marks the beginning of the Programming Fundamentals module and builds upon the knowledge acquired in the previous stage. It combines core concepts such as syntax, conditional statements, and loops into a more practical and structured context.

The main goal is to transition from writing simple programs to developing more structured logic and solving more complex problems.

---

## 📚 What is Basic Syntax?

Basic syntax refers to the rules that define how code is written and interpreted by the programming language.

In this lecture, the focus is on reinforcing:

* correct use of variables
* handling input and output
* formatting results
* writing clean and readable code

---

## 🔁 Combining Concepts

Unlike Programming Basics, tasks in this section:

* combine multiple concepts at once
* require better planning
* involve multiple steps in the solution

Example flow:

* input → condition → loop → calculation → output

---

## ⚖️ Conditional Statements (Advanced Usage)

Conditional logic is used in more complex scenarios:

* multiple conditions
* combining conditions with logical operators
* nested checks
* handling different input cases

### Example:

```python id="d1f7i7"
number = int(input())

if number > 0:
    if number % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Negative or zero")
```

👉 This example demonstrates:

* nested conditions
* classification logic

---

## 🔗 Logical Operators

Conditions can be combined using:

* `and` – all conditions must be true
* `or` – at least one condition must be true
* `not` – reverses the condition

```python id="hj2bmx"
if age >= 18 and has_id:
    print("Access granted")
```

---

## 🔁 Loops (For and While)

Loops are now used not only for repetition, but also for:

* processing input data
* accumulating values
* controlling program logic

---

### `for` Loop

Used when the number of iterations is known:

```python id="nqzg0y"
for i in range(1, 6):
    print(i)
```

---

### `while` Loop

Used when execution depends on a condition:

```python id="9j40ax"
number = int(input())

while number != 0:
    print(number)
    number = int(input())
```

---

## 🔄 Working with Multiple Inputs

This lecture frequently includes:

* reading a sequence of values
* processing them inside a loop
* stopping based on a condition

👉 This is a foundation for real-world applications.

---

## 🧮 Accumulating Values

Many tasks involve:

* summing values
* counting occurrences
* finding maximum or minimum

```python id="m7j67c"
total = 0

for i in range(5):
    number = int(input())
    total += number

print(total)
```

---

## 🧩 Types of Problems

---

### 1. Processing Sequences

* reading multiple inputs
* performing operations on them

---

### 2. Combined Logic

* condition + loop
* nested checks

---

### 3. Input Validation

* checking values
* repeating input until valid

---

### 4. Classification

* grouping values
* working with ranges

---

## 🪜 Problem-Solving Approach

### 1. Analyze the problem

* identify inputs
* determine expected output

---

### 2. Break down the logic

* condition
* loop
* calculations

---

### 3. Choose the right constructs

* `if`, `elif`, `else`
* `for` or `while`

---

### 4. Implement step by step

---

### 5. Test thoroughly

* different inputs
* edge cases

---

## 📏 Edge Cases

Important considerations:

* zero values
* negative numbers
* boundary conditions
* unexpected inputs

---

## 🚫 Common Mistakes

### 1. Mixing logic incorrectly

* poorly structured conditions

---

### 2. Using the wrong loop

* `for` instead of `while` or vice versa

---

### 3. Missing updates

* leads to infinite loops

---

### 4. Incorrect initialization

* wrong starting values

---

### 5. Missing scenarios

* not handling all possible inputs

---

## 🧠 Skills Developed

* combining programming concepts
* logical thinking
* structuring solutions
* handling input data
* writing more complex programs

---

## 🔄 Connection to Programming Basics

In Programming Basics:

* concepts are learned separately

Here:

* they are combined and applied together

👉 This marks a key transition toward real programming.

---

## 🎯 Conclusion

This lecture forms the foundation of the Programming Fundamentals module.
It teaches how different programming constructs work together to solve more complex problems.

Mastering this topic is essential for progressing to more advanced concepts such as lists, functions, and structured data handling.

---
