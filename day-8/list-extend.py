# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# The condition is like a filter that only accepts the items that valuate to True.
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# The condition is optional and can be omitted:
newlist = [x for x in fruits]
print(newlist)


# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)


# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)








