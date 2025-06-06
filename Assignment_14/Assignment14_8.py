class Vehicle:
    
    def Start(self):
        print("Inside Parent Start")
   
   
    
class Car(Vehicle):
    
    def Start(self):
        print("Inside Child Start")
    
    
def main():
    obj1=Car()
    obj1.Start()
 
if __name__=="__main__":    
    main()