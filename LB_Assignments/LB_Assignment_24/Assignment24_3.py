def ToggleBit(no):
    s_bit=1<<6
    mask=~(s_bit)
    
    print(no & s_bit)
    if no & s_bit:
        print(no & mask)
        
    else:
        print(no | s_bit)
    
def main():
    print("Enter Number")
    value=int(input())
        
    ToggleBit(value)
    
if __name__=="__main__":
    main()