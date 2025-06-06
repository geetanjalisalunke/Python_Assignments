def ChkBit(no):
    res=""
    while (no>0):
        val=no & 1
        res=str(val)+res
        no=no>>1
    print(len(res))
    print(res)
    if len(res)<4:
        return 0
    elif len(res)==4:
        return res[0]
    else:
        return res[-4]
    
        
def main():
    print("Enter Number")
    value=int(input())
        
    ret=ChkBit(value)
    print(ret)
    if ret=='1':
        print("True")
    else:
        print("False")
    
    
if __name__=="__main__":
    main()