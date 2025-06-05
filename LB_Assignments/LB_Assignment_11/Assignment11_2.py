def SumArray(lst):
    
    for i in range(len(lst)):
        sum=0
        while(lst[i]>0):
            val=lst[i]%10
            sum=sum+val
            lst[i]=lst[i]//10
        lst[i]=sum
    print(lst)  
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    SumArray(a)

    
    
if __name__=="__main__":
    main()