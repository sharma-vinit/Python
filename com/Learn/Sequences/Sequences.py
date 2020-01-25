'''
Sequences allow you to store multiple values in an organized and efficient fashion. There are seven sequence types: 
    1.    strings, 
    2.    Unicode strings, 
    3.    lists, 
    4.    tuples, 
    5.    bytearrays, 
    6.    buffers, and 
    7.    xrange objects. 


Other data types
Python also has other types of sequences, though these are used less frequently and need to be imported from the standard library before being used.
    array                      A typed-list, an array may only contain homogeneous values.
    collections.defaultdict    A dictionary that, when an element is not found, returns a default value instead of error.
    collections.deque          A double ended queue, allows fast manipulation on both sides of the queue.
    heapq                      A priority queue.
    Queue                      A thread-safe multi-producer, multi-consumer queue for use with multi-threaded programs. 
                               Note that a list can also be used as queue in a single-threaded code.


3rd party data structure
Some useful data types in Python do not come in the standard library. Some of these are very specialized in their use. 
    numpy.array                useful for heavy number crunching 
    sorteddict                 like the name says, a sorted dictionary

'''

'''
    An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), 
    and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value.

    Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

    All of Python’s immutable built-in objects are hashable, while no mutable containers (such as lists or dictionaries) are. Objects which are instances of user-defined classes are hashable by default; they all compare unequal, and their hash value is their id().
'''