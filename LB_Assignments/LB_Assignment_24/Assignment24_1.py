def OffBit(no):
    s_bit=~(1<<6)
    print(s_bit)
    
    res=no & s_bit
    return res
        
def main():
    print("Enter Number")
    value=int(input())
        
    ret=OffBit(value)
    print(ret)
    
if __name__=="__main__":
    main()