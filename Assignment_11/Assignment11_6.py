sum=0
def Sum_N(no):
    
    if no==0:
        return
    global sum
    sum=sum+no
    
    Sum_N(no-1)
    
    return sum
  
        
def main():
    
    print("Enter Number")
    value1=int(input())
    ret=Sum_N(value1)
    print(ret)
    
    
    
if __name__=="__main__":
    main()