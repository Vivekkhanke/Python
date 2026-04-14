
class Payment:
    def pay(self):
        print("processing payment")
    
class UPI(Payment):
    def pay(self):
        print("processing UPI payment")
        
class Card(Payment):
    def pay(self):
        print("processing card payment")

pay = [UPI(), Card()]  # create pay object for both the classes

for p in pay:
    p.pay()  # call the pay method for both the classes
    
    
