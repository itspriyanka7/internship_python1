# 📘 Python set – Use and Methods
## 🔹 What is a set?
A set in Python is a collection data type that is:

  - Unordered

  - Unindexed

  - Unchangeable (immutable elements)

  - No duplicate items allowed

 Used when you want to:

   - Store unique items
   - Perform mathematical set operations (like union, intersection)

## 🔹 Set Use (Applications)
✅ Removing duplicates from a list

✅ Membership tests (fast lookup using in)

✅ Set operations – union, intersection, difference

✅ Filtering data based on uniqueness

✅ Mathematical modeling (like Venn diagrams)

## 🔹 Common Set Methods

| Method	|  Description                                     |
|-----------|--------------------------------------------------| 
| add()	    |   Adds a single element to the set               |
| update()	|  Adds multiple elements (from iterable)          |
| remove()	|  Removes a specific element (error if not found) |
| discard()	|  Removes an element (no error if not found)      |
| pop()	    |  Removes and returns a random element            |
| clear()	|  Removes all elements from the set               |
| copy()	|  Returns a shallow copy of the set               |

# 🔹 Set Operations in Python

| **Operation**            | **Method**                             | **Description**                             |
|--------------------------|----------------------------------------|---------------------------------------------|
| **Union**                | `set1.union(set2)`                     | Combines all unique elements from both sets |
| **Intersection**         | `set1.intersection(set2)`              | Returns only the common elements            |
| **Difference**           | `set1.difference(set2)`                | Elements in `set1` but not in `set2`        |
| **Symmetric Difference** | `set1.symmetric_difference(set2)`      | Elements not common in both sets            |
