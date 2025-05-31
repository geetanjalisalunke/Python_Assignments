class Demo:
    Value=0
    def __init__(self,A,B):
        self.no1=A
        self.no2=B
    
    def fun(self):
        print("Inside Fun")
        print(self.no1)
        print(self.no2)
        
    def gun(self):
        print("Inside Gun")
        print(self.no1)
        print(self.no2)
        
obj1=Demo(11,21)
obj2=Demo(51,101)

obj1.fun()  #11 ,21
obj1.gun()  #11 ,21
obj2.fun()  #51,101
obj2.gun()  #51,101