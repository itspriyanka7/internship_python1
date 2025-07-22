# # Sets are used to store multiple items in a single variable.

# # A set is a collection which is unordered, unchangeable*, and unindexed.
# # Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# # Sets are written with curly brackets.

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# # Check if "banana" is present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset)

# # Add an item to a set, using the add() method:
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)

# # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)


# Assignment 1: Basic Set Operations

# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference (set1 - set2)
difference_set = set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)

# Subset check
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# Modify sets
set1.add(9)
set2.discard(8)  # discard() is safe even if the element doesn't exist

# Print final modified sets
print("Modified set1:", set1)
print("Modified set2:", set2)


# Assignment 2: FrozenSet Operations

# Create frozen sets
A = frozenset([10, 20, 30, 40])
B = frozenset([30, 40, 50, 60])

# Perform operations
print("Union of A and B:", A.union(B))
print("Common elements (Intersection):", A.intersection(B))
print("Only in A (Difference):", A.difference(B))
print("Not common in both (Symmetric Difference):", A.symmetric_difference(B))

# Check if A is a superset of {10, 20}
print("Is A a superset of {10, 20}?", A.issuperset({10, 20}))

# Try to add (will cause error because frozen sets can't be changed)
try:
    A.add(70)
except AttributeError:
    print("❌ Cannot add to frozenset – it is immutable")

# Print lengths
print("Number of items in A:", len(A))
print("Number of items in B:", len(B))
