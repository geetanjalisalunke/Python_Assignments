class Book:
    __Price=0
    
    def Get(self):
        return Book.__Price
    
    def Set(self,A):
        Book.__Price=A
    
def main():
    
    obj1=Book()
    
    obj1.Set(100)
    ret=obj1.Get()
    print(ret)
    
    obj2=Book()
    ret=obj2.Get()
    print(ret)
 
if __name__=="__main__":    
    main()