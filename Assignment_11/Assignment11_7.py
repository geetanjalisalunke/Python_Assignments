
def Pattern(no):
    
    if no==0:
        return
    Pattern(no-1)
    print("*"* no,end=" ")
    print()
    
  
        
def main():
    
    print("Enter Number")
    value1=int(input())
    Pattern(value1)
    
    
    
if __name__=="__main__":
    main()