def ChkArmstrong(no):
    
    num=no
    sum=0
    ch=str(no)
    while (no>0):
       power=1
       val=no%10
       power=val**len(ch)
       sum=sum+power
       
       no=no//10
    if num==sum:
        return True
    else:
        return False
    
def main():
    
    print("Enter Number")
    value1=int(input())
    
    ret=ChkArmstrong(value1)
    print(ret)


if __name__=="__main__":
    main()