def StrCpySmall(str1):
    res=""
    for ch in str1:
        if ch>='a' and ch<='z'  :
            res=res+ch
    print(res)
    
def main():
    
    print("Enter String")
    a=input()
   
    
    StrCpySmall(a)
    
if __name__=="__main__":
    main()