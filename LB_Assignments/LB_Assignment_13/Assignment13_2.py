def StrNCpyX(str1,no):
    res=""
    if no>len(str1):
        print(str1)
    for i in range(no,len(str1)):
        res=res+str1[i]
    print(res)    
def main():
    
    print("Enter String")
    a=input()
    
    print("Enter the number")
    value=int(input())
    
    StrNCpyX(a,value)
    
if __name__=="__main__":
    main()