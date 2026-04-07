# Arrays (Lists in Python)

This lecture introduces the concept of **arrays**, which in Python are implemented as **lists**.
Lists allow storing and managing multiple values in a single variable, making programs more efficient and scalable.

---

## 📚 What Are Arrays (Lists)?

An array (or list in Python) is a collection of elements stored in a specific order.

```python id="0g1mrm"
numbers = [1, 2, 3, 4, 5]
```

Each element in the list has an index:

* first element → index `0`
* second element → index `1`
* and so on

---

## 🔢 Accessing Elements

```python id="0c6x2x"
numbers = [10, 20, 30]

print(numbers[0])  # 10
print(numbers[2])  # 30
```

---

## 🔄 Modifying Elements

```python id="fc5h0w"
numbers = [1, 2, 3]
numbers[1] = 10

print(numbers)  # [1, 10, 3]
```

---

## 📏 List Length

```python id="w9r7zp"
numbers = [1, 2, 3]
print(len(numbers))  # 3
```

---

## 🔁 Iterating Through Lists

### Using `for` loop:

```python id="f5k3m1"
numbers = [1, 2, 3]

for num in numbers:
    print(num)
```

---

### Using index:

```python id="h68zzt"
for i in range(len(numbers)):
    print(numbers[i])
```

---

## ➕ Adding Elements

```python id="1y6y1m"
numbers = [1, 2]
numbers.append(3)

print(numbers)  # [1, 2, 3]
```

---

## ➖ Removing Elements

```python id="5j0e7v"
numbers = [1, 2, 3]
numbers.remove(2)

print(numbers)  # [1, 3]
```

---

## 🔄 Other Common Operations

```python id="8zh4dn"
numbers.insert(1, 100)
numbers.pop()
numbers.sort()
numbers.reverse()
```

---

## 🧠 Reading Lists from Input

```python id="8a2o0d"
numbers = list(map(int, input().split()))
```

👉 This reads multiple numbers from a single line.

---

## 🧮 Common Tasks with Lists

---

### 1. Sum of Elements

```python id="8jpl7p"
numbers = [1, 2, 3]
total = sum(numbers)
```

---

### 2. Finding Maximum / Minimum

```python id="6zyvlj"
print(max(numbers))
print(min(numbers))
```

---

### 3. Filtering Elements

```python id="x9zvhd"
for num in numbers:
    if num % 2 == 0:
        print(num)
```

---

### 4. Searching for Element

```python id="z6z2nx"
if 5 in numbers:
    print("Found")
```

---

## 🧩 Typical Problem Types

---

### 1. Processing Sequences

* reading multiple values
* applying operations

---

### 2. Filtering Data

* selecting specific elements

---

### 3. Transforming Data

* modifying elements

---

### 4. Aggregation

* sum, count, average

---

## 🪜 Problem-Solving Approach

### 1. Read input into a list

---

### 2. Iterate through elements

---

### 3. Apply logic

---

### 4. Store or update results

---

### 5. Output final result

---

## 📏 Edge Cases

* empty list
* single element
* duplicate values
* negative numbers

---

## 🚫 Common Mistakes

### 1. Index out of range

```python id="j1h8r0"
print(numbers[5])  # error
```

---

### 2. Modifying list while iterating

---

### 3. Incorrect input parsing

---

### 4. Forgetting type conversion

---

### 5. Confusing index vs value

---

## 🔄 Connection to Previous Lectures

Previously:

* working with single values

Now:

* working with collections of values

👉 This significantly expands problem-solving capabilities.

---

## 🧠 Skills Developed

* working with collections
* iterating over data
* processing sequences
* writing more efficient solutions
* understanding indexed structures

---

## 🎯 Conclusion

Lists (arrays) are a fundamental data structure that allow handling multiple values efficiently.
They are essential for solving real-world problems involving collections of data.

Mastering lists is a key step toward more advanced topics such as dictionaries, functions, and complex algorithms.

---
