# Abstraction is a fundamental concept in object-oriented programming (OOP) that allows you to hide the internal details of an object and only expose the necessary features to the outside world. In Python, you can achieve abstraction using abstract classes and abstract methods.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car is start with key...")
    
class Bike(Vehicle):
    def start(self):
        print("Bike is start with kick...")
    
c = Car()
c.start()