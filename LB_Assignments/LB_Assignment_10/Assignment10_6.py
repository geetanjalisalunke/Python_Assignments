def DiffArray(lst1,lst2):
    sum1=0
    sum2=0
    for num in lst1:
        sum1=sum1+num
    
    for num in lst2:
        sum2=sum2+num
    print(sum1-sum2)      
        
def main():
    a=[]
    b=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
        
    print("Enter Number")
    value2=int(input())
    
    for i in range(value2):
        b.append(int(input()))
    
    DiffArray(a,b)
    
    
if __name__=="__main__":
    main()