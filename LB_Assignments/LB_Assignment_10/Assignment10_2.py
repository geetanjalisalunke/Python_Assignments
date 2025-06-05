def DisplayEven(lst1,lst2):

    for num in lst1:
        if num%2==0:
            print(num,end=" ")
    print()
    for num in lst2:
        if num%2==0:
            print(num,end=" ")
           
        
def main():
    a=[]
    b=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
        
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        b.append(int(input()))
    
    DisplayEven(a,b)
    
    
if __name__=="__main__":
    main()