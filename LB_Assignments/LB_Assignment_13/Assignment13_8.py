def StrCmpX(str1,str2,no):
    for i in range(no):
        if str1[i]!=str2[i]:
            return False
        else:
            return True
    
    
def main():
    
    print("Enter First String")
    a=input()
    
    print("Enter Second String")
    b=input()
    
    print("Enter the number")
    c=int(input())
   
    ret=StrCmpX(a,b,c)
    print(ret)
    
if __name__=="__main__":
    main()