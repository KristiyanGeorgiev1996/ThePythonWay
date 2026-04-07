# More Complex Conditional Statements

This lecture builds upon the basic conditional structures by introducing more advanced logic through combining conditions, nested checks, and handling multiple scenarios.

At this stage, programs no longer evaluate a single condition, but instead make decisions based on **multiple factors simultaneously**.

---

## 📚 What Does “More Complex Logic” Mean?

In the previous lecture, the focus was on simple checks such as:

* comparing values
* checking if a number falls within a range

Now the focus expands to:

* combining multiple conditions
* working with logical operators
* nested conditional structures
* handling multiple possible outcomes

---

## 🔗 Combining Conditions

Often, more than one condition must be evaluated.

---

### Using `and`

Both conditions must be true:

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Access granted")
```

---

### Using `or`

At least one condition must be true:

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

---

### Using `not`

Reverses the condition:

```python
is_holiday = False

if not is_holiday:
    print("Work day")
```

---

## 🧠 Nested Conditional Statements

Nested conditions allow performing additional checks inside another condition.

```python
age = int(input())

if age >= 18:
    print("Adult")
    if age >= 65:
        print("Senior")
else:
    print("Minor")
```

### How it works:

* the outer condition is evaluated first
* if true → the inner condition is checked
* the inner condition runs independently within the outer block

---

## ⚖️ When to Use Nested `if`

Use nested conditions when:

* one condition depends on another
* the second check only makes sense if the first is true

❗ If conditions are independent → prefer `if-elif`

---

## 🔄 Simplifying Nested Conditions

Nested conditions can often be simplified using logical operators.

### Instead of:

```python
if age >= 18:
    if has_ticket:
        print("Access granted")
```

### Use:

```python
if age >= 18 and has_ticket:
    print("Access granted")
```

👉 This makes the code:

* shorter
* more readable

---

## 🧩 More Complex Scenarios

Tasks in this lecture often include:

* string-based input (types, categories, days)
* multiple conditions combined
* different outputs based on various cases

---

### Example: Behavior Based on Day

```python
day = input()

if day == "Monday" or day == "Tuesday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Unknown day")
```

---

## 🔠 Working with Strings in Conditions

```python
user_type = input()

if user_type == "student":
    print("Discount applied")
```

### Important:

* comparisons are **case-sensitive**
* `"Student"` is not equal to `"student"`

---

## 🧮 Combined Conditions

```python
age = int(input())
gender = input()

if age < 16 and gender == "m":
    print("Boy")
elif age >= 16 and gender == "m":
    print("Man")
elif age < 16 and gender == "f":
    print("Girl")
else:
    print("Woman")
```

👉 This demonstrates:

* classification based on multiple criteria

---

## 🧱 Increasing Logical Complexity

As conditions increase:

* code becomes longer
* logic becomes harder to follow

👉 Therefore:

* keep conditions clear
* avoid unnecessary checks
* structure logic carefully

---

## 🪜 Problem-Solving Approach

### 1. Identify all possible cases

* categories
* ranges
* combinations

---

### 2. Break down the logic

* which conditions are related
* which can be combined

---

### 3. Choose the right structure

* `if-elif-else` → multiple outcomes
* nested `if` → dependent checks
* logical operators → combined conditions

---

### 4. Order conditions correctly

Order matters for correct execution.

---

### 5. Test thoroughly

Especially:

* edge cases
* different combinations

---

## 📏 Edge Cases

Complex logic often introduces:

* overlapping conditions
* missing scenarios

Examples:

* values at exact boundaries
* unexpected but valid input

---

## 🚫 Common Mistakes

### 1. Overly complex conditions

Hard to read and maintain

---

### 2. Missing cases

Not all inputs are handled

---

### 3. Incorrect condition order

General condition placed before a specific one

---

### 4. Repeated logic

Same condition checked multiple times

---

### 5. String comparison errors

Case sensitivity and spacing issues

---

## 🧠 Skills Developed

* Combining logical conditions
* Working with multiple criteria
* Structuring complex decision-making
* Analyzing problem requirements
* Optimizing conditional logic

---

## 🔄 Connection to Previous Lecture

Previously:

* simple conditions

Now:

* combined logic
* nested conditions
* multiple scenarios

👉 This is a natural progression from basic conditional statements.

---

## 🎯 Conclusion

More complex conditional statements allow building realistic program logic.
They enable programs to evaluate multiple factors and handle diverse scenarios effectively.

Mastering this topic is essential for progressing toward more advanced programming concepts and real-world problem solving.

---
