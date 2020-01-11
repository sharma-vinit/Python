# Conditional Statements
# Many languages (like Java and PHP) have the concept of a one-line conditional (called The Ternary Operator), often used to simplify conditionally accessing a value. 
# For instance (in Java): 

#  a normal conditional assignment
'''
int res;
if(number < 0)
    res = -number;
else
    res = number;
'''

# For many years Python did not have the same construct natively, however you could replicate it by constructing a tuple of results and calling the test as the index of the tuple, like so:

number = int(input("Enter a number to get its absolute value:"))
res = (-number, number)[number > 0]
'''
It is important to note that, unlike a built in conditional statement, both the true and false branches are evaluated before returning, 
which can lead to unexpected results and slower executions if you're not careful. To resolve this issue, and as a better practice, 
wrap whatever you put in the tuple in anonymous function calls (lambda notation) to prevent them from being evaluated until the desired branch is called:
'''
number = int(input("Enter a number to get its absolute value:"))
res = (lambda: number, lambda: -number)[number < 0]()

# Since Python 2.5 however, there has been an equivalent operator to The Ternary Operator (though not called such, and with a totally different syntax):

number = int(input("Enter a number to get its absolute value:"))
res = -number if number < 0 else number

# Switch
'''
A switch is a control statement present in most computer programming languages to minimize a bunch of If - elif statements. 
Sadly Python doesn't officially support this statement, but with the clever use of an array or dictionary, 
we can recreate this Switch statement that depends on a value.
'''
x = 1

def hello():
    print ("Hello")

def bye():
    print ("Bye")

def hola():
    print ("Hola is Spanish for Hello")

def adios():
    print ("Adios is Spanish for Bye")

# Notice that our switch statement is a regular variable, only that we added the function's name inside
# and there are no quotes
menu = [hello,bye,hola,adios]

# To call our switch statement, we simply make reference to the array with a pair of parentheses
# at the end to call the function
menu[3]()   # calls the adios function since is number 3 in our array.

menu[0]()   # Calls the hello function being our first element in our array.

menu[x]()   # Calls the bye function as is the second element on the array x = 1

# This works because Python stores a reference of the function in the array at its particular index, and by adding a pair of parentheses we are actually calling the function. 
# Here the last line is equivalent to:
Another way. Using function through user Input

go = "y"
x = 0
def hello():
    print ("Hello")
 
def bye():
    print ("Bye")
 
def hola():
    print ("Hola is Spanish for Hello")
 
def adios():
    print ("Adios is Spanish for Bye")

menu = [hello, bye, hola, adios]
 

while x < len(menu) :
    print ("function", menu[x].__name__, ", press " , "[" + str(x) + "]")
    x += 1
    
while go != "n":
    c = int(input("Select Function: "))
    menu[c]()
    go = input("Try again? [y/n]: ")

print ("\nBye!")
   

#end

#    Another way

if x == 0:
    hello()
elif x == 1:
    bye()
elif x == 2:
    hola()
else:
    adios()

#    Another way is to use lambdas. Code pasted here with permissions1

result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}[value](x)

