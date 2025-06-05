def ArrayConcate(lst1,no1,lst2,no2):
    a=[]
    for num in lst1:
        a.append(num)
    
    for num in lst2:
        a.append(num)
    return a      
        
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
    
    ret=ArrayConcate(a,value1,b,value2)
    print(ret,end=" ")
    
    
if __name__=="__main__":
    main()