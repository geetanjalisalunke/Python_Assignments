def ToggleBit(no,pos):
    # Toggle last nibble (bits 0–3): mask = 0x0000000F
    # Toggle first nibble (bits 28–31): mask = 0xF0000000
    mask = 0xF000000F
    result = no ^ mask
    return result
  
    
def main():
    print("Enter Number")
    value=int(input())
    
    print("Enter the position")
    pos=int(input())
        
    ret=ToggleBit(value,pos)
    print(ret)
    
if __name__=="__main__":    
    main()