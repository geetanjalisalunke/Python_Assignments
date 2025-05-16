import functools as f


def main():
    a=[]
    print("Enter the Number")
    no=int(input())
    print("Enter the list Number")
    for i in range(no):
        a.append(int(input()))
    
    fdata=list(filter(lambda no:no%2==0,a))
    print(fdata)
    mdata=list(map(lambda no:no*no,fdata))
    print(mdata)
    rdata=f.reduce(lambda no1,no2:no1+no2,mdata)
    print(rdata)

if __name__=="__main__":
    main()