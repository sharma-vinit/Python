'''
    Strings
    A 'string' is simply a list of characters in order. 
    A character is anything you can type on the keyboard in one keystroke, like a letter, a number, space, or a backslash. 
    There are no limits to the number of characters you can have in a string, you can have anywhere from one to a million or more. 
    You can even have a string that has 0 characters, which is usually called "the empty string."
'''

'''
    There are three ways you can declare a string in Python: 
    1.    single quotes ('), 
    2.    double quotes ("), and 
    3.    triple quotes (""")
'''
# In all cases, you start and end the string with your chosen string declaration. For example:

print('I am a single quoted string')       # Prints    I am a single quoted string
print("I am a double quoted string")       # Prints    I am a double quoted string
print("""I am a triple quoted string""")   # Prints    I am a triple quoted string

'''
    You can use quotation marks within strings by placing a backslash ("\") directly before them, 
    so that Python knows you want to include the quotation marks in the string, instead of ending the string there. 
    Placing a backslash directly before another symbol like this is known as escaping the symbol. 
'''
print("So I said, \"You don't know me! You'll never understand me!\"")      # Prints:    So I said, "You don't know me! You'll never understand me!"
print('So I said, "You don\'t know me! You\'ll never understand me!"')      # Prints:    So I said, "You don't know me! You'll never understand me!"
print("This will result in only three backslashes: \\ \\ \\")               # Prints:    This will result in only three backslashes: \ \ \
print("""The double quotation mark (\") is used to indicate direct quotations.""")  # Prints:    The double quotation mark (") is used to indicate direct quotations.


# Concatenation:    You can also add two strings together using the + operator: this is called concatenating them.
print("Hello, " + "World!") # Prints: Hello, World!

# input() function
answer = input()
# You should use "input()" in python 3.x, because python 3.x doesn't have a function named "raw_input()".
# input() function reads a line from sys.stdin and returns it without the trailing newline. To get the old behavior of input(), use eval(input()).
# "raw_input()" was used in python 2.x
print(answer)
print(type(answer))     # Prints: <class 'str'>

# Cast input received from input() to appropriate data type before performing operations
response = input()
number = int(response)  # casting response to int data type
plusTen = number + 10
print ("If we add 10 to your number, we get " + str(plusTen))   # casting response to string data type

# String Formatting:
# Another way of doing the same is to add a comma after the string part and then the number variable, like this: 
print ("If we add 10 to your number, we get ", plusTen)
# or use special print formatting like this: 
print ("If we add 10 to your number, we get %s" % plusTen)
# which alternative can be written this way, if you have multiple inputs: 
plusTwenty = number + 20
print ("If we add 10 and 20 to your number, we get %s and %s" % (plusTen, plusTwenty))
# or use format() 
print ("If we add 10 to your number, we get {0}".format(plusTen))

# Strings in Python at a glance:
str1 = "Hello"                 # A new string using double quotes
str2 = 'Hello'                 # Single quotes do the same
str3 = "Hello\tworld\n"        # One with a tab and a newline
str4 = str1 + " world"         # Concatenation
str5 = str1 + str(4)           # Concatenation with a number
str6 = str1[2]                 # 3rd character
str6a = str1[-1]               # Last character
#str1[0] = "M"                 # No way; strings are immutable
for char in str1: print(char)  # For each character
str7 = str1[1:]                # Without the 1st character
str8 = str1[:-1]               # Without the last character
str9 = str1[1:4]               # Substring: 2nd to 4th character
str10 = str1 * 3               # Repetition
str11 = str1.lower()           # Lowercase
str12 = str1.upper()           # Uppercase
str13 = str1.rstrip()          # Strip right (trailing) whitespace
str14 = str1.replace('l','h')  # Replacement
list15 = str1.split('l')       # Splitting
if str1 == str2: print("Equ")  # Equality test
if "el" in str1: print("In")   # Substring test
length = len(str1)             # Length
pos1 = str1.find('llo')        # Index of substring or -1
pos2 = str1.rfind('l')         # Index of substring, from the right
count = str1.count('l')        # Number of occurrences of a substring

# String operations
# Equality
# Two strings are equal if they have exactly the same contents, meaning that they are both the same length and each character has a one-to-one positional correspondence.
# Python uses the is operator to test the identity of strings and any two objects in general.
a = 'hello'; b = 'hello'        # Assign 'hello' to a and b.
print(a == b)                   # check for equality, Prints: True
print(a == 'hello')             # Prints: True
print(a == "hello")             # (choice of delimiter is unimportant), Prints: True
print(a == 'hello ')            # (extra space) Prints: False
print(a == 'Hello')             # (wrong case) Prints: False

print(a is b)                   # a is identical to b, Prints: True

# Numerical
'''
There are two quasi-numerical operations which can be done on strings -- addition and multiplication. 
    String addition is just another name for concatenation. 
    String multiplication is repetitive addition, or concatenation. 
'''
c = 'a'
print(c + 'b')  # Prints: 'ab'
print(c * 5)    # Prints: 'aaaaa', a is repeated 5 times

# Containment
x = 'hello'
y = 'ell'
print(x in y)  # Prints: False
print(y in x)  # Prints: True

# Indexing and Slicing
s = "Python"
print(s[1]) # Prints: y
print(s[-1])        # Last Character of String         Prints: n
print(s[-len(s)])   # First Character of String        Prints: P
# print(s[-len(s)-1]) # IndexError: string index out of range

print ("Hello, world!"[-1], "Hello, world!"[-13])   # Prints: ! H

# s[a:b] will give us a string starting with s[a] and ending with s[b-1], where a is starting index and b is last index.
s = "Python"  
print(len(s))       # Prints: 6

# String:   P  y  t  h  o  n
# Index:    0  1  2  3  4  5
#          -6 -5 -4 -3 -2 -1

print(s[0: len(s)])   # Prints: Python    means we take everything in between index 0, and end at index 5
print(s[0:])          # Prints: Python
print(s[:2])          # Prints: Py
print(s[:])           # Prints: Python
print(s[0: 5])        # Prints: Pytho   # Note also that the brackets are inclusive on the left but exclusive on the right
print(s[-4:-1])       # Prints: tho, We can also use negative numbers in slices

# It is also possible to get non-continuous parts of an String. 
# If one wanted to get every n-th occurrence of a list, one would use the : : operator. 
# The syntax is a : b : n where a and b are the start and end of the slice to be operated upon.
print(s[::2])   # Prints: Pto
print(s[:4:2])  # Prints: Pt


# String methods: https://en.wikibooks.org/wiki/Python_Programming/Strings#String_methods

# escape sequences
print(r"Hello \ World!")    # Prints: Hello \ World!    Notice the r in from of String, r will tell Python that string will be displayed as raw string
