product = {
    "id":101,
    "name":"laptop",
    "price": 50000,
    "stock": 10
}

print(product["price"])

product["stock"] -= 1 # product["stock"] = product["stock"] - 1  #a = a+1 , a+=1
print(product)