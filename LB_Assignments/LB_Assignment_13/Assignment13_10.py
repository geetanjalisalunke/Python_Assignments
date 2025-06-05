def StrPallindrome(str1):
    
    rev=""
    for i in range(len(str1)-1,-1,-1):
        rev=rev+str1[i]
    for i in range(len(str1))    :
        if rev[i]==str1[i] or rev[i]==chr(ord(str1[i])+32) or rev[i]==chr(ord(str1[i])-32):
            return True
        else:
            return False
    
       
def main():
    
    print("Enter String")
    a=input()
   
    ret=StrPallindrome(a)
    print(ret)
    
if __name__=="__main__":
    main()