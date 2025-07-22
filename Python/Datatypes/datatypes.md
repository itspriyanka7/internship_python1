
# 📘 Python Data Types
Python has several built-in data types used to store values of different kinds.

---

## 🧠 1. Basic Data Types

| Type  | Example        | Description                          |
|-------|----------------|--------------------------------------|
| int   | 10, -5         | Integer numbers (no decimal)         |
| float | 3.14, -0.5     | Decimal numbers                      |
| str   | "Hello", 'A'   | Text (a sequence of characters)      |
| bool  | True, False    | Boolean (true or false) values       |

---

## 📦 2. Collection Data Types

| Type  | Example                          | Description                            |
|-------|----------------------------------|----------------------------------------|
| list  | [1, 2, 3]                        | Ordered, changeable, allows duplicates |
| tuple | (1, 2, 3)                        | Ordered, unchangeable                  |
| set   | {1, 2, 3}                        | Unordered, no duplicates               |
| dict  | {"name": "Alice", "age": 25}     | Key-value pairs                        |

---

## 🧪 3. Other Data Types

| Type       | Description                              |
|------------|------------------------------------------|
| NoneType   | Represents null/empty value (`None`)     |
| complex    | Complex numbers like `2 + 3j`            |
| bytes      | Immutable sequence of bytes              |
| bytearray  | Mutable sequence of bytes                |
| range      | Sequence of numbers (`range(5)`)         |


## 🔍 Example

```python
name = "Alice"        # str
age = 25              # int
height = 5.6          # float
is_student = True     # bool
grades = [90, 85, 92] # list
info = {"city": "Pune", "pin": 411001}  # dict
```
## ✅ Use type() to check datatype:

```python
print(type(name))  # <class 'str'>
```
