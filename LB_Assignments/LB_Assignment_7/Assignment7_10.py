def GenRoot(no):
    num=no
    sum=0
  
    while(no>0):
        val=no%10
        sum=sum+val
        no=no//10
    num=sum
    print(sum)
    sum=0
    
    while (num>0):
        val=num%10
        sum=sum+val
        num=num//10
    print(sum)
    
    
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    
    GenRoot(value1)
    
if __name__=="__main__":
    main()