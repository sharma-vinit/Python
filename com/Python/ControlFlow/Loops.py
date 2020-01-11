#    Control flow in Python at a glance:

x = -6                              # Branching
if x > 0:                           # If
    print("Positive")
elif x == 0:                        # Else if AKA elseif
    print("Zero")
else:                               # Else
    print("Negative")
list1 = [100, 200, 300]
for i in list1: print(i)             # A for loop
for i in range(0, 5):
    print(i)                         # A for loop from 0 to 4
for i in range(5, 0, -1):
    print(i)                         # A for loop from 5 to 1
for i in range(0, 5, 2):
    print(i)                         # A for loop from 0 to 4, step 2
list2 = [(1, 1), (2, 4), (3, 9)]
for x, xsq in list2: 
    print(x, xsq)                    # A for loop with a two-tuple as its iterator
l1 = [1, 2]; l2 = ['a', 'b']
for i1, i2 in zip(l1, l2):
    print(i1, i2)                    # A for loop iterating two lists at once.
i = 5
while i > 0:                         # A while loop
    i -= 1
list1 = ["cat", "dog", "mouse"]
i = -1 # -1 if not found
for item in list1:
    i += 1
    if item=="dog":
        break                           # Break; also usable with while loop
print("Index of dog:",i)             
for i in range(1,6):
    if i <= 4:
        continue                        # Continue; also usable with while loop
    print("Greater than 4:", i)




# In Python, there are two kinds of loops, 'for' loops and 'while' loops. 

# For loops
# A for loop iterates over elements of a sequence (tuple or list). A variable is created to represent the object in the sequence. For example,

x = [100,200,300]
for i in x:
    print (i)   #these parenthesis are needed for the code to get executed in higher versions of Python


'''
Prints: 
    100
    200
    300
'''
    
'''
The for loop loops over each of the elements of a list or iterator, assigning the current element to the variable name given. 
In the example above, each of the elements in x is assigned to i.
'''
# A built-in function called range exists to make creating sequential lists such as the one above easier. The loop above is equivalent to: 
l = range(100, 301,100)
for i in l:
    print (i)
    

# The range() Function
#    If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:
#    The given end point is never part of the generated sequence; range(10) generates 10 values, the legal indices for items of a sequence of length 10.
print(range(10))    # Prints: range(0, 10)

# The next example uses a negative step (the third argument for the built-in range function):

for i in range(5, 0, -1):
    print (i)
    
'''
Prints:
    5
    4
    3
    2
    1
'''
    
#    The negative step can be -2:

for i in range(10, 0, -2):
    print (i)
'''
Prints:
    10
    8
    6
    4
    2
'''

# For loops can have names for each element of a tuple, if it loops over a sequence of tuples:

l = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
for x, xsquared in l:
    print(x, ':', xsquared)

'''
Prints:
    1 : 1
    2 : 4
    3 : 9
    4 : 16
    5 : 25
'''

# range Versus xrange
'''
Above, you were introduced to the range function, which returns a list of all the integers in a specified range. 
Supposing you were to write an expression like range(0, 1000000): that would construct a list consisting of a million integers! That can take up a lot of memory.
Often, you do indeed need to process all the numbers over a very wide range. But you might only need to do so one at a time; as each number is processed, it can be discarded from memory before the next one is obtained.
To do this, you can use the xrange function instead of range. For example, the following simple loop
'''
for i in xrange(0, 1000000) :
    print(i)
#end for
'''
will print the million integers from 0 to 999999, but it will get them one at a time from the xrange call, instead of getting them all at once as a single list and going through that.

This is an example of an iterator, which yields values one at a time as they are needed, rather than all at once. As you learn more about Python, you will see a lot more examples of iterators in use, and you will learn how to write your own.
Note:     

Python 3 Note: In Python 3.x, there is no function named xrange. Instead, the range function has the behaviour described above for xrange.     
'''    
    
# While loops
#    A while loop repeats a sequence of statements until some condition becomes false. For example:
x = 5
while x > 0:
    print (x)  #all the print statement must be in parenthesis for version 3.4.0
    x = x - 1  #the algebra need not be done within the parenthesis
    
# Breaking and continuing
#    Python includes statements to exit a loop (either a for loop or a while loop) prematurely. To exit a loop, use the break statement:

x = 5
while x > 0:
    print(x)
    break
    x -= 1
    print(x)
    
# Python's while loops can also have an 'else' clause, which is a block of statements that is executed (once) when the while statement evaluates to false. The break statement inside the while loop will not direct the program flow to the else clause. For example:
x = 5
y = x
while y > 0:
    print (y)
    y = y - 1
else:
    print (x)

    
# The statement to begin the next iteration of the loop without waiting for the end of the current loop is 'continue'. 
l = [5,6,7]
for x in l:
    continue
    print(x)
    

# Else clause of loops
# The else clause of loops will be executed if no break statements are met in the loop.

l = range(1,100)
for x in l:
    if x == 100:
        print(x)
        break
    else:
        print(x," is not 100")
else:
    print("100 not found in range")
    

# You can also add "elif" (short for "else if") branches onto the if statement. 
# If the predicate on the first “if” is false, it will test the predicate on the first elif, and run that branch if it’s true. If the first elif is false, it tries the second one, and so on. Note, however, that it will stop checking branches as soon as it finds a true predicate, and skip the rest of the if statement. You can also end your if statements with an "else" branch. If none of the other branches are executed, then python will run this branch.

x = -6
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
    
    
