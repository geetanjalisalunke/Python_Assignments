def StrCpySmall(str1,str2):
    res=""
    for ch in str1:
        res=res+ch
    for ch in str2:
        res=res+ch
    print(res)
    
def main():
    
    print("Enter First String")
    a=input()
    
    print("Enter Second String")
    b=input()
   
    
    StrCpySmall(a,b)
    
if __name__=="__main__":
    main()