def make_payment(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Invalid amount")
        else:
            print("Payment successfull : ", amount)
    except ValueError:
        print("Error : ",ValueError)

print("Hello")

make_payment(10)