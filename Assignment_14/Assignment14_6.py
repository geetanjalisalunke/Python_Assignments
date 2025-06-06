class Calculator:
   
    def Add(self,A,B):
        return A+B
    def Sub(self,A,B):
        return A-B
    def Mult(self,A,B):
        return A*B
    def Div(self,A,B):
        return A/B
    
    
def main():
    
    obj1=Calculator()
    ret=obj1.Add(10,21)
    print(ret)
    ret=obj1.Add(100,21)
    print(ret)
    ret=obj1.Sub(10,21)
    print(ret)
    
    ret=obj1.Div(10,21)
    print(ret)
    ret=obj1.Mult(10,21)
    print(ret)
 
if __name__=="__main__":    
    main()