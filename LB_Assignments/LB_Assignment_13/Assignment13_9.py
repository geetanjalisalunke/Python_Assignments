def StrCmpX(str1):
    rev=""
    for i in range(len(str1)-1,-1,-1):
        rev=rev+str1[i]
    return rev
       
    
    
def main():
    
    print("Enter String")
    a=input()
   
    ret=StrCmpX(a)
    print(ret)
    
if __name__=="__main__":
    main()