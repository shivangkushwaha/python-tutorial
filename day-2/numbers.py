# Let's see numbers examples and types of numbers 
x = 1
y = 2.8
z = 1j

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Intgers numbers and how we define int
x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Floating Points numbers and how we define int

x = 1.10
y = 1.0
z = -35.59

print(x, type(x))
print(y, type(y))
print(z, type(z))


# scientific numbers with an "e" to indicate the power of 10

x = 35e3
y = 12E4
z = -87.7e100

print(x, type(x))
print(y, type(y))
print(z, type(z))


# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j
print(x, type(x))
print(y, type(y))
print(z, type(z))


# Let's take a look to type conversion 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Let's see random number 
import random

print(random.randrange(1, 10))