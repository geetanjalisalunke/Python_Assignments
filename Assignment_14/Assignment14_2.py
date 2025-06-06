class Rectangle:
    
    def __init__(self,A,B):
        self.Length=A
        self.Width=B
        
    def Area(self):
        return self.Length*self.Width
    
    def Perimeter(self):
        return 2*(self.Length+self.Width)
    
def main():
    
    obj1=Rectangle(10,20)
    obj2=Rectangle(31,25)
    
    ret=obj1.Area()
    print(ret)
    ret=obj1.Perimeter()
    print(ret)
    
    ret=obj2.Area()
    print(ret)
    ret=obj2.Perimeter()
    print(ret)
    
    
    
if __name__=="__main__":    
    main()