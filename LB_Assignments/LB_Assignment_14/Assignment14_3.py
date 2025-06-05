def StrWrdRev(str1):
    a=[]
    
    temp=str1.split()
    for word in temp:
        rev=""
        for ch in word:
            rev=ch+rev
        a.append(rev)
    return a
       
def main():
    
    print("Enter String")
    a=input()
   
    ret=StrWrdRev(a)
    print(ret)
    
if __name__=="__main__":
    main()