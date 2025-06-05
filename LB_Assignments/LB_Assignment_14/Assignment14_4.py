def StrCpyX(str1):
    a=[]
    temp=str1.split()
    for word in temp:
        a.append(word)
    return "".join(a)
       
def main():
    
    print("Enter String")
    a=input()
   
    ret=StrCpyX(a)
    print(ret)
    
if __name__=="__main__":
    main()