def Pattern(row,col):
    
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print(j,end=" ")
           
        print()
       
def main():
    
    print("Enter First Number")
    a=int(input())
    print("Enter Second Number")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()