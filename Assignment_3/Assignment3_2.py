def list_max(b):
    max=b[0]
    for val in b:
        if max<val:
            max=val
    return max
    
    
def main():
    a=[]
    print("Enter the number")
    val1=int(input())
    print("Enter the numbers in list")
    for i in range(val1):
        a.append(int(input()))
    ans=list_max(a)
    print("Maximum number is :",ans)
    
if __name__=="__main__":
    main()
