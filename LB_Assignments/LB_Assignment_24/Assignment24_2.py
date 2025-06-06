def OffBit(no):
    s_bit=1<<6
    t_bit=1<<9
    
    bit=~(s_bit | t_bit)
    res=(no & bit)
    return res
        
def main():
    print("Enter Number")
    value=int(input())
        
    ret=OffBit(value)
    print(ret)
    
if __name__=="__main__":
    main()