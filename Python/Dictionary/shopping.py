cart = {
    "Laptop" :1,
    "Mouse": 5,
    "Keyboard":2,
    "Mouse" : 4,
    "Laptop" :11,
    "Mouse" : 8,
}
total_items=0  #1, 6, 8

for p, qty in cart.items():
    total_items = total_items + qty   # total_items = 0 + 1

print("Total Items : ",total_items)

print(cart)