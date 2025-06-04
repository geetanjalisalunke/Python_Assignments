def ChkStrong(no):
    num=no
    sum=0
    while(no>0):
        fact=1
        val=no%10
        
        for i in range(1,val+1):
            fact=fact*i
        #print(fact)
        sum=sum+fact
        #print(sum)   
        no=no//10
    print(sum)
    if num==sum:
        return True
    else:
        return False
    
def main():
    
    print("Enter Number")
    value1=int(input())
    ret=ChkStrong(value1)
    print(ret)


if __name__=="__main__":
    main()