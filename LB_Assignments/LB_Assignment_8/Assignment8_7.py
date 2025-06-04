def PrintSumDigit(lst):
    
    for num in lst:
        sum=0
        while(num>0):
            val=num%10
            sum=sum+val
            num=num//10
        print(sum,end=" ")    
        
        
    
def main():
    a=[]
    print("Enter 5 Numbers")
    for i in range(5):
        a.append(int(input()))
    PrintSumDigit(a)
    
if __name__=="__main__":
    main()