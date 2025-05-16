import MarvellousNum as mn

def list_prime(b):
    sum=0
    for val in b:
        ret=mn.Chkprime(val)
        if ret==True:
            sum=sum+val
    return sum
    
def main():
    a=[]
    print("Enter the number")
    val1=int(input())
    print("Enter the numbers in list")
    for i in range(val1):
        a.append(int(input()))

    ans=list_prime(a)
    print("Addition of all prime numbers is :",ans)
    
if __name__=="__main__":
    main()
