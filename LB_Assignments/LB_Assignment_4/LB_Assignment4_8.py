def DigitX(no):
    
    cnt=0
    while(no>0):
        
        val=no%10
        if val==0:
            cnt=cnt+1
        no=no//10
    return cnt


def main():
    
    print("Enter First Number")
    value1=int(input())
    
    print("Enter Second Number")
    value2=int(input())
    
    print("Enter Third Number")
    value3=int(input())
    
    ret=DigitX(value1)
    print("Occurenece of 0 in digit:",ret)
    
    ret=DigitX(value2)
    print("Occurenece of 0 in digit:",ret)
    
    ret=DigitX(value3)
    print("Occurenece of 0 in digit:",ret)
    
if __name__=="__main__":
    main()