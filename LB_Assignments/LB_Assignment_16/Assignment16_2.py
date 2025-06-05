def Pattern(row,col):
    for i in range(1,row+1):
        for j in range(1,col+1):
            if j==1 or j==col or i==1 or i==row:
                print(j,end=" ")
            else:
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