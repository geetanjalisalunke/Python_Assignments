import functools as f

def chk_prime(no):
    cnt=0
    for i in range(1,no+1):
        if no%i==0:
            cnt=cnt+1
    
    if cnt==2:
        return True
    else:
        return False
def max(no1,no2):
    max=no1
    if no2>no1:
        max=no2
    return max
    

def main():
    print("Enter the Number")
    no=int(input())
    a=[]
    
    print("Enter the Elements")
    
    for i in range(no):
        a.append(int(input()))
    
    fdata=list(filter(chk_prime,a))
    print(fdata)
    
    mdata=list(map(lambda no:no*2,fdata))
    print(mdata)
    
    rdata=f.reduce(max,mdata)
    print(rdata)

if __name__=="__main__":
    main()