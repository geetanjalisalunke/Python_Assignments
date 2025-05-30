sum=0
def Sum_Digit(no):
   if no==0:
       return
   val=no%10
   global sum
   sum=sum+val
   Sum_Digit(no//10)
   return sum
        
def main():
    
    print("Enter Number")
    value1=int(input())
    ret=Sum_Digit(value1)
    print(ret)
    
    
    
if __name__=="__main__":
    main()