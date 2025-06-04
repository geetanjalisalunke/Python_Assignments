def ArrReverce(lst):
    for num in lst:
        b=[]
        while(num>0):
            val=num%10
            b.append(str(val))
            num=num//10
        print("".join(b))
        
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    ArrReverce(a)
    
    
if __name__=="__main__":
    main()