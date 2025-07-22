# 🐍 Python Operators

Python operators are special symbols used to perform operations on variables and values.

---

## 1. Arithmetic Operators
Used to perform mathematical operations.

| Operator | Meaning        | Example  | Result |
|----------|----------------|----------|--------|
| `+`      | Addition        | 5 + 2    | 7      |
| `-`      | Subtraction     | 5 - 2    | 3      |
| `*`      | Multiplication  | 5 * 2    | 10     |
| `/`      | Division        | 5 / 2    | 2.5    |
| `//`     | Floor Division  | 5 // 2   | 2      |
| `%`      | Modulus         | 5 % 2    | 1      |
| `**`     | Exponentiation  | 2 ** 3   | 8      |

---

## 2. Comparison Operators
Compare two values and return True or False.

| Operator | Meaning              | Example   | Result |
|----------|----------------------|-----------|--------|
| `==`     | Equal to             | 5 == 5    | True   |
| `!=`     | Not equal to         | 5 != 3    | True   |
| `>`      | Greater than         | 5 > 3     | True   |
| `<`      | Less than            | 5 < 3     | False  |
| `>=`     | Greater or equal to  | 5 >= 5    | True   |
| `<=`     | Less or equal to     | 3 <= 5    | True   |

---

## 3. Logical Operators
Used to combine conditional statements.

| Operator | Meaning                | Example            | Result |
|----------|------------------------|--------------------|--------|
| `and`    | True if both are true  | True and False     | False  |
| `or`     | True if one is true    | True or False      | True   |
| `not`    | Reverses the result    | not True           | False  |

---

## 4. Assignment Operators
Used to assign values to variables.

| Operator | Meaning         | Example   | Same as     |
|----------|------------------|-----------|-------------|
| `=`      | Assign           | x = 5     | —           |
| `+=`     | Add and assign   | x += 3    | x = x + 3   |
| `-=`     | Subtract         | x -= 3    | x = x - 3   |
| `*=`     | Multiply         | x *= 2    | x = x * 2   |
| `/=`     | Divide           | x /= 2    | x = x / 2   |
| `**=`    | Power            | x **= 2   | x = x ** 2  |

---

## 5. Bitwise Operators
Used to perform bit-level operations.

| Operator | Meaning    | Example   | Result |
|----------|------------|-----------|--------|
| `&`      | AND        | 5 & 3     | 1      |
| `|`      | OR         | 5 | 3     | 7      |
| `^`      | XOR        | 5 ^ 3     | 6      |
| `~`      | NOT        | ~5        | -6     |
| `<<`     | Left Shift | 5 << 1    | 10     |
| `>>`     | Right Shift| 5 >> 1    | 2      |

---

## 6. Identity Operators
Check if two variables point to the same object in memory.

| Operator | Meaning               | Example     | Result |
|----------|------------------------|-------------|--------|
| `is`     | Same object            | x is y      | True   |
| `is not` | Different objects      | x is not y  | True   |

---

## 7. Membership Operators
Check if a value exists in a sequence (list, tuple, string).

| Operator | Meaning           | Example          | Result |
|----------|-------------------|------------------|--------|
| `in`     | Value exists      | 3 in [1,2,3]     | True   |
| `not in` | Value doesn't exist| 4 not in [1,2]  | True   |


---

## 📘 More Information on Each Operator

### 1. Arithmetic Operators
These are used for performing basic mathematical operations. They work on numbers (int, float).

- `+`: Adds two values.
- `-`: Subtracts the second value from the first.
- `*`: Multiplies two values.
- `/`: Divides the first by the second (returns float).
- `//`: Performs floor division (returns integer).
- `%`: Returns the remainder.
- `**`: Raises to the power.

---

### 2. Comparison Operators
Used to compare values. Returns a boolean (`True` or `False`).

- `==`: True if values are equal.
- `!=`: True if values are not equal.
- `>`: True if left is greater than right.
- `<`: True if left is less than right.
- `>=`: True if left is greater or equal.
- `<=`: True if left is less or equal.

---

### 3. Logical Operators
Combines conditional expressions.

- `and`: Returns True if both conditions are true.
- `or`: Returns True if at least one is true.
- `not`: Inverts the boolean value.

---

### 4. Assignment Operators
Used to update the value of a variable.

- `=`: Assign value.
- `+=`: Add and assign.
- `-=`: Subtract and assign.
- `*=`: Multiply and assign.
- `/=`: Divide and assign.
- `**=`: Power and assign.

---

### 5. Bitwise Operators
Operate on binary (bit) values.

- `&`: Binary AND.
- `|`: Binary OR.
- `^`: Binary XOR.
- `~`: Binary NOT (inverts bits).
- `<<`: Shifts bits left.
- `>>`: Shifts bits right.

---

### 6. Identity Operators
Check memory address of objects (object identity).

- `is`: Returns True if variables refer to the same object.
- `is not`: Returns True if they do not refer to the same object.

---

### 7. Membership Operators
Used to test membership in sequences like list, tuple, string.

- `in`: True if value exists in the sequence.
- `not in`: True if value does not exist.

