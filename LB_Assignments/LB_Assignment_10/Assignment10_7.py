def MinArray(lst1,lst2):
    min1=lst1[0]
    min2=lst2[0]
    for num in lst1:
        if min1>num:
            min1=num
    print(min1,end=" ")
    
    for num in lst2:
        if min2>num:
            min2=num
    print(min2)      
        
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
    
    MinArray(a,b)
    
    
if __name__=="__main__":
    main()