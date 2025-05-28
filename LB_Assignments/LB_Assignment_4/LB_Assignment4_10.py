def DigitX(no):
    
    evensum=0
    oddsum=0
    while(no>0):
        
        val=no%10
        if val%2!=0:
            oddsum=oddsum+val
        else:
            evensum=evensum+val
        no=no//10
    return evensum,oddsum


def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=DigitX(value1)
    print("Sum of even and odd digit:",ret)
    
if __name__=="__main__":
    main()