def OnBit(no,pos):
    mask=1<<pos-1
    return no | mask
  
    
def main():
    print("Enter Number")
    value=int(input())
    
    print("Enter the position")
    pos=int(input())
        
    ret=OnBit(value,pos)
    print(ret)
    
if __name__=="__main__":
    main()