def Pattern(lst,no):
    
    for i in range(1,no+1):
        for j in range(i):
            print(lst[j],end=" ")
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