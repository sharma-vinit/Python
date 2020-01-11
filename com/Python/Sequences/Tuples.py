'''
    Tuples
    Tuples are similar to lists, except they are immutable. 
    Once you have set a tuple, there is no way to change it whatsoever: you cannot add, change, or remove elements of a tuple. 
    Otherwise, tuples work identically to lists. 
    A tuple of hashable objects is hashable and thus suitable as a key in a dictionary and as a member of a set. 
'''

# To declare a tuple, you use commas (with or without parentheses, but generally tuples are enclosed in parentheses. ):
immutable = "Hello", 0, "World", "!"
print(type(immutable))

immutable_with_parentheses = ("Hello", 0, "World", "!")
print(type(immutable_with_parentheses))
# One-element tuples can be entered by surrounding the entry with parentheses and adding a comma like:        
singleton_tuple = ('this is a singleton tuple',) 

#Multiple assignments, could be done on same line like:
list1, list2 = ("Hello", " "), ("World", "!")
# Above declaration is equivalent to:
list1 = "Hello", " "
list2 = "World", "!"

print(list1, type(list1))   # Prints: ('Hello', ' ') <class 'tuple'>
print(list2, type(list2))   # Prints: ('World', '!') <class 'tuple'>

# Addition or, combine tuples
list3 = list1 + list2
print(list3)                # Prints: ('Hello', ' ', 'World', '!')

# It is often necessary to use parentheses to differentiate between different tuples, such as when doing multiple assignments on the same line:
'''
immutable, list = "Hello", 0, "World", "!"  # 4 elements here
Above statement throws ValueError: too many values to unpack (expected 2)
'''
immutable, list = ("Hello", 0), ("World", "!")  # 2 elements here, each element is a tuple
print(immutable)    # Prints: ('Hello', 0)
print(list)         # Prints: ("World", "!")

# Packing and Unpacking
message_hello = "Hello"
message_world = ("World", "!")
t = message_hello, message_world    # Tuple packing
list1, list2 =  t           # is called "tuple unpacking" because the tuple t was unpacked and its values assigned to each of the variables on the left.
                            # When unpacking a tuple, or performing multiple assignment, you must have the same number of variables being assigned to as values being assigned. 
print(list1, type(list1))
print(list2, type(list2))

# Unnecessary parentheses can be used without harm, but nested parentheses denote nested tuples:
immutable = ("Hello", 0, "World", "!" ) # 4 elements here
immutable = ("Hello", 0, ("World", "!" )) # 3 elements here, 3rd element is itself a tuple

# Tuples may be created directly or converted from lists
l = [1, 'a', [6, 3.14]]
t = tuple(l)            # Convert list to tuples using the built in tuple() method.
some_list = list(t)     # Converting a tuple into a list using the built in list() method to cast as a list
print(t == tuple(l))    # Prints: True
print(t == l)           # Prints: False

# Dictionaries can also be converted to tuples of tuples using the items method of dictionaries: 
d = {'a': 1, 'b': 2}
print(type(tuple(d.items())))


#    Tuples in Python at a glance:

tup1  = (1, 'a')
tup2  = 1, 'a'                # Brackets not needed
tup3  = (1,)                  # Singleton
tup4  = 1,                    # Singleton without brackets
tup5 = ()                     # Empty tuple
list1 = [1, 'a']
it1, it2 = tup1               # Assign items
print(tup1 == tup2)           # True
print(tup1 == list1)          # False
print(tup1 == tuple(list1))   # True
print(list(tup1) == list1)    # True
print(tup1[0])                # First member
for item in tup1: 
    print(item)               # Iteration
print((1, 2) + (3, 4))        # (1, 2, 3, 4)
tup1 += (3,)
print(tup1)                   # (1, 'a', 3), despite immutability
print(len(tup1))              # Length AKA size AKA item count
print(3 in tup1)              # Membership - true
# return r1, r2                 # Return multiple values
# r1, r2 = myfun()              # Receive multiple values
tup6 = ([1,2],)
tup6[0][0]=3
print(tup6)                   # The list within is mutable
set1 = set( (1,2) )           # Can be placed into a set
#set1 = set( ([1,2], 2) )     # Error: The list within makes it unhashable

# Operations on tuples
#    These are the same as for lists except that we may not assign to indices or slices, and there is no "append" operator.



# Uses of Tuples
'''
    Tuples can be used in place of lists where the number of items is known and small, for example when returning multiple values from a function. 
    Many other languages require creating an object or container to return, but with Python's tuple assignment, multiple-value returns are easy:
'''
def func(x, y):
    # code to compute x and y
    return x, y

#    This resulting tuple can be easily unpacked with the tuple assignment technique explained above:

x, y = func(1, 2)


# Using List Comprehension to process Tuple elements
'''
    Occasionally, there is a need to manipulate the values contained within a tuple in order to create a new tuple. 
    For example, if we wanted a way to double all of the values within a tuple, we can combine some of the above information in addition to list comprehension like this:
'''
def double(T):
    'double() - return a tuple with each tuple element (e) doubled.'
    return tuple( [ e * 2 for e in T ] )

print(double((4, 5, 6)))