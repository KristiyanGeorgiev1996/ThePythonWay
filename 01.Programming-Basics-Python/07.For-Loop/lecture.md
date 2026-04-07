# For Loop

This lecture introduces the concept of **repetition in programming** using loops.
Until now, programs executed each instruction only once. With the `for` loop, a block of code can be executed multiple times.

---

## 📚 What is a Loop?

A loop is a programming construct that allows a block of code to be executed **repeatedly**.

It is especially useful when:

* the same action needs to be performed multiple times
* a sequence of values must be processed
* repetitive calculations are required

---

## 🔁 What is a `for` Loop?

A `for` loop is used when the number of repetitions is **known in advance**.

```python
for i in range(5):
    print(i)
```

---

## 🔢 The `range()` Function

The `range()` function generates a sequence of numbers.

### Main forms:

```python
range(n)
```

👉 generates numbers from `0` to `n-1`

```python
range(start, end)
```

👉 generates numbers from `start` to `end-1`

```python
range(start, end, step)
```

👉 generates numbers with a defined step

---

### Examples:

```python
for i in range(5):
    print(i)
```

Output:

```
0 1 2 3 4
```

---

```python
for i in range(1, 6):
    print(i)
```

Output:

```
1 2 3 4 5
```

---

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```
1 3 5 7 9
```

---

## 🧠 Loop Variable

The variable used in the loop (e.g., `i`) is called the **iterator**.

It:

* takes a different value on each iteration
* can be used for calculations or conditions

```python
for i in range(3):
    print("Iteration:", i)
```

---

## 🧩 Common Use Cases of `for` Loops

---

### 1. Repeating an Action

```python
for i in range(5):
    print("Hello")
```

👉 Prints "Hello" 5 times

---

### 2. Summing Numbers

```python
total = 0

for i in range(1, 6):
    total += i

print(total)
```

👉 Sums numbers from 1 to 5

---

### 3. Finding Maximum / Minimum

```python
max_number = -999999

for i in range(5):
    number = int(input())
    if number > max_number:
        max_number = number

print(max_number)
```

---

### 4. Counting Events

```python
count = 0

for i in range(10):
    number = int(input())
    if number % 2 == 0:
        count += 1

print(count)
```

👉 Counts even numbers

---

### 5. Iterating Through Text

```python
text = "Python"

for char in text:
    print(char)
```

👉 Iterates through each character

---

## 🔄 Accumulator Variables

These are variables that collect values during each iteration.

Common examples:

* sum (`total`)
* count (`count`)
* maximum (`max`)
* minimum (`min`)

---

## 🪜 Problem-Solving Approach

### 1. Determine how many repetitions are needed

👉 defines the `range()`

---

### 2. Define what happens in each iteration

👉 calculation, condition, or output

---

### 3. Decide if accumulation is needed

👉 sum, count, etc.

---

### 4. Check if conditions are required inside the loop

👉 combine with `if`

---

## 📏 Start and End of the Loop

Important concept:

* start value
* end value (NOT included)

```python
range(1, 5)
```

👉 produces: `1, 2, 3, 4`

---

## ⚠️ Common Mistakes

### 1. Incorrect range

```python
range(1, 5)  # does not include 5
```

---

### 2. Incorrect initialization

```python
total = 0  # must be outside the loop
```

---

### 3. Overwriting instead of accumulating

```python
total = i   # wrong
total += i  # correct
```

---

### 4. Logic outside the loop

Sometimes calculations must be inside the loop, not after it.

---

## 🔄 Nested Loops (Brief Overview)

A loop inside another loop:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

👉 the inner loop runs for every iteration of the outer loop

(This topic is covered in more detail in a later lecture.)

---

## 🧠 Skills Developed

* Thinking in repetition
* Working with sequences
* Accumulating values
* Combining loops with conditions
* Automating repetitive tasks

---

## 🔄 Connection to Previous Lectures

Previously:

* input/output
* conditional logic

Now:

* repeating logic
* processing multiple values

👉 This is a key step toward solving more complex problems.

---

## 🎯 Conclusion

The `for` loop is one of the most fundamental tools in programming.
It enables automation of repetitive tasks and efficient processing of multiple values.

Mastering it is essential for:

* algorithm development
* working with collections and data structures
* building more advanced programs

---
