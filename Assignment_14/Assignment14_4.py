class Student:
    School_name="JKP"
    
    def __init__(self,A,B):
        self.Name=A
        self.Roll_No=B
        
    def Display(self):
        print(self.Name)
        print(self.Roll_No)
        print(Student.School_name)
    
def main():
    
    obj1=Student("Geetanjali",101)
    
    obj1.Display()
    
    obj2=Student("Vinod",102)
    obj2.Display()
    Student.School_name="Modern College"
    print(Student.School_name)
 
if __name__=="__main__":    
    main()