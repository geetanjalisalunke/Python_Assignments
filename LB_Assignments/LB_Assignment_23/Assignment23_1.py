def DisplayBinary(no):
    res=""
    while (no>0):
        val=no%2
        res=str(val)+res
        no=no//2
    print(res)
        
def main():
    print("Enter Number")
    value=int(input())
        
    DisplayBinary(value)
    
    
if __name__=="__main__":
    main()