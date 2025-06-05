def StrCmpX(str1,str2):
    
    if len(str1)!=len(str2):
        return -1
    for i in range(len(str2)):
        if str1[i]!=str2[i]:
            return False
        else:
            return True
    
    
def main():
    
    print("Enter First String")
    a=input()
    
    print("Enter Second String")
    b=input()
   
    ret=StrCmpX(a,b)
    print(ret)
    
if __name__=="__main__":
    main()