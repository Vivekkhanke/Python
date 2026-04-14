# polymorphism   

# Method 
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

obj_list = [Dog(), Cat()]

for a in obj_list:
    a.sound()
    
# -----------------------------------------------------------
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