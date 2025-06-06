def OnBit(no,pos):
  
    mask=no>>pos-1
    mask=mask & 1
    if mask==1:
        return True
    else:
        return False
    
    
    
def main():
    print("Enter Number")
    value=int(input())
    
    print("Enter the position")
    pos=int(input())
        
    ret=OnBit(value,pos)
    print(ret)
    
if __name__=="__main__":
    main()