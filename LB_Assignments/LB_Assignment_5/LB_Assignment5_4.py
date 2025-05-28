def AreaSquare(no):
    return no**2


def main():
    
    print("Enter Number")
    value1=float(input())
    
    ret=AreaSquare(value1)
    print("Area of Square",ret)
    
if __name__=="__main__":
    main()