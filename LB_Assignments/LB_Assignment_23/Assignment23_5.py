def CountBit(no):
    res=""
    while(no>0):
        val=no & 1
        res=str(val)+res
        no=no>>1
    print(len(res))
    
        
def main():
    print("Enter Number")
    value=int(input())
        
    CountBit(value)
    
if __name__=="__main__":
    main()