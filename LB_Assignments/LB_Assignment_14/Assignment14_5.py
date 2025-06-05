def StrCap(str1):
    a=[]
    temp=str1.split()
    for word in temp:
        res=""
        for i in range(0,len(word)):
            if word[i]>='a' and word[i]<='z':
                if i==0:
                    new_ch=chr(ord(word[i])-32)
                    res=res+new_ch
                else:
                    res=res+word[i]
            else:
                res=res+word[i]
        a.append(res)
    return " ".join(a)
            
       
def main():
    
    print("Enter String")
    a=input()
   
    ret=StrCap(a)
    print(ret)
    
if __name__=="__main__":
    main()