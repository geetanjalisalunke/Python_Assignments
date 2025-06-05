def Display(ch1):
    res=''
    print(ord(ch1))
    num=ord(ch1)
    while(num>0):
        val=num%8
        res=str(val)+res
        num=num//8
    print("0o"+res)
    res1=''
    num=ord(ch1)
    while(num>0):
        val=num%16
        res1=str(val)+res1
        num=num//16
    print("0X"+res1)
    
    print(oct(ord(ch1)))
    print(hex(ord(ch1)))
        
def main():
    
    print("Enter Character")
    a=input()
    
    Display(a)
    
if __name__=="__main__":
    main()