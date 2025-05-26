def Factorial(no):
    res=1
    if no<=0:
        return -1
    
    for i in range(1,no+1):
        res=res*i
    return res
    
def main():
    
    print("Enter number")
    no=int(input())
    ret=Factorial(no)
    print(ret)
    
if __name__=="__main__":
    main()