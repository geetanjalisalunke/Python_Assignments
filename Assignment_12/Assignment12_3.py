class Arithmetic:
    
    def __init__(self):
        self.value1=0
        self.value2=0
        
    def Accept(self,A,B):
        self.value1=A
        self.value2=B
    
    def Addition(self):
        return self.value1+self.value2
        
    def Substraction(self):
        return self.value1-self.value2
        
    def Multiplication(self):
        return self.value1*self.value2
        
    def Division(self):
        return self.value1/self.value2
    
obj1=Arithmetic()
obj1.Accept(11,10)
ret=obj1.Addition()
print(ret)
ret=obj1.Substraction()
print(ret)
ret=obj1.Multiplication()
print(ret)
ret=obj1.Division()
print(ret)

obj2=Arithmetic()
obj2.Accept(51,2)
ret=obj2.Multiplication()
print(ret)
        