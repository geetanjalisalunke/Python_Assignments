def Pattern(lst,no):
    
    for i in range(no):
        for j in range(no):
            if (j==0 or j==no-1) or (i==0 or i==no-1):
                print(lst[j],end=" ")
            else:
                print("00",end=" ")
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