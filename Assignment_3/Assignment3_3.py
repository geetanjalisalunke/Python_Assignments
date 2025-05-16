def list_min(b):
    min=b[0]
    for val in b:
        if min>val:
            min=val
    return min
    
    
def main():
    a=[]
    print("Enter the number")
    val1=int(input())
    print("Enter the numbers in list")
    for i in range(val1):
        a.append(int(input()))
    ans=list_min(a)
    print("Minimum number is :",ans)
    
if __name__=="__main__":
    main()
