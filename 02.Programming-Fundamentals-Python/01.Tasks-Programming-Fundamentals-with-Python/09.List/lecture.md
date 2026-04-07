# Lists (Advanced List Operations)

This lecture expands on the concept of lists by introducing more advanced operations and techniques for working with collections of data.

The focus is on manipulating, transforming, and efficiently processing lists in more complex scenarios.

---

## 📚 What Are Lists?

A list is an ordered collection of elements that can store multiple values in a single variable.

```python id="eqm3b7"
numbers = [1, 2, 3, 4]
```

Lists are:

* ordered
* mutable (can be changed)
* able to store different data types

---

## 🔁 Iterating Through Lists

### Using values:

```python id="m9q7l8"
for num in numbers:
    print(num)
```

---

### Using indices:

```python id="2ak2he"
for i in range(len(numbers)):
    print(numbers[i])
```

---

## ➕ Adding Elements

```python id="x7pl8q"
numbers.append(5)
numbers.insert(1, 100)
```

---

## ➖ Removing Elements

```python id="4w33xz"
numbers.remove(2)
numbers.pop()
numbers.pop(0)
```

---

## 🔄 Modifying Lists

```python id="r9xgq7"
numbers[0] = 10
```

---

## 🔀 Sorting Lists

```python id="ewd09z"
numbers.sort()
numbers.sort(reverse=True)
```

---

## 🔄 Reversing Lists

```python id="gn08jf"
numbers.reverse()
```

---

## 🔍 Searching in Lists

```python id="5q0p3l"
if 3 in numbers:
    print("Found")
```

---

## 🔢 List Slicing

```python id="u7r4lf"
numbers = [1, 2, 3, 4, 5]

print(numbers[1:4])  # [2, 3, 4]
print(numbers[:3])   # [1, 2, 3]
print(numbers[2:])   # [3, 4, 5]
```

---

## 🔄 List Comprehension

A powerful way to create lists:

```python id="sz5ql2"
numbers = [x for x in range(5)]
```

---

### With condition:

```python id="rbt1a1"
even_numbers = [x for x in range(10) if x % 2 == 0]
```

---

## 🧮 Common Operations

---

### 1. Filtering Elements

```python id="x8b91k"
filtered = [x for x in numbers if x > 5]
```

---

### 2. Transforming Data

```python id="3y6kxa"
squared = [x * x for x in numbers]
```

---

### 3. Counting Elements

```python id="bx5v3n"
count = numbers.count(2)
```

---

### 4. Finding Index

```python id="1ktcm3"
index = numbers.index(3)
```

---

## 🔄 Copying Lists

```python id="0j3l5v"
copy = numbers.copy()
```

👉 Avoid direct assignment when copying lists.

---

## 🧩 Typical Problem Types

---

### 1. Filtering and Selection

* extracting elements based on conditions

---

### 2. Data Transformation

* modifying list values

---

### 3. Aggregation

* sum, average, count

---

### 4. Rearranging Data

* sorting, reversing

---

## 🪜 Problem-Solving Approach

### 1. Understand input format

👉 list or sequence

---

### 2. Choose iteration method

---

### 3. Apply logic

---

### 4. Store results

---

### 5. Output correctly

---

## 📏 Edge Cases

* empty list
* single element
* duplicate values
* large lists

---

## 🚫 Common Mistakes

### 1. Index out of range

---

### 2. Modifying list during iteration

---

### 3. Confusing value vs index

---

### 4. Incorrect slicing

---

### 5. Not copying lists properly

---

## 🔄 Connection to Previous Lectures

Previously:

* basic list usage

Now:

* advanced list manipulation

👉 This enables solving more complex data-processing problems.

---

## 🧠 Skills Developed

* working with dynamic collections
* filtering and transforming data
* writing efficient list operations
* using list comprehensions
* improving code readability

---

## 🎯 Conclusion

Advanced list operations are essential for efficient data handling.
They allow transforming and processing large sets of data with concise and readable code.

Mastering lists is a critical step toward working with more advanced structures such as dictionaries, sets, and algorithms.

---
