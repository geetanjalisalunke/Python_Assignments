def StrCpyCap(str1):
    res=""
    for ch in str1:
        if ch>='A' and ch<='Z'  :
            res=res+ch
    print(res)
    
def main():
    
    print("Enter String")
    a=input()
   
    
    StrCpyCap(a)
    
if __name__=="__main__":
    main()