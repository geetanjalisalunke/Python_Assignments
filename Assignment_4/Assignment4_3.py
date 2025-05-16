import functools as f

def filter_no(no):
    return no>=70 and no<=90

def Incrase(no):
    return no+10

def mult(no1,no2):
    ret=1
    ret=no1*no2
    return ret

def main():
    a=[]
    print("Enter the Number")
    no=int(input())
    print("Enter the list Number")
    for i in range(no):
        a.append(int(input()))
    
    fdata=list(filter(filter_no,a))
    print(fdata)
    mdata=list(map(Incrase,fdata))
    print(mdata)
    rdata=f.reduce(mult,mdata)
    print(rdata)

if __name__=="__main__":
    main()