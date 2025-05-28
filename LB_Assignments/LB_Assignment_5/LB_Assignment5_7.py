def main():
    
    print("Enter Radius")
    value1=float(input())
    
    AreaCircle=lambda val:3.14*val*2
    
    ret=AreaCircle(value1)
    print("Area of Circle ",ret)
    
if __name__=="__main__":
    main()