class Employee:
    
    def __init__(self,A,B,C):
        self.Name=A
        self.Id=B
        self.Salary=C
        
    def Display(self):
        print("Name:",self.Name)
        print("Id:",self.Id)
        print("Salary:",self.Salary)
    
def main():
    
    obj1=Employee("Geetanjali",101,10000)
    obj2=Employee("Vinod",102,20000)
    
    obj1.Display()
    obj2.Display()
    
    
    
if __name__=="__main__":    
    main()