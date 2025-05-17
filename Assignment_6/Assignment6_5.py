def main():
    print("Enter Number")
    no=int(input())
    cnt=0
    for i in range(1,no+1):
        if no%i==0:
            cnt=cnt+1
    if cnt==2:
        print(f"{no} is prime number")
    else:
        print(f"{no} is not prime number")
    
if __name__=="__main__":
    main()
    