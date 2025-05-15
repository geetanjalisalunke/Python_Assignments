def factorial(no1):
    res=1
    if no1==0:
        return 0
    elif no1<0:
        return -1
    else:
        for i in range(1,no1+1):
            res=res*i
        return res
        
def main():
    
    print("Enter the number")
    val1=int(input())
    ans=factorial(val1)
    if ans==-1:
        print("ValueError: factorial() not defined for negative values")
    else:
        print("Factorial is :",ans)
    
if __name__=="__main__":
    main()
