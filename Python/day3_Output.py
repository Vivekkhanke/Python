# Output formatting

name = input("Enter the Name : ")
age = 25

print("Name : ",name, "Age : ",age)
# My name is Vivek and I am 26 years old
print(f"My name is {name} and I am {age} years old")
x=5
y=8

x=int(input("Enter the value of X : "))
y=int(input("Enter the value of Y : "))
# Addditiojn of 25 and 23 is : 48
print(f"Addition of {x} and {y} is {x+y}")

# Multiple inputs in one line
a,b,c,d = map(int, input("Enter the number : ").split() ) # 21 32 25 21

print("Addition of a and b is : ",a+b+c+d)
