class college:
    a = 50
    b = 20
    c = a + b
    print("C = ",c)
    
    def it(self):
        print("It department")
    
    def entc(self):
        print("ENTC Department")
        
    def mechanical(self):
        print("Mechanical dept")
    
    def cs(self):
        print("CS Department")
        
    def iot(self):
        return 100
    
sg = college() #create object of college class
# sg.it() 
# sg.entc()
# sg.cs()    #calling functions
a =  sg.iot()
print(a)