# List of orders (Orderid, cust_name, amount)
orders = [
    (101, "Amit", 500),
    (102, "Rahul", 1500),
    (103, "Amit", 700),
    (104, "Vivek", 2000),
    (105, "sita", 300),
    (106, "Rahul", 800)
]

# set to store unique orders
unique_customers = set()

# store high value orders
high_value_orders = []

total_Sales = 0

for order in orders:
    order_id,name,amount = order  #tuple unpacing
    # add customers
    unique_customers.add(name)
    # add total sales
    total_Sales += amount #(total_Sales = total_Sales + amount)
    
    if amount > 1000:
        high_value_orders.append(order)
        print(f"High value order: {order_id} - {name} - {amount}")
    else:
        print(f"Regular oredrs: {order_id} - {name} - {amount}")
    
print("\n ****** Summary *******")
print("Total sales: ",total_Sales)
print("Unique customers: ",unique_customers)
print("Number of unique customers: ", len(unique_customers))
print("\n High value orders: ")

for hv in high_value_orders:
    print(hv)