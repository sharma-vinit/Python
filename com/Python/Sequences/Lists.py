'''
    Lists
    A list in Python is an ordered group of items (or elements). 
    It is a very general structure, and list elements don't have to be of the same type: you can put numbers, letters, strings and nested lists all on the same list.
    Unlike, tuples Lists are mutable
'''

# A list is created using square brackets. For example, an empty list would be initialized like this:
myList = []

# The values of the list are separated by commas. For example:
myList = ["bacon", "eggs", 42]

# Like characters in a string, items in a list can be accessed by indexes starting at 0. 
# To access a specific item in a list, you refer to it by the name of the list, followed by the item's number in the list inside brackets.

myList = ["bacon", "eggs", 42]
print(myList)                               # Prints: ['bacon', 'eggs', 42]
print(myList[0], myList[1], myList[2])      # Prints: bacon eggs 42

# You can also use negative numbers, which count backwards from the end of the list:
print(myList[-3], myList[-2], myList[-1])      # Prints: bacon eggs 42

# Length of list:    The len() function also works on lists, returning the number of items in the array.
print(len(myList))      # Prints: 3

# Slicing
# As with strings, lists may be sliced
print(myList[1:])      # Prints: ['eggs', 42]
print(myList[:-1])      # Prints: ['bacon', 'eggs']

# It is also possible to add items to a list. There are many ways to do it, the easiest way is to use the append() method of list:
myList.append([100, 101])   # adds only one element, at the end of the list. So if the intention was to concatenate two lists, always use extend. 
#    myList[4] = -1     # Note that you cannot manually insert an element by specifying the index outside of its range.
print(myList)      # Prints: ['bacon', 'eggs', 42, [100, 101]]

# It's even possible to append items onto the start of lists by assigning to an empty slice: 
myList[:0] = ['at', 'start']
print(myList)      # Prints: ['at', 'start', 'bacon', 'eggs', 42, [100, 101]]

# We could also use extend() 
myList.extend([-1, -2])     # Adds 2 elements, unlike append()
print(myList)      # Prints: ['at', 'start', 'bacon', 'eggs', 42, [100, 101], -1, -2]

# You can also delete items from a list using the del statement
print("Undo all ...")
del myList[0]
del myList[0]
del myList[3]
del myList[3]
del myList[3]
print(myList)      # Prints: ['bacon', 'eggs', 42]

# With slicing you can create copy of list since slice returns a new list:
print('Copying elements into new List: ') 
myList.append([])
list_copy = myList[:]
print(list_copy)      # Prints: ['bacon', 'eggs', 42, []]

# Note, however, that this is a shallow copy and contains references to elements from the original list, so be careful with mutable types: 
print('Replacing content at index 2 in list_copy')
list_copy[3].append('something')
print(myList)      # Prints: ['bacon', 'eggs', 42, ['something']]

del myList[3]       # deletes element at index 3, leaving myList = ['bacon', 'eggs', 42]
print(myList)       # ['bacon', 'eggs', 42]    
print(list_copy)    # ['bacon', 'eggs', 42, ['something']]    myList (original list has been modified but it's copy (list_copy) still retains ['something']

# If you want to insert an item inside a list at a certain index, you may use the insert() method of list
myList.insert(1, 'and') # This inserts 'and' at index one (i.e. after 'bacon')                   
print(myList)      # Prints: ['bacon', 'and', 'eggs', 42]

# Combine Lists (besides append() and extend())
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)    # Prints: [1, 2, 3, 4, 5, 6]

# As you can see, the list re-orders itself, so there are no gaps in the numbering. 
# Lists have an unusual characteristic. Given two lists a and b, if you set b to a, and change a, b will also be changed. 
a=[2, 3, 4, 5]
b=a             # set b to a    Now, a and b both references the same list 
del a[3]        # change a
print (a)       # a after some change to it looks like: [2, 3, 4]
print (b)       # b will also be changed, and looks like: [2, 3, 4]

