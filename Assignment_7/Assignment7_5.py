def palindrome(str1):
    a=[]
    for i in range(len(str1)-1,-1,-1):
        a.append(str1[i])
    str2="".join(a)
    
    if str1==str2:
        return True
    else:
        return False        

def main():
    
    print("Enter String")
    name=input()
    ans=palindrome(name)
    if ans==True:
        print(f"{name} is palindrome")
    else:
        print(f"{name} is not a palindrome")
    
    
if __name__=="__main__":
    main()
    