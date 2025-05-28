

def main():
    
    print("Enter Radius")
    value1=float(input())
    
    AreaCircle=lambda r:3.14*r*r
    
    ret=AreaCircle(value1)
    print("Area of Circle",ret)
    
if __name__=="__main__":
    main()