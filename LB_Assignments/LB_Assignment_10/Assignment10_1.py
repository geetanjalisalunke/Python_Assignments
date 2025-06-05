def Display(lst1,lst2):

    for num in lst1:
        print(num,end=" ")
    
    for num in lst2:
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
    
    Display(a,b)
    
    
if __name__=="__main__":
    main()