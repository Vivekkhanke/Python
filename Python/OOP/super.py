class Animal:
    def show(self):
        print("Parent Method")
        
class Dog(Animal):
    def show(self):
        super().show()
        print("child method")
    
obj = Dog()
obj.show()

