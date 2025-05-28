def DigitDiff(no):
    
    min=no%10
    max=no%10
    while(no>0)    :
        val=no%10
        if val<min:
            min=val
        elif val>max:
            max=val
        no=no//10
        
    return max-min
        
        
def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret1=DigitDiff(value1)
    print(ret1)
    
    
if __name__=="__main__":
    main()