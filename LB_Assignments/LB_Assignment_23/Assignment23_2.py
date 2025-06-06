def DisplayBinary(no):
    res=""
    while (no>0):
        val=no & 1
        res=str(val)+res
        no=no>>1
    print(res)
        
def main():
    print("Enter Number")
    value=int(input())
        
    DisplayBinary(value)
    
    
if __name__=="__main__":
    main()