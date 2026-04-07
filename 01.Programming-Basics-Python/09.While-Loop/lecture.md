# While Loop

This lecture introduces the concept of **conditional repetition** using the `while` loop.
Unlike the `for` loop, which runs a fixed number of times, the `while` loop continues executing **as long as a given condition is true**.

---

## 📚 What is a `while` Loop?

A `while` loop repeatedly executes a block of code **while a condition remains true**.

```python
while condition:
    # code block
```

👉 The loop:

1. checks the condition
2. executes the block if the condition is true
3. repeats until the condition becomes false

---

## 🔁 Basic Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

### How it works:

* starts from `count = 1`
* prints the value
* increases `count`
* repeats until `count > 5`

---

## 🔄 When to Use `while`?

Use a `while` loop when:

* the number of repetitions is **not known in advance**
* execution depends on a condition
* input is read until a certain value appears

---

## 🔢 Difference Between `for` and `while`

| `for` loop                 | `while` loop                 |
| -------------------------- | ---------------------------- |
| Fixed number of iterations | Unknown number of iterations |
| Uses `range()`             | Uses a condition             |
| Controlled by sequence     | Controlled by logic          |

---

## 🧠 Loop Control Variable

A `while` loop requires a variable that changes over time.

```python
i = 0

while i < 3:
    print(i)
    i += 1
```

👉 Without updating `i`, the loop would run forever.

---

## ⚠️ Infinite Loops

An infinite loop occurs when the condition never becomes false.

```python
while True:
    print("Infinite loop")
```

👉 This loop never stops unless manually interrupted.

---

## 🛑 Avoiding Infinite Loops

Always ensure:

* the condition will eventually become false
* the control variable is updated correctly

---

## 🧩 Common Use Cases

---

### 1. Reading Input Until a Condition

```python
text = input()

while text != "Stop":
    print(text)
    text = input()
```

👉 Continues until `"Stop"` is entered

---

### 2. Accumulating Values

```python
total = 0
number = int(input())

while number != 0:
    total += number
    number = int(input())

print(total)
```

👉 Stops when `0` is entered

---

### 3. Counting Iterations

```python
count = 0
number = int(input())

while number >= 0:
    count += 1
    number = int(input())

print(count)
```

---

### 4. Validating Input

```python
password = input()

while password != "secret":
    password = input()

print("Access granted")
```

👉 Repeats until correct input is provided

---

## 🔁 Loop Flow

Typical structure:

```python
initialization

while condition:
    action
    update
```

---

## 🔄 `break` Statement

Stops the loop immediately:

```python
while True:
    text = input()
    
    if text == "Stop":
        break
    
    print(text)
```

---

## 🔄 `continue` Statement

Skips the current iteration:

```python
number = 0

while number < 5:
    number += 1
    
    if number == 3:
        continue
    
    print(number)
```

👉 Skips printing `3`

---

## 🪜 Problem-Solving Approach

### 1. Identify the stopping condition

👉 when should the loop end

---

### 2. Define initial values

👉 starting point

---

### 3. Ensure proper updates

👉 prevent infinite loops

---

### 4. Decide if `break` is needed

👉 for early termination

---

## 📏 Edge Cases

Important to consider:

* first input value
* boundary conditions
* stopping values

---

## 🚫 Common Mistakes

### 1. Missing update

```python
while i < 5:
    print(i)
```

👉 infinite loop

---

### 2. Wrong condition

---

### 3. Input not updated inside loop

---

### 4. Incorrect termination logic

---

### 5. Overusing `while` instead of `for`

---

## 🧠 Skills Developed

* Working with condition-based repetition
* Handling unknown iteration counts
* Input validation
* Loop control and flow management
* Writing flexible and dynamic programs

---

## 🔄 Connection to Previous Lecture

Previously:

* `for` loop → fixed repetitions

Now:

* `while` loop → condition-based repetition

👉 This introduces more flexible program control.

---

## 🎯 Conclusion

The `while` loop is essential for handling situations where the number of iterations is not predetermined.
It allows programs to run dynamically based on conditions and user input.

Mastering `while` loops is crucial for building interactive and real-world applications.

---
