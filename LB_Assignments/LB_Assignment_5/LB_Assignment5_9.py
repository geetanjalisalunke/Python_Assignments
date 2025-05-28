def main():
    
    print("Enter Length")
    value1=float(input())
    print("Enter Width")
    value2=float(input())
    
    AreaRect=lambda l,w:l*w
    
    ret=AreaRect(value1,value2)
    print("Area of Rectangle",ret)
    
if __name__=="__main__":
    main()