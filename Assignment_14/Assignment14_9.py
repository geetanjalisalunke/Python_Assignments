class Product:
    
    def __init__(self,A,B):
        self.Name=A
        self.Price=B
    
    def __eq__(self, object):
        return self.Price==object.Price
    
def main():
    obj1=Product("Car",1000)
    obj2=Product("Car",1000)
    print(obj1==obj2)
 
if __name__=="__main__":    
    main()