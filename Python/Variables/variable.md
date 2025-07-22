# 🐍 Python Variables

Variables in Python are used to store data values. They act as containers for storing information.

---

## 📘 What is a Variable?

A **variable** is a name that refers to a value stored in memory. In Python, you don’t need to declare the type of variable. Python is dynamically typed.

Example:
```python
x = 10
name = "Alice"
```

---

## 🔤 Rules for Naming Variables

1. Must begin with a letter (a–z, A–Z) or underscore (_)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (`myVar` and `myvar` are different)
4. Cannot use reserved keywords (like `class`, `for`, `if`, etc.)

---

## 🧠 Variable Assignment

You assign a value to a variable using the `=` operator.

```python
x = 5
name = "John"
price = 99.99
```

---

## 🔁 Multiple Assignment

You can assign multiple variables in a single line:

```python
a, b, c = 1, 2, 3
```

Or assign the same value to multiple variables:

```python
x = y = z = 100
```

---

## 🧪 Variable Types

Python automatically detects the variable type:

| Type      | Example           |
|-----------|-------------------|
| int       | `x = 10`          |
| float     | `price = 10.5`    |
| str       | `name = "Tom"`    |
| bool      | `flag = True`     |
| list      | `fruits = ["a"]`  |
| tuple     | `t = (1, 2)`      |
| dict      | `d = {"a": 1}`    |

---

## 🔄 Dynamic Typing

Python allows you to change the type of variable:

```python
x = 10      # int
x = "Ten"   # now str
```

---

## 🧹 Deleting Variables

Use `del` to delete a variable:

```python
x = 10
del x
```

Trying to access `x` after deletion will raise an error.

---

## 🛑 Reserved Keywords (Cannot Be Used as Variable Names)

| False | class | finally | is | return |
|-------|-------|---------|----|--------|
| None  | continue | for | lambda | try |
| True  | def | from | nonlocal | while |
| and   | del | global | not | with |
| as    | elif | if | or | yield |
| assert| else | import | pass | break |
| except| in | raise |

---

## ✅ Summary

- Variables store data.
- No need to declare types explicitly.
- Use meaningful names for readability.
- Follow naming rules to avoid errors.

