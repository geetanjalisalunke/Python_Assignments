def FactDigit(no):
    sum=0
    while(no>0):
       
        res=1 
        val=no%10
        
        for i in range(1,val+1):
            res=res*i
        sum=sum+res
        no=no//10
    return sum
    
        
def main():
    
    print("Enter Number")
    value1=int(input())
    ret=FactDigit(value1)
    print(ret)
    
    
if __name__=="__main__":
    main()