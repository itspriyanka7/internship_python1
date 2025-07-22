# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.


thistuple = ("apple", "banana", "cherry")
print(thistuple)

# To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



#Other All Methods Same as list

# #✅ Assignment 4: Basic Tuple Operations

# # Create a tuple of student names
# students = ("John", "Emma", "Alice", "David", "Nina")

# # Print the second student's name (index 1)
# print("Second student:", students[1])

# # Check if "Alice" is in the tuple
# print("Is 'Alice' in the list?", "Alice" in students)

# # Concatenate with another tuple of new students
# new_students = ("Sara", "Mike", "Leo")
# all_students = students + new_students

# # Print the length of the final tuple
# print("Total students:", len(all_students))

# # ✅ Assignment 5: Tuple Unpacking & Conversion

# # Tuple with product details
# product_info = ("Laptop", 50000, 2)

# # Unpack the tuple
# product, price, quantity = product_info

# # Calculate total cost
# total = price * quantity
# print(f"Total cost of {product}: ₹{total}")

# # Convert to list to modify quantity
# product_list = list(product_info)
# product_list[2] = 3  # change quantity to 3

# # Convert back to tuple and print
# product_info = tuple(product_list)
# print("Updated product info:", product_info)

# # ✅ Assignment 6: Dictionary Program

# # Store students and their grades
# grades = {
#     "Alice": 88,
#     "Bob": 92,
#     "Clara": 79,
#     "David": 95
# }

# # Add a new student
# grades["Eva"] = 85

# # Find average grade
# average = sum(grades.values()) / len(grades)
# print("Average Grade:", average)

# # Identify top performer
# top_student = max(grades, key=grades.get)
# print("Top Performer:", top_student, "-", grades[top_student])

# # ✅ Assignment 7: Array (List) Program

# # Store daily temperatures
# temps = [32, 35, 30, 31, 36, 33, 34]

# # Hottest and coldest day
# print("Hottest temperature:", max(temps))
# print("Coldest temperature:", min(temps))

# # Calculate average temperature
# avg_temp = sum(temps) / len(temps)

# # Days above average
# above_avg = [t for t in temps if t > avg_temp]
# print("Days above average:", above_avg)

# # List slicing examples
# print("First 3 days:", temps[:3])
# print("Last 2 days:", temps[-2:])
