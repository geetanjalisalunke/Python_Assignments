def EvenDigit(no):
    sum=0
    while(no>0):
        
        val=no%10
        if val%2==0:
            sum=sum+val
        no=no//10
        
    return sum
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=EvenDigit(value1)
    print("Sum of Even digit:",ret)
    
if __name__=="__main__":
    main()