# This can easily be worked around by using b=a[:] instead.
a=[2, 3, 4, 5]
b=a[:]          # set b to a    This is the way to clone the list
del a[3]        # change a, by deleting it's element at 3rd index
print (a)       # a after some change to it looks like: [2, 3, 4]
print (b)       # b will also be changed, and looks like: [2, 3, 4, 5]


# Lists in Python at a glance:

list1 = []                      # A new empty list
list2 = [1, 2, 3, "cat"]        # A new non-empty list with mixed item types
list1.append("cat")             # Add a single member, at the end of the list
list1.extend(["dog", "mouse"])  # Add several members
list1.insert(0, "fly")          # Insert at the beginning
list1[0:0] = ["cow", "doe"]     # Add members at the beginning
doe = list1.pop(1)              # Remove item at index
if "cat" in list1:              # Membership test
    list1.remove("cat")           # Remove AKA delete
# list1.remove("elephant") - throws an error [ ValueError: list.remove(x): x not in list]
for item in list1:              # Iteration AKA for each item
    print(item)
print("Item count:", len(list1)) # Length AKA size AKA item count
list3 = [6, 7, 8, 9]
for i in range(0, len(list3)):  # Read-write iteration AKA for each item
    list3[i] += 1                 # Item access AKA element access by index
last = list3[-1]                # Last item
nextToLast = list3[-2]          # Next-to-last item
isempty = len(list3) == 0       # Test for emptiness
set1 = set(["cat", "dog"])      # Initialize set from a list
list4 = list(set1)              # Get a list from a set
list5 = list4[:]                # A shallow list copy
list4equal5 = list4==list5      # True: same by value
list4refEqual5 = list4 is list5 # False: not same by reference
list6 = list4[:]
del list6[:]                    # Clear AKA empty AKA erase
list7 = [1, 2] + [2, 3, 4]      # Concatenation
print(list1, list2, list3, list4, list5, list6, list7)
print(list4equal5, list4refEqual5)
print(list3[1:3], list3[1:], list3[:2]) # Slices
print(max(list3 ), min(list3 ), sum(list3))# Aggregates

print([x for x in range(10)] )  # List comprehension
print([x for x in range(10) if x % 2 == 1])
print([x for x in range(10) if x % 2 == 1 if x < 5])
print([x + 1 for x in range(10) if x % 2 == 1])
print([x + y for x in '123' for y in 'abc'])


# List creation
# a.    Plain creation
list = [ 1,2,3,"This is a list",'c'] # Or, list = [ 1,2,3,"This is a list",'c',Employee("kong") ]

# b.    List comprehensions
'''
        output_list = [ output_exp for var in input_list if (var satisfies this condition) ]
                        ---||----  ---------------------------||--------------------------
what each element will look like                      what you do to get it
    Above is the basic structure of a list comprehension. Note that list comprehension may or may not contain an if condition. 
'''
# Suppose we want to create an output list which contains squares of all the numbers from 1 to 9. Let's see how to do this using for loops and list comprehension.
# Constructing output list using for loop 
output_list = [] 
for var in range(1, 10): 
    output_list.append(var ** 2) 
    
print("Output List using for loop:", output_list) 


# Constructing output list using list comprehension 
list_using_comp = [var**2 for var in range(1, 10)] 
print("Output List using list comprehension:", list_using_comp) 



# Non-Continuous slices
'''    
    It is also possible to get non-continuous parts of an array. 
    If one wanted to get every n-th occurrence of a list, one would use the : : operator. 
    The syntax is a : b : n where a and b are the start and end of the slice to be operated upon.
'''
list = [i for i in range(10) ]
print(list)         # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[::2])    # Output: [0, 2, 4, 6, 8]
print(list[1:7:2])  # Output: [1, 3, 5]



# Comparing lists
        # Lists can be compared for equality.    
print([1,2] == [1,2])   # Output: True
print([1,2] == [3,4])   # Output: False


    # Lists can be compared using a less-than operator, which uses lexicographical order:
