def main():
    
    print("Enter Number")
    value1=float(input())
    
    Estimate=lambda val:val*560
    
    ret=Estimate(value1)
    print(ret)
    
if __name__=="__main__":
    main()