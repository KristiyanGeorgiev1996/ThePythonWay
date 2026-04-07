# Objects and Classes

This lecture introduces the fundamentals of **object-oriented programming (OOP)**, focusing on classes and objects.
It marks a significant step from procedural programming toward more structured and scalable software design.

---

## 📚 What Are Classes and Objects?

A **class** is a blueprint for creating objects.
An **object** is an instance of a class.

```python
class Person:
    pass
```

```python
person = Person()
```

---

## 🧠 Why Use Classes?

Classes help to:

* organize code into logical structures
* model real-world entities
* group related data and behavior
* improve code readability and maintainability

---

## 🔢 Defining a Class

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

👉 `__init__` is a constructor that initializes object data.

---

## 🔄 Creating Objects

```python
person = Person("John", 25)
```

---

## 📦 Attributes

Attributes are variables stored inside an object.

```python
print(person.name)
print(person.age)
```

---

## 🔁 Methods

Methods are functions defined inside a class.

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}"
```

```python
person = Person("John")
print(person.greet())
```

---

## 🔗 `self` Keyword

`self` refers to the current instance of the class.

👉 It is used to:

* access attributes
* call methods within the class

---

## 🔄 Modifying Object Data

```python
person.age = 30
```

---

## 🧩 Multiple Objects

```python
p1 = Person("Alice", 20)
p2 = Person("Bob", 30)
```

👉 Each object has its own data.

---

## 🧮 Example Use Case

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
```

---

## 🔄 Object Interaction

Objects can interact through methods and data.

---

## 🧱 Encapsulation (Basic Idea)

Encapsulation means grouping data and methods together.

👉 This helps protect and organize code.

---

## 🧩 Typical Problem Types

---

### 1. Modeling Data

* representing real-world objects

---

### 2. Grouping Logic

* combining data and behavior

---

### 3. Managing State

* tracking object properties

---

### 4. Simplifying Code

* replacing complex logic with structured objects

---

## 🪜 Problem-Solving Approach

### 1. Identify the entity

👉 what object should be created

---

### 2. Define attributes

👉 what data it holds

---

### 3. Define methods

👉 what actions it performs

---

### 4. Create objects

---

### 5. Use objects in logic

---

## 📏 Edge Cases

* missing or invalid data
* incorrect attribute initialization
* accessing non-existing attributes

---

## 🚫 Common Mistakes

### 1. Forgetting `self`

```python
def greet():  # wrong
```

---

### 2. Incorrect constructor usage

---

### 3. Misunderstanding object instances

---

### 4. Using global variables instead of class attributes

---

### 5. Overcomplicating simple problems

---

## 🔄 Connection to Previous Lectures

Previously:

* working with variables and functions

Now:

* grouping data and logic into objects

👉 This is a major step toward scalable and real-world applications.

---

## 🧠 Skills Developed

* understanding object-oriented concepts
* structuring code using classes
* modeling real-world problems
* improving code organization
* writing reusable and scalable code

---

## 🎯 Conclusion

Classes and objects are fundamental to modern programming.
They enable building structured, modular, and scalable applications.

Mastering this topic is essential for advanced programming concepts such as inheritance, polymorphism, and full object-oriented design.

---
