"""
    Built-in Data types
        Python's built-in (or standard) data types can be grouped into several classes like are numeric types, sequences,
        sets and mappings (and a few more).

    boolean:
    The type of the built-in values True and False.
    Useful in conditional expressions, and anywhere else you want to represent the truth or falsity of some condition.
    Mostly interchangeable with the integers 1 and 0.
    In fact, conditional expressions will accept values of any type,
        treating special ones like boolean False, integer 0 and the empty string "" as equivalent to False, and all other values as equivalent to True.
        But for safety's sake, it is best to only use boolean values in these places.

    Numeric types:
    1.    int:     Integers; equivalent to C longs in Python 2.x, non-limited length in Python 3.x
    2.    long:    Long integers of non-limited length; exists only in Python 2.x
    3.    float:   Floating-Point numbers, equivalent to C doubles
    4.    complex: Complex Numbers are entered by adding a real number and an imaginary one, which is entered by appending a j.
                   i.e. 10+5j is a complex number. So is 10j, Note that j by itself does not constitute a number. If this is desired, use 1j.

    Sequences:     Details in com.Python.Sequences
    1.    str:     String; represented as a sequence of 8-bit characters in Python 2.x,
                   but as a sequence of Unicode characters (in the range of U+0000 - U+10FFFF) in Python 3.x
    2.    bytes:     a sequence of integers in the range of 0-255; only available in Python 3.x
    3.    byte array: like bytes, but mutable (see below); only available in Python 3.x
    4.    list
    5.    tuple

    Sets:
    1.    set: an unordered collection of unique objects; available as a standard type since Python 2.6
    2.    frozen set: like set, but immutable; available as a standard type since Python 2.6

    Mappings:
    1.    dict: Python dictionaries, also called hashmaps or associative arrays, which means that an element of the list
          is associated with a definition,
                rather like a Map in Java

"""
import numbers

# ellipsis:     ameError: name 'ellipsis' is not defined
# None:         TypeError: descriptor 'mro' requires a 'type' object but received a 'NoneType'
# NotImplemented:   TypeError: descriptor 'mro' requires a 'type' object but received a 'NotImplementedType'
# numbers:          TypeError: descriptor 'mro' requires a 'type' object but received a 'module'

list_of_data_types = [numbers.Number, numbers.Integral, int, bool,
                      numbers.Complex, float, numbers.Rational, numbers.Real, str, bytes, list,
                      tuple, bytearray, set, dict]
for types in list_of_data_types:
    print(types, " : ", type.mro(types))

'''
object
+-- None
+-- NotImplemented
+-- ellipsis

+-- numbers
	+-- Number
		+-- Integral
	+-- Complex
		+-- Real
			+-- Rational
	
+-- int
	+-- bool
+-- float

+-- str
+-- bytes
+-- list
+-- tuple
+-- bytearray
+-- set
+-- dict
'''