try:
    a = int(input("Enter the num : "))
    b = 5
    print(a/b)
except TypeError:
    print("Invalid data types")
    
try:
    a = "10"
    b = 5
    print(a/b)
except TypeError:
    print("Invalid data types")