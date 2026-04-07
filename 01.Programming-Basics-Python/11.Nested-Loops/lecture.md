# Nested Loops

This lecture introduces the concept of **nested loops**, where one loop is placed inside another.
Nested loops allow programs to handle more complex repetitive tasks, especially when working with combinations, patterns, and multi-dimensional data.

---

## 📚 What Are Nested Loops?

A nested loop is a loop inside another loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

👉 The inner loop runs completely for each iteration of the outer loop.

---

## 🔁 How Nested Loops Work

Execution flow:

1. The outer loop starts
2. The inner loop runs from start to finish
3. The outer loop moves to the next iteration
4. The inner loop runs again

---

### Example:

```python
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)
```

Output:

```
1 1
1 2
1 3
2 1
2 2
2 3
```

👉 The inner loop repeats fully for each outer loop iteration.

---

## 🧠 When to Use Nested Loops

Nested loops are used when:

* working with **combinations of values**
* generating **patterns**
* processing **tables or grids**
* comparing multiple elements
* solving problems with multiple levels of repetition

---

## 🧩 Common Use Cases

---

### 1. Generating Pairs

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} {j}")
```

👉 Prints all combinations of numbers from 1 to 3

---

### 2. Pattern Printing

```python
for i in range(1, 4):
    for j in range(i):
        print("*", end="")
    print()
```

Output:

```
*
**
***
```

---

### 3. Multiplication Table

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")
```

---

### 4. Searching for a Condition

```python
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == 25:
            print(i, j)
```

---

## 🔄 Nested Loops with `while`

Nested loops can also be created using `while`:

```python
i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1
```

---

## 🧱 Loop Hierarchy

* Outer loop → controls main repetition
* Inner loop → runs completely for each outer iteration

👉 Total iterations = outer × inner

Example:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

👉 Executes **3 × 2 = 6 times**

---

## 🪜 Problem-Solving Approach

### 1. Identify repetition levels

👉 How many loops are needed?

---

### 2. Define loop roles

* outer loop → main control
* inner loop → detailed repetition

---

### 3. Determine boundaries

👉 start and end values for each loop

---

### 4. Understand execution order

👉 inner loop always completes fully

---

### 5. Test with small values

👉 easier to debug and understand

---

## 📏 Common Patterns

---

### Triangle Pattern

```python
for i in range(1, 5):
    for j in range(i):
        print(j + 1, end=" ")
    print()
```

---

### Reverse Pattern

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

---

## ⚠️ Common Mistakes

### 1. Incorrect loop ranges

👉 leads to missing or extra output

---

### 2. Misplacing print statements

👉 affects formatting

---

### 3. Forgetting inner loop reset (`while`)

```python
# Wrong
while i <= 3:
    while j <= 2:
        ...
```

👉 `j` must be reset inside outer loop

---

### 4. Confusing loop variables

👉 using same variable names incorrectly

---

### 5. Performance issues

👉 too many nested loops can slow programs

---

## 🔄 Using `break` in Nested Loops

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

👉 `break` only stops the **inner loop**

---

## 🔄 Using `continue`

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
```

👉 skips current inner iteration

---

## 🧠 Skills Developed

* Understanding multi-level repetition
* Working with combinations and patterns
* Building structured and layered logic
* Improving algorithmic thinking
* Managing complex loop behavior

---

## 🔄 Connection to Previous Lectures

Previously:

* `for` loop → fixed repetition
* `while` loop → condition-based repetition

Now:

* nested loops → multiple levels of repetition

👉 This enables solving significantly more complex problems.

---

## 🎯 Conclusion

Nested loops are a powerful tool for handling complex repetitive logic.
They allow programs to process combinations, generate patterns, and work with structured data efficiently.

Mastering nested loops is essential for progressing to more advanced programming concepts such as algorithms, matrices, and data processing.

---
