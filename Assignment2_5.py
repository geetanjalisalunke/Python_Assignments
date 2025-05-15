def prime(no1):
    cnt=0
    for val in range(1,no1+1):
        if no1%val==0:
            cnt=cnt+1
    if cnt==2:
        print("Given number is a prime number")
    else:
        print("Given number is not a prime number")
            
        
def main():
    
    print("Enter the number")
    val1=int(input())
    prime(val1)
    
if __name__=="__main__":
    main()
