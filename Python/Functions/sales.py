cart = []
# function to add products
def add_product(cart, name, price, quantity):
    total = price * quantity
    cart.append((name, price, quantity, total))

# calculate total bill
def calculate_total(cart):
    total_amt = 0
    for item in cart:
        total_amt = total_amt + item[3]
    return total_amt
    
def discount(total):
    if total > 2000:
        return total * 0.90 # 10 % discount
    elif total > 1000:
        return total * 0.95 # 5 % discount
    else:
        return total 

def display_bill():
    print("\n ----Invoice-----")
    for item in cart:
        print(f"{item[0]} | Price : {item[1]} | Qty: {item[2]} | Total: {item[3]}")
          


# call to functions
# Input --function

add_product(cart, "Laptop",1000,2)
add_product(cart, "Iphone",100,2)

total = calculate_total(cart)
final_amt = discount(total)
display_bill()
print("Final Amount : ",final_amt)



