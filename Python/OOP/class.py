class car:
    def start(self):
        print("car started")
    def add(self, a,b):
        c = a+ b
        print(c)
    def stop(self):
        print("car stopped")

obj = car()  # create a object of class

obj.start()  #calling the function.
obj.add(10, 10)