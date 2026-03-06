# Integer - data type
"""charachteristics : 
Positive and negative integers
No decimal
"""
a=5
age = 25
temperature = -10
#------------------------------------

#Float data type
"""charachteristics : 
values contain decimal point
"""
price = 99.99
weight = 10.5
temperature = -2.3

#------------------------------------

#String data type
"""
string means text data.
string must be inside quotes ( single or double)
"""
name ="Ram"
city ="Pune"
course = 'Python'


#Boolean - Data type
"""
it has only 2 values: True and false or Yes/No.
Boolean represents True and false or Yes/No conditions.
it is used in conditions and decisions.
"""
logged_in = True
is_logged_in = False

# Print data types

print(type(price))
print(type(logged_in))
print(type(city))
print(type(age))


###Types of ERROR ####
# 1. syntax error -- when error in syntaxt
print(("vivek") 

# 2. Run time error -- error occurs while the program is running 
x=10
y=0
print(x/y)  #invalid operation 
print(abc)  #we have not defined the abc variable so we got abc is not defined error

x=10
y="vivek"
print(x+y) # type error addition of integer and string type is not allowed in python

# 3.Logical Error
"""
The error happens when the program runs correctly but gives wrong output
"""
a=10
b=20
avg =  a + b / 2
avg = ( a + b) / 2
print(avg)



