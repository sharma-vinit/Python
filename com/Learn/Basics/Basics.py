'''
Basics of Python 3
@author: Vinit.Sharma
'''
import this

# Check the Python Version
import sys
print(sys.version)

'''
    Print function:    simply outputs its parameters to the terminal. 
    By default, print appends a newline character to its output, which simply moves the cursor to the next line. 
    In Python 2.x, print is a statement rather than a function. 
'''

print("Hello World!")       # Hello, World! In Python 3
print('Hello World!')       # Hello, World! In Python 3
print("""Hello World!""")   # Hello, World! In Python 3

# You can also put the below line to pause the program at the end until you press anything. 
input('Press some key to proceed further...')

# Single Line Comment

'''
This is a multiline
comment.
'''

# Indentation
x = 1
if x == 1:
    # Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported,
    # but the standard indentation requires standard Python code to use four spaces. 
    # Spaces and tabs don't mix, so use only one or the other when indenting your programs. 
    print("x is 1.")

'''
    Variables and Types
    A variable is something that holds a value that may change. Python is completely object oriented, and not "statically typed". 
    You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.
    All variables are case-sensitive. 
'''
# We can also change what is inside a variable, by assigning different values to it. 
# We can also assign the value of a variable to be the value of another variable.
red = 5
blue = 10
print (red, blue)   # Prints 5 10

yellow = red
print (yellow, red, blue)   # Prints 5 5 10

red = blue
print (yellow, red, blue)   # Prints 5 10 10
