'''
    Sets
    Sets are just like lists except that they are unordered and they do not allow duplicate values. 
    Elements of a set are neither bound to a number (like list and tuple) nor to a key (like dictionary). 
    The reason for using a set over other data types:
        is that a set is much faster for a large number of items than a list or tuple and 
        sets provide fast data insertion, deletion, and membership testing. 
        Sets also support mathematical set operations such as testing for subsets and finding the union or intersection of two sets.
        
     Note that sets are unordered, items you add into sets will end up in an indeterminable position, and it may also change from time to time. 
     Sets cannot contain a single value more than once.
    
     Unlike lists, which can contain anything, the types of data that can be included in sets are restricted. A set can only contain hashable, immutable data types. 
        Integers, strings, and tuples are hashable; 
        lists, dictionaries, and other sets (except frozensets) are not.
'''

mySet = set([42, 'a string', (23, 4)])
print(mySet)    # Prints: {'a string', 42, (23, 4)}    # Please note the order has changed

# Let's change the order in the Set, observe the output order of elements
mySet = set([42, (23, 4),'a string'])
print(mySet)        # Prints: {(23, 4), 42, 'a string'}

mySet.add("Hello")  # To add another element to existing Set
print(mySet)        # Prints: {(23, 4), 42, 'Hello', 'a string'}

mySet.add("Hello")  # To add duplicate element to existing Set
print(mySet)        # Prints: {(23, 4), 42, 'Hello', 'a string'}    # duplicate element was not added

copySet = mySet.copy()  # Way to copy a set. However, remember that the copy constructor will copy the set, but not the individual elements.
print(copySet)      # Prints: {(23, 4), 'Hello', 42, 'a string'}

mySet.update("World!")
print(mySet)        # Prints: {(23, 4), 42, 'r', 'a string', 'o', 'd', 'W', '!', 'Hello', 'l'}

print(set("obtuse"))    # Prints: {'b', 't', 's', 'o', 'e', 'u'}

# Membership Testing
print(42 in mySet)              # True
print(copySet in mySet)         # False

# Given two sets S1 and S2, we check if S1 is a subset or a superset of S2. 
print(copySet.issubset(mySet))  # True
print(copySet.issuperset(mySet))# False

# Note that the <= and >= operators also express the issubset and issuperset functions respectively.
print(copySet <= mySet)     # Prints: True, Just like copySet.issubset(mySet)
print(copySet >= mySet)     # Prints: False, Just like copySet.issuperset(mySet)

# Removing Items
'''
    There are three functions which remove individual items from a set, called:
        pop, 
        remove, and 
        discard. 
'''
# The first, pop, simply removes an item from the set. Note that there is no defined behavior as to which element it chooses to remove. 
mySet.pop()
print(mySet)    # Prints: {'r', 42, 'W', 'o', '!', 'l', 'd', 'Hello', 'a string'}

# We also have the "remove" function to remove a specified element. However, removing a item which isn't in the set causes an error. 
# mySet.remove("World!")  # This throws error: KeyError: 'World!'

# If you wish to avoid this error, use "discard." It has the same functionality as remove, but will simply do nothing if the element isn't in the set 
mySet.discard("World!") # Prints: {'!', 'Hello', 'l', 42, 'W', 'd', 'o', 'r', 'a string'}
print(mySet)

mySet.remove("!")
print(mySet) # Prints: {'W', 'a string', 'Hello', 42, 'l', 'o', 'r', 'd'}

# We also have another operation for removing elements from a set, clear, which simply removes all elements from the set. 
copySet.clear()
print(copySet)  #Prints: set()    empty Set

# Iteration Over Sets
# We can also have a loop move over each of the items in a set. However, since sets are unordered, it is undefined which order the iteration will follow. 
for n in mySet:
    print(n)
    
'''
Prints:
    Hello
    d
    42
    W
    r
    l
    a string
    o
'''

# Set Operations
'''
    Python allows us to perform all the standard mathematical set operations, using members of set. 
    Note that each of these set operations has several forms. 
    One of these forms, s1.function(s2) will return another set which is created by "function" applied to S1 and S2. 
    The other form, s1.function_update(s2), will change S1 to be the set created by "function" of S1 and S2. 
    Finally, some functions have equivalent special operators. For example, s1 & s2 is equivalent to s1.intersection(s2) 
'''
# Intersection    Any element which is in both S1 and S2 will appear in their intersection. 
copySet.add("Hello")
print(mySet.intersection(copySet))      # Prints: {'Hello'}
print(set.intersection(copySet, mySet)) # Prints: {'Hello'}    This is using set constructor

