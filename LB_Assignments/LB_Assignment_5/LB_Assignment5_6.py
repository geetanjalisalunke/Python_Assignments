def main():
    
    print("Enter Number")
    value1=float(input())
    
    CeToMe=lambda val:val/100
    
    ret=CeToMe(value1)
    print("Centimeter to meter ",ret)
    
if __name__=="__main__":
    main()