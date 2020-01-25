'''
    Divisions
    The result of divisions is somewhat confusing. 
    1. Python 2.x, using the / operator on two integers will return another integer, using floor division. 
        For example, 5/2 will give you 2. 
        You will have to specify one of the operands as a float to get true division, 
            e.g. 5/2. or 5./2 (the dot specifies you want to work with float) will yield 2.5. 
            Starting with Python 2.2 this behaviour can be changed to true division by the future division statement from __future__ import division. 
            
    2. Python 3.x, the result of using the / operator is always true division 
        However, you can ask for floor division explicitly by using the // operator since Python 2.2.
'''

x = 5//2
print(x)        # Prints: 2    using // for division rounds off the result
print(type(x))  # Prints: <class 'int'>

y = 5/2         # Prints:
print(y)        # Prints: 2.5
print(type(y))  # Prints: <class 'float'>