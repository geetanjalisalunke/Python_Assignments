def ChkBit(no):
    f_bit=1<<3
    s_bit=1<<6
    
    
    if no & f_bit :
        print("4th bit is ON")
    else:
        print("4th bit is OFF")
    
    if no & s_bit :
        print("7th bit is ON")
    else:
        print("7th bit is OFF")
    
        
def main():
    print("Enter Number")
    value=int(input())
        
    ChkBit(value)
    
if __name__=="__main__":
    main()