'''
    Dictionaries
    Dictionaries are also like lists, and they are mutable -- you can add, change, and remove elements from a dictionary. 
    However, the elements in a dictionary are not bound to numbers, the way a list is. 
    Every element in a dictionary has two parts: a key, and a value. 
        Calling a key of a dictionary returns the value linked to that key. 
        You could consider a list to be a special kind of dictionary, in which the key of every element is a number, in numerical order. 
        
    A dictionary in Python is a collection of unordered values accessed by key rather than by index. 
    The keys have to be hashable: integers, floating point numbers, strings, tuples, and frozensets are hashable, 
    while lists, dictionaries, and sets other than frozensets are not. 
    
    Dictionaries were available as early as in Python 1.4. 
'''

# Dictionaries in Python at a glance:

dict1 = {}                     # Create an empty dictionary
dict2 = dict()                 # Create an empty dictionary 2
dict2 = {"r": 34, "i": 56}     # Initialize to non-empty value
dict3 = dict([("r", 34), ("i", 56)])      # Init from a list of tuples
dict4 = dict(r=34, i=56)       # Initialize to non-empty value 3
dict1["temperature"] = 32      # Assign value to a key
if "temperature" in dict1:     # Membership test of a key AKA key exists
    del dict1["temperature"]   # Delete AKA remove
equalbyvalue = dict2 == dict3
itemcount2 = len(dict2)        # Length AKA size AKA item count
isempty2 = len(dict2) == 0     # Emptiness test
for key in dict2:              # Iterate via keys
    print(key, dict2[key])     # Print key and the associated value
    dict2[key] += 10           # Modify-access to the key-value pair
for key in sorted(dict2):      # Iterate via keys in sorted order of the keys
    print(key, dict2[key])     # Print key and the associated value
for value in dict2.values():   # Iterate via values
    print(value)
for key, value in dict2.items(): # Iterate via pairs
    print(key, value)
dict5 = {} # {x: dict2[x] + 1 for x in dict2 } # Dictionary comprehension in Python 2.7 or later
dict6 = dict2.copy()             # A shallow copy
dict6.update({"i": 60, "j": 30}) # Add or overwrite; a bit like list's extend
dict7 = dict2.copy()
dict7.clear()                  # Clear AKA empty AKA erase
sixty = dict6.pop("i")         # Remove key i, returning its value
print(dict1, dict2, dict3, dict4, dict5, dict6, dict7, equalbyvalue, itemcount2, sixty)

# Dictionaries may be created directly or converted from sequences. Dictionaries are enclosed in curly braces, {}
# Dictionaries are declared using curly braces, and each element is declared first by its key, then a colon, and then its value.
# Keys could be of any primitive data type, like string, number etc.
definitions = {"key1": 1, "key2": 2, "3": 4, 4: 5, 6.0: 'Storing_Float'}
print(definitions["key1"], definitions["3"], definitions[4], definitions[6.0])    # Prints: 1 4 5 Storing_Float


# Also, adding an element to a dictionary is much simpler: simply declare it as you would a variable.
definitions[True] = False
print(definitions)  # Prints: {'key1': 1, 'key2': 2, '3': 4, 4: 5, 6.0: 'Storing_Float', True: False}

d = {'city':'Paris', 'age':38, (102,1650,1601):'A matrix coordinate'}
seq = [('city','Paris'), ('age', 38), ((102,1650,1601),'A matrix coordinate')]
print(d)    # Prints: {'city': 'Paris', 'age': 38, (102, 1650, 1601): 'A matrix coordinate'}
print(dict(seq))    # Prints: {'city': 'Paris', 'age': 38, (102, 1650, 1601): 'A matrix coordinate'}
print(d == dict(seq))   # Prints: True

# Also, dictionaries can be easily created by zipping two sequences. 
seq1 = ('a','b','c','d')
seq2 = [1,2,3,4]
d = dict(zip(seq1,seq2))
print(d)    # Prints:  {'a': 1, 'c': 3, 'b': 2, 'd': 4}

# Operations on Dictionaries
# The operations on dictionaries are somewhat unique. Slicing is not supported, since the items have no intrinsic order.
d = {'a':1,'b':2, 'cat':'Fluffers'}
d.keys()    ['a', 'b', 'cat']
d.values()    [1, 2, 'Fluffers']
print(d['a'])   # Prints:     1
d['cat'] = 'Mr. Whiskers'
print(d['cat'])    # Prints: 'Mr. Whiskers'
print('cat' in d)    # Prints: True
print('dog' in d)    # Prints: False


# Combining two Dictionaries
# You can combine two dictionaries by using the update method of the primary dictionary. 
# Note that the update method will merge existing elements if they conflict.

d = {'apples': 1, 'oranges': 3, 'pears': 2}
ud = {'pears': 4, 'grapes': 5, 'lemons': 6}
d.update(ud)
print(d)    # Prints:  {'grapes': 5, 'pears': 4, 'lemons': 6, 'apples': 1, 'oranges': 3}

# Deleting from dictionary    del dictionaryName[membername]
del d['apples']

