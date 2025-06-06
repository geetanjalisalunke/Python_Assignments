def ToggleBit(no):
    s_bit=1<<6
    t_bit=1<<9
    mask=s_bit | t_bit
    
    print(no ^ mask)
    
    
def main():
    print("Enter Number")
    value=int(input())
        
    ToggleBit(value)
    
if __name__=="__main__":
    main()