# Arithmetic Operators: +, -, *, /, %, **, //
print("Arithmetic Operators")
a = 21
b = 2
c=a+b
d=a-b
e=a*b
f=a/b
g=a % b
print(c)
print(d)
print(e)
print(f)
print(g)
# ---------------------------------
# Comparison Operators ( ==, !=, > , <, >=, <= )
print("Comparison Operators")
x=50
print(x==10)
print(x!=10)
print(x>20)
print(x<20)
print(x>=20)
print(x<=20)

# Logical Operator ( and, or, not)
print("*****Logical Operators*****")
print(10>5 and 8>3 and 50==50)
print(10>20 and 50>20)
print(10>20 or 20>=20)
print( not(5>2) )
print( not(20>10) )
# Assignment Operator ( =, +=, -=, *=, /=)
print("Assignment Operator")
x=10
x=x+10
x += 10
x -= 10 # ( x = x -10)
print(x)

#Membership Operators ( in , not in)
print("Membership Operators ( in , not in)")

a= "Python Programming"
print('mmm' in a)
print('mmm' not in a)

numbers = [1,2,3,4,5,6]
print( 10 not in numbers)

# Identity operators ( is, is not)
print("Identity operators")
a = 10
b = 10
c = 20
print (a is b)
print (a is c)
print (a is not c)




