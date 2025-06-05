def SwapX(ch1,ch2):
    
    if  (ch1>='a' and ch1<='z') and (ch2>='a' and ch2<='z'):
        temp=ch1
        ch1=ch2
        ch2=temp
    if  (ch1>='A' and ch1<='Z') and (ch2>='A' and ch2<='Z'):
        temp=ch1
        ch1=ch2
        ch2=temp
            
    return ch1,ch2
        
def main():
    
    print("Enter First Character")
    a=input()
    print("Enter Second Character")
    b=input()
    
    ret1,ret2=SwapX(a,b)
    print(ret1,ret2)
    
if __name__=="__main__":
    main()