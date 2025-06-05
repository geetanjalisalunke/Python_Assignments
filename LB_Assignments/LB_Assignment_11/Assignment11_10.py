def Pattern(lst):
    
    for num in lst:
        if num%2==0:
            print("*"*num,end=" ")
            print()    
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    Pattern(a)
    
    
    
if __name__=="__main__":
    main()