'''
        When applied to numbers (for alphabets, its dictionary order), lexicographic order is increasing numerical order, 
        i.e. increasing numerical order (numbers read left to right). 
        For example, the permutations of {1,2,3} in lexicographic order are 123, 132, 213, 231, 312, and 321.
'''
print([0,0] < [0,1])   # Output: True
print([0,9] < [1,0])   # Output: True
print([8,9] < [9,0])   # Output: True
print([7,8,9] < [7,9,0])   # Output: True
print([7,8,9] < [7,0,10])   # Output: False

print(["a","b"] < ["b","a"])    # Output: True
print(["x","b"] < ["x","a"])    # Output: False


# Sorting lists
list1 = [2,3,1,'a','B']
#    list1.sort()                   # TypeError: '<' not supported between instances of 'str' and 'int'

list1 = ['2','3','1','a','B']
list1.sort()                        # list1 gets modified, case sensitive.       Output: ['1', '2', '3', 'B', 'a']

'''
Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    
Note that unlike the sort() method, sorted(list) does not sort the list in place, but instead returns the sorted list. 
The sorted() function, like the sort() method also accepts the reverse parameter.
'''
list2 = sorted(list1)            # list1 is unmodified; since Python 2.4.     Output: ['1', '2', '3', 'B', 'a']
list3 = sorted(list1, key=lambda x: x.lower()) # case insensitive              Output: ['1', '2', '3', 'a', 'B']
list4 = sorted(list1, reverse=True)    # Reverse sorting order: descending     Output: ['a', 'B', '3', '2', '1']

# Note that the list is sorted in place, and the sort() method returns None to emphasize this side effect. 


# Iteration
listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Read-only iteration over a list, AKA for each element of the list: 
for item in listOfNumbers:
    print (item)

# Writable iteration over a list:     
for i in range(0, len(listOfNumbers)):
    listOfNumbers[i]+=1     # Modify the item at an index as you see fit
    
print (listOfNumbers)       # Prints: [2, 3, 4, 5, 6, 7, 8, 9]

# range(start, end, increment/decrement)

# From a number to a number with a step: 
print('step(increment) 3')
for i in range(0, len(listOfNumbers), 3): # For i=0 to 7 step(increment) 3, i.e. skips next two elements starting with index = 0
    print(listOfNumbers[i])

print('step(decrement) 3')
for i in range(len(listOfNumbers)-1, 0, -3): # For i=7 to 0 step(decrement) 3
    print(listOfNumbers[i])
    
# For each element of a list satisfying a condition (filtering):

def condition(item):
    return item > 2

for item in listOfNumbers:
    if not condition(item):
        continue
    print(item)

# Removing
#    Removing aka deleting an item at an index (pop(i)):

list1 = [1, 2, 3, 4]
list1.pop() # Remove the last item
list1.pop(0) # Remove the first item , which is the item at index 0
print(list1)

list1 = [1, 2, 3, 4]
del list1[1] # Remove the 2nd element; an alternative to list.pop(1)
print(list1)

# Removing an element by value:
list1 = ["a", "a", "b"]
list1.remove("a") # Removes only the 1st occurrence of "a"
print(list1)


# Keeping only items in a list satisfying a condition, and thus removing the items that do not satisfy it:

list1 = [1, 2, 3, 4]
newlist = [item for item in list1 if item > 2]  # This uses a list comprehension.
print(newlist)

# Removing items failing a condition can be done without losing the identity of the list being made shorter, by using "[:]":

list1 = [1, 2, 3, 4]
sameList = list1
list1[:] = [item for item in list1 if item > 2]
print(sameList, sameList is list1)

# Removing items failing a condition can be done by having the condition in a separate function:

list1 = [1, 2, 3, 4]

def keepingCondition(item):
    return item > 2

sameList = list1
list1[:] = [item for item in list1 if keepingCondition(item)]
print(sameList, sameList is list1)

'''
    https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
'''
# Removing items while iterating a list usually leads to unintended outcomes unless you do it carefully by using an index:
list1 = [1, 2, 3, 4]
index = len(list1)
while index > 0:
    index -= 1
    if not list1[index] < 2:
        list1.pop(index)