# Union    The union is the merger of two sets. Any element in S1 or S2 will appear in their union.
copySet.add("Pyhton")
print(mySet.union(copySet)) # Prints: {'o', 'l', 42, 'd', 'Pyhton', 'r', 'a string', 'W', 'Hello'}
print(mySet|copySet)        # Prints: {'o', 'l', 42, 'd', 'Pyhton', 'r', 'a string', 'W', 'Hello'}

# Symmetric Difference    The symmetric difference of two sets is the set of elements which are in one of either set, but not in both. 
print(mySet.symmetric_difference(copySet))  # Prints: {'a string', 'Pyhton', 'o', 'W', 42, 'r', 'd', 'l'}
print(mySet.symmetric_difference_update(copySet))   # Prints: None

# Set Difference    Python can also find the set difference of S1 and S2, which is the elements that are in S1 but not in S2. 
print(mySet.difference(copySet))    # Prints: {'W', 42, 'o', 'r', 'a string', 'd', 'l'}
print(copySet.difference(mySet))    # Prints: {'Hello'}
print(copySet - mySet)              # Prints: {'Hello'}

print(mySet.difference_update(copySet)) # None

# Multiple sets    Starting with Python 2.6, "union", "intersection", and "difference" can work with multiple input by using the set constructor. For example, using "set.intersection()": 
s1 = set([3, 6, 7, 9])
s2 = set([6, 7, 9, 10])
s3 = set([7, 9, 10, 11])
print(set.intersection(s1, s2, s3)) # Prints: set([9, 7])



'''
    Frozenset
    The relationship between frozenset and set is like the relationship between tuple and list. Frozenset is an immutable version of set. 
    Since they are immutable, they are also hashable, which means that frozensets can be used as members in other sets and as dictionary keys. 
    frozensets have the same functions as normal sets, except none of the functions that change the contents (update, remove, pop, etc.) are available. 
'''
myFrozenSet = frozenset(['Hello','World','!', 4])
print(myFrozenSet)  # Prints: frozenset({4, '!', 'Hello', 'World'})

anotherSet = set([myFrozenSet, 4, 5, 6])
print(anotherSet)       # Prints: {5, frozenset({4, '!', 'Hello', 'World'}), 4, 6}

print(myFrozenSet.intersection(anotherSet)) # frozenset({4})

#    myFrozenSet.add(6)
#    print(myFrozenSet)  # Throws error: AttributeError: 'frozenset' object has no attribute 'add'


# Sets in Python at a glance:

set1 = set()                   # A new empty set
set1.add("cat")                # Add a single member
set1.update(["dog", "mouse"])  # Add several members, like list's extend
set1 |= set(["doe", "horse"])  # Add several members 2, like list's extend
if "cat" in set1:              # Membership test
    set1.remove("cat")
#set1.remove("elephant") - throws an error
set1.discard("elephant")       # No error thrown
print(set1)
for item in set1:              # Iteration AKA for each element
    print(item)
print("Item count:", len(set1)) # Length AKA size AKA item count
#1stitem = set1[0]             # Error: no indexing for sets
isempty = len(set1) == 0       # Test for emptiness
set1 = {"cat", "dog"}          # Initialize set using braces; since Python 2.7
#set1 = {}                     # No way; this is a dict
set1 = set(["cat", "dog"])     # Initialize set from a list
set2 = set(["dog", "mouse"])
set3 = set1 & set2             # Intersection
set4 = set1 | set2             # Union
set5 = set1 - set3             # Set difference
set6 = set1 ^ set2             # Symmetric difference
issubset = set1 <= set2        # Subset test
issuperset = set1 >= set2      # Superset test
set7 = set1.copy()             # A shallow copy
set7.remove("cat")
print(set7.pop())              # Remove an arbitrary element
set8 = set1.copy()
set8.clear()                   # Clear AKA empty AKA erase
set9 = {x for x in range(10) if x % 2} # Set comprehension; since Python 2.7
print(set1, set2, set3, set4, set5, set6, set7, set8, set9, issubset, issuperset)


