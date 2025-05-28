def DigitX(no):
    
    cnt=0
    while(no>0):
        
        val=no%10
        if val>=5:
            cnt=cnt+1
        no=no//10
    return cnt


def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=DigitX(value1)
    print("Number of digit greater than or equal to 5:",ret)
    
if __name__=="__main__":
    main()