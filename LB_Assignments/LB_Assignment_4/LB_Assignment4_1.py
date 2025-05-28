def MultDigit(no):
    ans=1
    while(no>0):
        
        val=no%10
        no=no//10
        ans=ans*val
        
    return ans
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=MultDigit(value1)
    print("Multiplication of digit:",ret)
    
if __name__=="__main__":
    main()