def prime(no1):
    cnt=0
    for i in range(1,no1+1):
        if no1%i==0:
            cnt=cnt+1
    if cnt==2:
        return True
    else:
        return False
    
def main():
    a=[]
    print("Enter the number")
    no=int(input())
    
    for i in range(no):
        a.append(int(input()))
    
    ans=list(filter(prime,a))
    print("Prime numbers :",ans)
    
if __name__=="__main__":
    main()
    