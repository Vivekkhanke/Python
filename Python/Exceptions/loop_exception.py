while True:
    try:
        num = int(input("Enter a number : "))
        print("Result : ", 100 / num)
        break
    
    except ZeroDivisionError:
        print("Division by zero is not allowed")
        
    except ValueError:
        print("Please enter the valid number")