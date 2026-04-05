with open("F:\Python Programs\Python\File Handling\sales.csv", "r") as file:
    for i in file:
        Order_ID,Order_Date,Region,Category,Product_Name,Quantity,Unit_Price,Cost_Price,Sales,Profit = i.strip().split(",")
        print(Order_ID,Order_Date,Region,Category,Product_Name,Quantity,Unit_Price,Cost_Price,Sales,Profit)
        
# 1001,2024-01-05,North,Electronics,Laptop,2,60000,50000,120000,20000