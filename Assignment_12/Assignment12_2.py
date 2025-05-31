class Circle:
    PI=3.14
    
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
        
    def Accept(self):
        print("Enter the Radius")
        self.radius=float(input())
        
    def CalculateArea(self):
        
        self.area=Circle.PI*self.radius*self.radius
    
    def CalculateCircumference(self):
        
        self.circumference=2*Circle.PI*self.radius
        
    def Display(self):
        
        print("Raduis of Circle",self.radius)
        print("Area of Circle",self.area)
        print("Circumference of Circle",self.circumference)
        
obj1=Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()