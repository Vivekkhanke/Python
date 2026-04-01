try:
    num = int(input("Enter the number : "))
    print(10/num)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid Input")
finally:
    print("Execution completed")
    
print("Hello")
