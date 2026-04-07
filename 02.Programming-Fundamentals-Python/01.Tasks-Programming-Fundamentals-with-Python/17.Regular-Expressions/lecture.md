# Regular Expressions (Regex)

This lecture introduces **regular expressions (regex)** — a powerful tool for pattern matching and text processing.
Regex allows searching, validating, and extracting information from text efficiently using predefined patterns.

---

## 📚 What Are Regular Expressions?

Regular expressions are sequences of characters that define a **search pattern**.

They are used to:

* find specific text
* validate input formats
* extract data from strings
* replace patterns

---

## 🔧 Using Regex in Python

Python provides the built-in `re` module:

```python id="4yzf7k"
import re
```

---

## 🔍 Searching for Patterns

```python id="6z1qlp"
text = "Hello 123"

match = re.search(r"\d+", text)

if match:
    print(match.group())
```

👉 Finds the first sequence of digits

---

## 🔁 Finding All Matches

```python id="g0xpxv"
numbers = re.findall(r"\d+", text)
```

👉 Returns all matches in a list

---

## 🔄 Matching Patterns

```python id="c8f1nm"
match = re.match(r"Hello", text)
```

👉 Checks only at the beginning of the string

---

## 🔄 Replacing Patterns

```python id="q7d6ux"
result = re.sub(r"\d+", "#", text)
```

👉 Replaces digits with `#`

---

## 🔤 Common Regex Patterns

| Pattern | Meaning            |
| ------- | ------------------ |
| `\d`    | digit              |
| `\D`    | non-digit          |
| `\w`    | word character     |
| `\W`    | non-word character |
| `\s`    | whitespace         |
| `.`     | any character      |

---

## 🔢 Quantifiers

| Symbol  | Meaning               |
| ------- | --------------------- |
| `+`     | one or more           |
| `*`     | zero or more          |
| `?`     | zero or one           |
| `{n}`   | exactly n times       |
| `{n,m}` | between n and m times |

---

### Example:

```python id="l2bhr7"
re.findall(r"\d{3}", "123 4567 89")
```

👉 Matches sequences of exactly 3 digits

---

## 🔗 Character Classes

```python id="n0f43d"
re.findall(r"[A-Za-z]", text)
```

👉 Matches letters

---

## 🔍 Groups

```python id="ytn1uy"
match = re.search(r"(\d+)", text)
print(match.group(1))
```

👉 Extracts specific parts of a match

---

## 🧮 Common Use Cases

---

### 1. Extracting Numbers

```python id="fq7h84"
re.findall(r"\d+", text)
```

---

### 2. Validating Email

```python id="3u4dpn"
pattern = r"[a-z]+@[a-z]+\.[a-z]+"
```

---

### 3. Parsing Data

```python id="iv5w0n"
re.findall(r"[A-Za-z]+", text)
```

---

### 4. Replacing Patterns

```python id="p04p7n"
re.sub(r"\s+", "-", text)
```

---

## 🧩 Typical Problem Types

---

### 1. Pattern Matching

* finding specific sequences

---

### 2. Validation

* checking if input matches format

---

### 3. Extraction

* retrieving parts of text

---

### 4. Transformation

* replacing or modifying content

---

## 🪜 Problem-Solving Approach

### 1. Identify the pattern

👉 what needs to be matched

---

### 2. Build regex expression

---

### 3. Choose correct function

* `search`
* `findall`
* `match`
* `sub`

---

### 4. Apply to input

---

### 5. Validate results

---

## 📏 Edge Cases

* empty strings
* no matches
* overlapping patterns
* special characters

---

## 🚫 Common Mistakes

### 1. Incorrect pattern syntax

---

### 2. Forgetting raw strings (`r""`)

---

### 3. Overly complex expressions

---

### 4. Not testing patterns

---

### 5. Confusing `match` vs `search`

---

## 🔄 Connection to Previous Lectures

Previously:

* basic text processing

Now:

* advanced pattern-based text handling

👉 This enables powerful data extraction and validation.

---

## 🧠 Skills Developed

* pattern recognition
* advanced text processing
* data extraction and validation
* working with regex tools
* writing efficient text-handling solutions

---

## 🎯 Conclusion

Regular expressions are a powerful tool for working with text data.
They allow efficient searching, validation, and transformation of strings using flexible patterns.

Mastering regex significantly enhances the ability to handle complex data-processing tasks in real-world applications.

---
