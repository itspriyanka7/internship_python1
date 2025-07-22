
# 🧵 Python `string` – Use and Methods

## 🔹 What is a String?
A **string** in Python is a sequence of characters enclosed in single quotes `' '`, double quotes `" "`, or triple quotes `''' '''` / `""" """`.

Strings are:
- Ordered
- Immutable (cannot be changed after creation)
- Iterable

---

## 🔹 String Use (Applications)

- ✅ Store and display text
- ✅ User input/output handling
- ✅ Parsing and manipulating text data
- ✅ Working with file names, paths, logs
- ✅ Data formatting and templating

---

## 🔹 Common String Methods

| **Method**         | **Description**                                      |
|--------------------|------------------------------------------------------|
| `upper()`          | Converts all characters to uppercase                 |
| `lower()`          | Converts all characters to lowercase                 |
| `capitalize()`     | Capitalizes the first character                      |
| `title()`          | Capitalizes the first character of each word         |
| `strip()`          | Removes leading/trailing whitespace                  |
| `replace(old, new)`| Replaces all occurrences of a substring              |
| `find(sub)`        | Returns the first index of the substring             |
| `split(sep)`       | Splits string into list using a separator            |
| `join(list)`       | Joins elements of a list into a single string        |
| `startswith(sub)`  | Checks if string starts with a given substring       |
| `endswith(sub)`    | Checks if string ends with a given substring         |

---

## 🔹 String Indexing & Slicing

- Indexing: `s[0]` gives first character
- Negative Indexing: `s[-1]` gives last character
- Slicing: `s[start:end]` returns a substring

---

## 🔹 String Formatting

- f-strings: `f"Hello, {name}!"`
- `format()`: `"Hello, {}".format(name)`
- `%`: `"Hello, %s" % name`

