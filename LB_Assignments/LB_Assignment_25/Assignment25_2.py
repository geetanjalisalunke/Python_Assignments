def OffBit(no,pos):
    mask=~(1<<(pos-1))
    print(mask)
    num=no & mask
    return num
  
    
    
    
def main():
    print("Enter Number")
    value=int(input())
    
    print("Enter the position")
    pos=int(input())
        
    ret=OffBit(value,pos)
    print(ret)
    
if __name__=="__main__":
    main()