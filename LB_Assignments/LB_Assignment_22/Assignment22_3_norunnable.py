def Pattern(lst,no):
    
    for i in range(no):
        cnt=0
        for j in range(no-2):
                print(lst[cnt],end=" ")
                cnt=cnt+2
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