# Aggregates
#    There are some built-in functions for arithmetic aggregates over lists. These include minimum, maximum, and sum:

list = [1, 2, 3, 4]
print(max(list), min(list), sum(list))
average = sum(list) / float(len(list)) # Provided the list is non-empty
# The float above ensures the division is a float one rather than integer one.
print(average)

#    The max and min functions also apply to lists of strings, returning maximum and minimum with respect to alphabetical order:
list = ["aa", "ab"]
print(max(list), min(list)) # Prints "ab aa"



# Copying
#    Copying AKA cloning of lists:

# Making a shallow copy:

list1= [1, 'element']
list2 = list1[:]    # Copy using "[:]"
list2[0] = 2        # Only affects list2, not list1
print(list1[0])     # Displays 1

# By contrast
list1 = [1, 'element']
list2 = list1
list2[0] = 2        # Modifies the original list
print(list1[0])     # Displays 2

#    The above does not make a deep copy, which has the following consequence:
list1 = [1, [2, 3]] # Notice the second item being a nested list
list2 = list1[:]    # A shallow copy
list2[1][0] = 4     # Modifies the 2nd item of list1 as well
print(list1[1][0])  # Displays 4 rather than 2

#    Making a deep copy:
import copy
list1 = [1, [2, 3]] # Notice the second item being a nested list
list2 = copy.deepcopy(list1) # A deep copy
list2[1][0] = 4     # Leaves the 2nd item of list1 unmodified
print(list1[1][0])  # Displays 2



# Clearing a list:

del list1[:] # Clear a list
list1 = []   # Not really clear but rather assign to a new empty list

#    Clearing using a proper approach makes a difference when the list is passed as an argument:

def workingClear(ilist):
    del ilist[:]

def brokenClear(ilist):
    ilist = [] # Lets ilist point to a new list, losing the reference to the argument list
list1=[1, 2]; workingClear(list1); print(list1)
list1=[1, 2]; brokenClear(list1); print(list1)


# Removing duplicate items from a list (keeping only unique items) can be achieved as follows.

#    If each item in the list is hashable, using list comprehension, which is fast:
list1 = [1, 4, 4, 5, 3, 2, 3, 2, 1]
seen = {}
list1[:] = [seen.setdefault(e, e) for e in list1 if e not in seen]

#    If each item in the list is hashable, using index iteration, much slower:
list1 = [1, 4, 4, 5, 3, 2, 3, 2, 1]
seen = set()
for i in range(len(list1) - 1, -1, -1):
    if list1[i] in seen:
        list1.pop(i)
    seen.add(list1[i])

#    If some items are not hashable, the set of visited items can be kept in a list:
list1 = [1, 4, 4, ["a", "b"], 5, ["a", "b"], 3, 2, 3, 2, 1]
seen = []
for i in range(len(list1) - 1, -1, -1):
    if list1[i] in seen:
        list1.pop(i)
    seen.append(list1[i])

#    If each item in the list is hashable and preserving element order does not matter:
list1 = [1, 4, 4, 5, 3, 2, 3, 2, 1]
list1[:] = list(set(list1))  # Modify list1
list2 = list(set(list1))

'''
    In the above examples where index iteration is used, scanning happens from the end to the beginning. 
    When these are rewritten to scan from the beginning to the end, the result seems hugely slower.
''' 

# Operators

l = [0, 1, 2, 3, 4]
for x in l:     # in operator, returns True if element is present in the list, else returns False
    print(x)
    
# Difference
# To get the difference between two lists, just iterate:

a = [0, 1, 2, 3, 4, 4]
b = [1, 2, 3, 4, 4, 5]
print([item for item in a if item not in b])    # [0]

# Intersection
#    To get the intersection between two lists (by preserving its elements order, and their doubles), apply the difference with the difference:

a = [0, 1, 2, 3, 4, 4]
b = [1, 2, 3, 4, 4, 5]
dif = [item for item in a if item not in b]
print([item for item in a if item not in dif])  # [1, 2, 3, 4, 4]
