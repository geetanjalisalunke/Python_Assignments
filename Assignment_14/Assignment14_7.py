class Person:
   
   def __init__(self,A,B):
       self.Name=A
       self.Age=B
    
    
class Teacher(Person):
    
    def __init__(self, A, B,C,D):
        super().__init__(A,B)
        self.Subject=C
        self.Salary=D
    
    def Display(self):
         print(self.Name)
         print(self.Age)
         print(self.Subject)
         print(self.Salary)
    
    
def main():
    obj1=Teacher("Geetanjali",25,"Math",10000)
    obj1.Display()
 
if __name__=="__main__":    
    main()