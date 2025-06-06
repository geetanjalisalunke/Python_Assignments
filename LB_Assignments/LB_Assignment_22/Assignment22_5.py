def Pattern(lst,no):
    
    a=[]
    for num in lst:
        sum=0
        while(num>0):
            val=num%10
            sum=sum+val
            num=num//10
        a.append(sum)
    print(a)
    for i in range(no):
        for j in range(no):
            if (i==0 or i==no-1) or (j==0 or j==no-1):
                print(a[j],end=" ")
            else:
                print("0",end=" ")
        print()
    
        
def main():
    a=[]
    print("Enter Number")
    value=int(input())
    
    for i in range(value):
        a.append(int(input()))
        
    Pattern(a,value)
    
    
if __name__=="__main__":
    main()