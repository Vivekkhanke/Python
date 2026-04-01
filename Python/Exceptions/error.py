# # print(5/0)
# try:
#     # code
# except:
#     # Error handle
# finally:
#     # Always run
try: 
    num = int(input("Enter the number : "))
    res = 10 / num
    print(res)
except:
    print("Cannot devide by zero")
finally:
    print("Execution completed")
    
print('hello')