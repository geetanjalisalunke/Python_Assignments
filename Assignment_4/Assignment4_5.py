import functools as f

def prime(no):
    cnt=0
    for i in range(1,no+1):
        if no%i==0:
            cnt=cnt+1
    if cnt==2:
        return True
    else:
        return False
    
def mult(no)  :
    return no*2

def max(no1,no2):
    max=no1
    if no1<no2:
        max=no2
    return no2

def main():
    a=[]
    print("Enter the Number")
    no=int(input())
    print("Enter the list Number")
    for i in range(no):
        a.append(int(input()))
    
    fdata=list(filter(prime,a))
    print(fdata)
    mdata=list(map(mult,fdata))
    print(mdata)
    rdata=f.reduce(max,mdata)
    print(rdata)

if __name__=="__main__":
    main()