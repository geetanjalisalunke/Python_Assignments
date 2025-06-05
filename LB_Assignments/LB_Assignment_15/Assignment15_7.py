def Pattern(no1,no2):
    
    for i in range (1,no1+1):
        for j in range(1,no2+1):
            
            if i%2==0:
                print("#",end=" ")
            
            else:
                print("$",end=" ")
        print()
       
def main():
    
    print("Enter First Number")
    a=int(input())
    print("Enter Second Number")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()