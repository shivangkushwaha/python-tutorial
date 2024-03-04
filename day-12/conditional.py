"""
Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

"""
a = 33
b = 200
if b > a:
  print(f"{b} is greater than {a}")


a = 33
b = 33
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
  print(f"{a} and {b} are equal")


a = 200
b = 33
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
  print(f"{a} and {b} are equal")
else:
  print(f"{a} is greater than {b}")
  
  
a = 200
b = 33
if b > a:
  print(f"{b} is greater than {a}")
else:
  print(f"{b} is not greater than {a}")
  
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
a = 33
b = 200

if b > a:
  pass