'''
    Type conversion
    In general, the number types are automatically 'up cast' in this order:  
        Int → Long → Float → Complex. 
    The farther to the right you go, the higher the precedence. 
'''

x = 5
print(type(x)) # Prints: <type 'int'>

x = 187687654564658970978909869576453
print(type(x)) # Prints: <type 'long'> in Python 2.x, <type 'int'> in Python 3.x

x = 1.34763    # <type 'float'> 

x = 5 + 2j    # <type 'complex'>


#    1.    Type conversion in Python by example:
v1 = int(2.7)         # 2
v2 = int(-3.9)        # -3
v3 = int("2")         # 2
v4 = int("11", 16)    # 17, base 16
#   v5 = long(2)      # exists only in Python 2.x
v6 = float(2)         # 2.0
v7 = float("2.7")     # 2.7
v8 = float("2.7E-2")  # 0.027
v9 = float(False)     # 0.0
vA = float(True)      # 1.0
vB = str(4.5)         # "4.5"
vC = str([1, 3, 5])   # "[1, 3, 5]"
vD = bool(0)          # False; bool fn since Python 2.2.1
vE = bool(3)          # True
vF = bool([])         # False - empty list
vG = bool([False])    # True - non-empty list
vH = bool({})         # False - empty dict; same for empty tuple
vI = bool("")         # False - empty string
vJ = bool(" ")        # True - non-empty string
vK = bool(None)       # False
vL = bool(len)        # True
vM = set([1, 2])
vN = list(vM)         # [1, 2] <class 'list'>
vO = list({1: "a", 2: "b"})     # dict -> list of keys
vP = tuple(vN)
vQ = list("abc")      # ['a', 'b', 'c']

# 2.    Implicit type conversion:
int1 = 4
float1 = int1 + 2.1             # 6.1     4 converted to float
# str1 = "My int:" + int1       # Error: no implicit type conversion from int to string
str1 = "My int:" + str(int1)    # My int:4
int2 = 4 + True                 # 5: bool is implicitly converted to int
