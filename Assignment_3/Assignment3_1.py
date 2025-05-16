def list_add(b):
    sum=0
    for val in b:
        sum=sum+val
    return sum
    
    
def main():
    a=[]
    print("Enter the number")
    val1=int(input())
    print("Enter the numbers in list")
    for i in range(val1):
        a.append(int(input()))
    ans=list_add(a)
    print("Addition of numbers is :",ans)
    
if __name__=="__main__":
    main()
