# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "female"]
print(list1)


# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Task 1:  Remove Duplicates from a List

# def remove_duplicates(lst):
#     return list(dict.fromkeys(lst))

# print(remove_duplicates([1, 2, 2, 3, 1]))

# # Task 2: Merge and Sort Two Lists

# def merge_sort_unique(a, b):
#     return sorted(set(a + b))

# print(merge_sort_unique([4, 2, 7], [5, 2, 6]))  # Output: [2, 4, 5, 6, 7]
