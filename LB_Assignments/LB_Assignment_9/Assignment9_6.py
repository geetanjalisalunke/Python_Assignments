def SumDigit(lst):
    for num in lst:
        sum=0
        while(num>0):
            val=num%10
            sum=sum+val
            num=num//10
        print(sum)
        
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    SumDigit(a)
    
    
if __name__=="__main__":
    main()