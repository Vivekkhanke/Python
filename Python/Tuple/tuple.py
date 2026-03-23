"""
() --> Paranthesis
[] --> Square braces
{} --> curly braces
: --> colon
; --> semi colon
~ --> Tild
& --> Ampersand
"""
# Tuple is immutable ( cannot be changed)
a = (1,4,5,3,6,4,7,8)
print(a.count(4))

print(a[2])

tuple = (1,2,3)
tuple[0] = 5
print(tuple)  #Immutable
# ---------------------------------------

# Tuple packing and unpacking
t = (1,2,3,4)
print(t)

a,b,c,d = t  #unpacking

print(a,b,c,d)