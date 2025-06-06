class Employee:
    
    def __init__(self,A,B,C):
        self.Name=A
        self.__Salary=B
        self._Dept=C
    
    def Display(self):
        print(self.__Salary)
        print(self._Dept)
        print(self.Name)
        
class Manager(Employee):
    
    def __init__(self,A,B,C):
        super().__init__(A,B,C)
        
    def Display(self):
        super().Display()
        
        
def main():
    obj1=Manager("Geetanjali",1000,"HR")
    obj1.Display()
    print(obj1.Name)
    print(obj1._Dept)
    #print(obj1.__Salary)   not accessible outside the class as it is private attribute
 
if __name__=="__main__":    
    main()