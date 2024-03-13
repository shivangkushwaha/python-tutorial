# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

cars = ["Ford", "Volvo", "BMW"]
"""An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
Access the Elements of an Array
You refer to an array element by referring to the index number.
"""
x = cars[0]

# Modify the value of the first array item:
cars[0] = "Toyota"

# Use the len() method to return the length of an array (the number of elements in an array).
x = len(cars)


# You can use the for in loop to loop through all the elements of an array.
for x in cars:
  print(x)

# You can use the append() method to add an element to an array.
cars.append("Honda")

# You can use the append() method to add an element to an array.
cars.pop(1)

# You can also use the remove() method to remove an element from the array.
cars.remove("Volvo")


"""
Python has a set of built-in methods that you can use on lists/arrays.

    Method	Description
    append()	Adds an element at the end of the list
    clear()	Removes all the elements from the list
    copy()	Returns a copy of the list
    count()	Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	Removes the element at the specified position
    remove()	Removes the first item with the specified value
    reverse()	Reverses the order of the list
    sort()	Sorts the list
"""





