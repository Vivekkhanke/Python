class car:
    def __init__(self,name):
        self.name = name
        print("constructor automatically called when the object is created")
    
    def display(self):
        # print("hello")
        print(self.name)
        return "hello"

class train:
    def __init__(self):
        print("Hello")
        
    def start(self):
        print("started")
        

# obj = car("BMW") #create a object
# print(obj.display())

obj_train = train()
obj_train.start()

