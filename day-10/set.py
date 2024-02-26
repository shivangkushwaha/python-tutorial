"""_summary_
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
"""
thisset = {"apple", "banana", "cherry"}
print("This is a set example", thisset)

# Duplicates Not Allowed
# Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print("This is a set example", thisset)


# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print("This is a set example", thisset)

# False and 0 is considered the same value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print("This is a set example", thisset)


"""_summary_
Access Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


# Change Items
# Once a set is created, you cannot change its items, but you can add new items.




