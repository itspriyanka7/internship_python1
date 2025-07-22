# 📘 Python List

Python `list` is a built-in data type used to store multiple items in a single variable.

---

## ✅ Creating a List

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.5, True]
```

---

## 🧠 List Features

- Ordered
- Changeable (mutable)
- Allows duplicate values
- Can store different data types

---

## 🧪 Accessing List Items

```python
print(fruits[0])     # Output: apple
print(fruits[-1])    # Output: cherry (last item)
```

---

## 🔁 Looping Through a List

```python
for fruit in fruits:
    print(fruit)
```

---

## ➕ List Operations

### Add Items

```python
fruits.append("orange")     # Add at the end
fruits.insert(1, "mango")   # Insert at position 1
```

### Remove Items

```python
fruits.remove("banana")     # Remove specific item
fruits.pop()                # Remove last item
del fruits[0]               # Delete by index
```

---

## 📏 List Length

```python
print(len(fruits))
```

---

## 🔄 List Methods

| Method         | Description                          |
|----------------|--------------------------------------|
| append()       | Adds an item to the end              |
| insert()       | Inserts an item at specified index   |
| remove()       | Removes a specific item              |
| pop()          | Removes the last item                |
| clear()        | Removes all items                    |
| sort()         | Sorts the list                       |
| reverse()      | Reverses the list                    |
| copy()         | Returns a copy of the list           |

---

## 🧪 List Slicing

```python
print(fruits[1:3])   # Items from index 1 to 2
```

---

## 📋 List Comprehension

```python
squares = [x*x for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

## 📌 Nested Lists

```python
nested = [[1, 2], [3, 4]]
print(nested[1][0])  # Output: 3
```
