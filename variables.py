print("To create variable, first assing a value to it")

a = 2022481031
b = "Efe"
print(a)
print(b)

print("Variables don't need to be declared with any particular type.")

c = 195       # c is of type int
c = "Can"     # c is now of type str
print(c)

print("With casting, we can specify data type of a variable.")

d = str(1)    # d will be '1'
e = int(1)    # e will be 1
f = float(1)  # f will be 1.0

print("We can learn data type of variable with 'type()' function.")

g = 3133
h = "Kara"
print(type(g))
print(type(h))

print("String variables can be declared either with single or double quotes.")

# Two values are the same.
i = "karsterr"
i = 'karsterr'

print("Variables are case-sensitive.")

# J won't overwrite j value.
j = 30
J = "Kono Dio da!"

print("A variable can have short or descriptive name.")

k = "Ayşe"
isim = "Fatma"

print("There are some rules for Python variables.")

print("1 - Must start with a letter or underscore(_)")

var1 = 1
_var2 = 2

print("2 - Can't start with a number")

# 2 = "Hello World!"
print("Commented variable assinging gives us a SyntaxError.")

print("3 - Only contains alpha-numeric characters and underscores (A-z, 0-9, and _ )")

print("4 - Variable names are case-sensitive")

age = 19
Age = 19
AGE = 19

print("This variables can't be used as a variable")

'''
2myvar = 'White'
my-var = 'Black'
my var = 'Grey'
'''

print("There are several techniques you can use to make them more readable.")

camelCaseVariable = "Camel Case Variable"
PascalCaseVariable = "Pascal Case Variable"
snake_case_variable = "Snake Case Variable"

print("Python allows us to assing values to multiple variables in one line.")

l, m, n = "Orange", "Banana", "Cherry"
print(l)
print(m)
print(n)

print("We cans assing the same value to multiple variables")

o = p = q = "Apple"
print(o)
print(p)
print(q)

print("If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.")

myName = ["Efe", "Can", "Kara"]
firstName, secondName, surname = myName
print(firstName)
print(secondName)
print(surname)

print("print() function is used to output variables.")

r = "I'm awesome!"
print(r)

print("Can output multiple variables with seperated by a comma.")
s = 1
t = 2
u = 3
print(s, t, u)

print("Use the + operator to output multiple variables")
w = "Python"
v = " Cheat"
y = "sheet"
z = "."
print(w + v + y + z)

print("Global variables can be used by everyone, both inside of functions and outside.")

name = "Efe Can Kara"
def pmn():
    print("My name is " + name)

pmn()

print("If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.")

name = "Efe Can Kara"
def printMyName():
    name = "John Doe"
    print("My name is " + name)

printMyName()
print(name)

print("To create a global variable inside a function, you can use the global keyword.")

def globalVariable():
  global x
  x = "fantastic"
  print(x)

globalVariable()
print("Python is " + x)

print("Also, use the global keyword if you want to change a global variable inside a function.")

x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
