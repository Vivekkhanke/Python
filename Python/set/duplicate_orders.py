orders = [101,102,103,101]
set = set(orders)

if len(orders) != len(set):
    print("Duplicate orders found")
else:
    print("No Duplicates")