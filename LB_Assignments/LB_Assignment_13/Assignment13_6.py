def StrNCatX(str1,str2,no):
    res=""
    if no>len(str2):
        for ch in str1:
            res=res+ch
        for ch in str2:
            res=res+ch
    else:
        for ch in str1:
            res=res+ch
        res=res+" "
        for i in range(0,no) :
            res=res+str2[i]
    print(res)
    
def main():
    
    print("Enter First String")
    a=input()
    
    print("Enter Second String")
    b=input()
    
    print("Enter the number")
    c=int(input())
   
    StrNCatX(a,b,c)
    
if __name__=="__main__":
    main()