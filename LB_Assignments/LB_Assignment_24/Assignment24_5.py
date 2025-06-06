def OnBit(no):
    mask=15
    print(no | mask)
    
    
def main():
    print("Enter Number")
    value=int(input())
        
    OnBit(value)
    
if __name__=="__main__":
    main()