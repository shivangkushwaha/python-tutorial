# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print("a:- ",a)



# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print("a:- ",a)

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print("a[1]",a[1])


# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# The len() function returns the length of a string:
a = "Hello, World!"
print("a length:- ",len(a))

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
