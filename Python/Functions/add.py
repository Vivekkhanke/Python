def add(a,b):
    return a+b

result =  add(20,10)
print(result)

# No parameter with return
def num():
    return 10

val = num()
print(val)

# Default parameter
def greet(name="Vivek"):
    print("Hello", name)
    
greet()