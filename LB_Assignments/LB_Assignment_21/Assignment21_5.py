def Pattern(lst,no):
    
    for i in range(no):
        for j in range(no):
            if j%2!=0:
                print("00",end=" ")
            else:
                print(lst[i],end=" ")
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