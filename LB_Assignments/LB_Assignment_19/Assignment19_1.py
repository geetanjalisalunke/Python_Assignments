def Pattern(row,col):
    for i in range(row):
        for j in range(col):
            if i==0 or i==row-1 or j==0 or j==col-1:
                print(chr(ord("A")+j),end=" ")
            else:
                print("0",end=" ")
        print()
        
def main():
    
    print("Enter row")
    a=int(input())
    print("Enter column")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()