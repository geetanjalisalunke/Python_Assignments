def Pattern(lst,no):
    
    for i in range(no-1,-1,-1):
        for j in range(no):
            if i>=j:
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