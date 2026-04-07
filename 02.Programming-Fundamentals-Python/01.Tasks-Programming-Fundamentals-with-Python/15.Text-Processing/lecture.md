# Text Processing

This lecture focuses on **processing and manipulating text data (strings)** in Python.
Text processing is a fundamental skill used in many real-world applications such as data parsing, validation, formatting, and transformation.

---

## 📚 What Is Text Processing?

Text processing involves working with strings to:

* analyze content
* extract information
* modify or transform data
* validate input

Strings are sequences of characters and are one of the most commonly used data types.

---

## 🔤 Working with Strings

```python
text = "Hello, World!"
```

Strings can be:

* indexed
* sliced
* iterated
* modified (through new string creation)

---

## 🔢 Accessing Characters

```python
text = "Python"

print(text[0])  # P
print(text[-1]) # n
```

---

## 🔄 String Slicing

```python
text = "Python"

print(text[1:4])  # yth
print(text[:3])   # Pyt
print(text[3:])   # hon
```

---

## 🔁 Iterating Through Strings

```python
for char in text:
    print(char)
```

---

## 🔄 String Methods

---

### Changing Case

```python
text.lower()
text.upper()
text.capitalize()
```

---

### Removing Spaces

```python
text.strip()
```

---

### Replacing Text

```python
text.replace("a", "b")
```

---

### Splitting Text

```python
words = text.split()
```

---

### Joining Text

```python
" ".join(words)
```

---

## 🔍 Searching in Strings

```python
if "Python" in text:
    print("Found")
```

---

## 🔢 Counting Occurrences

```python
text.count("a")
```

---

## 🔄 Building New Strings

```python
result = ""

for char in text:
    result += char.upper()
```

---

## 🧮 Common Use Cases

---

### 1. Filtering Characters

```python
for char in text:
    if char.isdigit():
        print(char)
```

---

### 2. Extracting Words

```python
words = text.split()
```

---

### 3. Replacing Patterns

```python
text.replace("hello", "hi")
```

---

### 4. Validation

```python
if text.isalpha():
    print("Only letters")
```

---

## 🧩 Typical Problem Types

---

### 1. Parsing Input

* breaking text into parts

---

### 2. Filtering Data

* extracting specific characters

---

### 3. Transforming Text

* modifying format

---

### 4. Validating Input

* checking text conditions

---

## 🪜 Problem-Solving Approach

### 1. Understand input format

👉 string or multiple strings

---

### 2. Decide processing method

👉 loop, split, replace

---

### 3. Apply transformations

---

### 4. Build result

---

### 5. Output final string

---

## 📏 Edge Cases

* empty string
* special characters
* spaces and formatting
* mixed input (letters + numbers)

---

## 🚫 Common Mistakes

### 1. Modifying strings directly

(strings are immutable)

---

### 2. Incorrect slicing

---

### 3. Ignoring case sensitivity

---

### 4. Improper splitting

---

### 5. Inefficient string concatenation

---

## 🔄 Connection to Previous Lectures

Previously:

* working with numbers and collections

Now:

* working with text data

👉 This expands programming capabilities significantly.

---

## 🧠 Skills Developed

* working with strings
* parsing and transforming text
* validating input
* extracting meaningful data
* building efficient string operations

---

## 🎯 Conclusion

Text processing is a critical skill in programming.
It allows handling and transforming textual data, which is essential in many real-world applications.

Mastering string operations is key to working with data, user input, and communication between systems.

---
