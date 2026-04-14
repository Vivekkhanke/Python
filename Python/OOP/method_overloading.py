# Method/Function Overloading in Python

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

obj = Calculator()
a = obj.add(1,2,3)
print(a)

# Method/Function Overloading using default arguments
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()
print(obj.add(5))         # Output: 5
print(obj.add(1, 2))      # Output: 3
print(obj.add(1, 2, 3))   # Output: 6

# using *args for method overloading

class Calculator:
    def add(self, *args):
        return sum(args) 
       
obj = Calculator()
print(obj.add(5))         # Output: 5
print(obj.add(5,5))         # Output: 
print(obj.add(1, 2, 3))   # Output: 
print(obj.add(1, 2, 3, 4))   # Output: 10