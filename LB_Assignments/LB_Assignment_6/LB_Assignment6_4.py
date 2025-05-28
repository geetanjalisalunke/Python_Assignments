def CalculateHr(no):
    
    hr= no//60
    min=no/60
    decimal_part = min -int(min)
    second=int(decimal_part*60)
    
    return hr ,second
        
def main():
    
    print("Enter Number")
    value1=int(input())
    
    
    ret1,ret2=CalculateHr(value1)
    print(f"{ret1} Hour and {ret2} Minute ")
    
if __name__=="__main__":
    main()