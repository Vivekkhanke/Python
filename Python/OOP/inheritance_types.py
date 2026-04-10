# Single level inheritance
class Parent:
    def hello(self):
        print("parent")

class father(Parent):
    def hello1(self):
        print("father")
    
obj = father()
obj.hello1()
obj.hello()
# ----------------------

# Multilevel Inheritance
class Parent:
    def hello(self):
        print("parent")

class father(Parent):
    def hello1(self):
        print("father")
    
class son(father):
    def hello2(self):
        print("son")
    
obj = son()
obj.hello1()
obj.hello()

# Multiple inheritance
class Father:
    def property(self):
        print("Father property")

class Mother:
    def property(self):
        print("Mother property")
        

class Child(Father, Mother):
    pass

obj = Child()
obj.property()


# Hierarchical inheritance
class Animal:
    def eat(self):
        print("Animal Eating")

class cat(Animal):
    pass
    
class dog(Animal):
    def eat(self):
        print("Dog Eating")
    

dog = dog()  #Cret
cat = cat()

cat.eat()  # calling function
dog.eat()
