def Reverse(no):
    
    a=[]
    b=[]
    while(no>0):
        
        val=no%10
        a.append(val)
        no=no//10
    
    for val in a:
        ch=str(val)
        b.append(ch)
    return ''.join(b)

def main():
    
    print("Enter First Number")
    value1=int(input())
    
    ret=Reverse(value1)
    print("Reverse Digit is",ret)
    
if __name__=="__main__":
    main()