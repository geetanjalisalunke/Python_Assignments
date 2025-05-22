import functools as f

def main():
    print("Enter the Number")
    no=int(input())
    a=[]
    
    print("Enter the Elements")
    
    for i in range(no):
        a.append(int(input()))
    
    fdata=list(filter(lambda no:no%2==0,a))
    print(fdata)
    
    mdata=list(map(lambda no:no**2,fdata))
    print(mdata)
    
    rdata=f.reduce(lambda no1,no2:no1+no2,mdata)
    print(rdata)

if __name__=="__main__":
    main()