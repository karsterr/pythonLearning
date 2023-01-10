print("You can display a string literal with the print() function")

print("Hello")
print('Hello')

print("Assigning a string to a variable is done with the variable name followed by an equal sign and the string")

x = "Efe"
print(x)

print("We can assign a multiline string to a variable by using three quotes or single quotes.")

x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)

y = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(y)

print("Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.")
print("Square brackets can be used to access elements of the string.")

x = "Hello, World!"
print(x[1])

print("Since strings are arrays, we can loop through the characters in a string, with a for loop.")

for x in "banana":
  print(x)

print("To get the length of a string, use the len() function.")

x = "karsterr"
print(len(x))

print("To check if a certain phrase or character is present in a string, we can use the keyword in.")

example = "Your soul is mine!"
print("soul" in example)

print("To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.")

txt = "The best things in life are free!"
print("expensive" not in txt)

print("You can return a range of characters by using the slice syntax.")
print("Specify the start index and the end index, separated by a colon, to return a part of the string.")

print("By leaving out the start index, the range will start at the first character")

x = "Hello, World!"
print(x[:5])

print("By leaving out the end index, the range will go to the end.")

print(x[2:])

print("Use negative indexes to start the slice from the end of the string.")

print(x[-5:-2])

print("The upper() method returns the string in upper case.")

print(x.upper())

print("The lower() method returns the string in lower case.")

print(x.lower())

print("Whitespace is the space before and/or after the actual text, and very often you want to remove this space.")

x = " Hello World! "

print(x.strip())

print("The replace() method replaces a string with another string")

print(x.replace("H", "J"))

print("The split() method splits the string into substrings if it finds instances of the separator")

print(x.split(","))