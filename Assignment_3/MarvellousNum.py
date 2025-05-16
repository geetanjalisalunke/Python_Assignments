def Chkprime(no1):
    cnt=0
    for i in range(1,no1+1):
        if no1%i==0:
            cnt=cnt+1
    if cnt==2:
        return True
    else:
        return False

