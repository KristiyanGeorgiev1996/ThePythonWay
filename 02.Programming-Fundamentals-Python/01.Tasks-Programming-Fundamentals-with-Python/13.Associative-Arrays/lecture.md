# Associative Arrays (Dictionaries)

This lecture introduces **associative arrays**, known in Python as **dictionaries**.
Dictionaries allow storing and managing data using **key-value pairs**, making them highly efficient for structured and fast data access.

---

## 📚 What Is a Dictionary?

A dictionary is a collection of key-value pairs.

```python
student = {
    "name": "John",
    "age": 25,
    "grade": 5.50
}
```

👉 Each key is unique and maps to a specific value.

---

## 🔍 Accessing Values

```python
print(student["name"])  # John
```

---

## 🔄 Modifying Values

```python
student["age"] = 26
```

---

## ➕ Adding Elements

```python
student["city"] = "Sofia"
```

---

## ➖ Removing Elements

```python
del student["age"]
```

---

## 🔁 Iterating Through Dictionaries

### Keys:

```python
for key in student:
    print(key)
```

---

### Values:

```python
for value in student.values():
    print(value)
```

---

### Key-Value Pairs:

```python
for key, value in student.items():
    print(key, value)
```

---

## 🔢 Checking for Key Existence

```python
if "name" in student:
    print("Key exists")
```

---

## 📏 Dictionary Length

```python
print(len(student))
```

---

## 🔄 Nested Dictionaries

```python
students = {
    "student1": {"name": "John", "age": 20},
    "student2": {"name": "Anna", "age": 22}
}
```

---

## 🔄 Dictionary Methods

```python
student.get("name")
student.keys()
student.values()
student.items()
```

---

## 🧮 Common Use Cases

---

### 1. Counting Occurrences

```python
text = "hello"

counts = {}

for char in text:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1
```

---

### 2. Grouping Data

```python
groups = {}

for num in [1, 2, 3, 4]:
    groups[num] = num * num
```

---

### 3. Storing Structured Data

```python
products = {
    "apple": 1.20,
    "banana": 0.80
}
```

---

### 4. Fast Lookup

```python
if "apple" in products:
    print(products["apple"])
```

---

## 🧩 Typical Problem Types

---

### 1. Frequency Counting

* counting occurrences of elements

---

### 2. Data Mapping

* linking keys to values

---

### 3. Data Aggregation

* storing computed results

---

### 4. Nested Structures

* organizing complex data

---

## 🪜 Problem-Solving Approach

### 1. Identify key-value relationship

👉 what should be the key and value

---

### 2. Initialize dictionary

---

### 3. Process input

---

### 4. Update dictionary

---

### 5. Output results

---

## 📏 Edge Cases

* missing keys
* duplicate keys (overwriting values)
* empty dictionary
* large datasets

---

## 🚫 Common Mistakes

### 1. Accessing non-existing keys

```python
print(student["city"])  # error
```

---

### 2. Not checking for key existence

---

### 3. Overwriting values unintentionally

---

### 4. Confusing keys and values

---

### 5. Incorrect iteration usage

---

## 🔄 Connection to Previous Lectures

Previously:

* lists → indexed data

Now:

* dictionaries → key-based data

👉 This allows more flexible and efficient data handling.

---

## 🧠 Skills Developed

* working with key-value structures
* organizing structured data
* counting and grouping data
* efficient data lookup
* building more complex data models

---

## 🎯 Conclusion

Dictionaries are one of the most powerful data structures in Python.
They provide fast access, flexible organization, and efficient data handling.

Mastering dictionaries is essential for real-world programming, especially when working with structured or large datasets.

---
