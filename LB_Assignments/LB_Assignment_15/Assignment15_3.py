def Pattern(no1,no2):
    
    for i in range (no1):
        for j in range(no2):
            print("*",end=" ")
        print()
       
def main():
    
    print("Enter First Number")
    a=int(input())
    print("Enter Second Number")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()