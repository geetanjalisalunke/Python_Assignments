def Pattern(row,col):
    for i in range(row):
        for j in range(col):
            if  i==j:
                print("$",end=" ")
            elif (i==row-1 and i!=j ) or(j==0 and i!=j)  :
                print("*",end=" ")
            elif (i==0 and i!=j) or (j==col-1 and i!=j):
                print("@",end=" ")
            elif i>j:
                print("#",end=" ")
            else:
                print("&",end=" ")
            
        print()
        
def main():
    
    print("Enter row")
    a=int(input())
    print("Enter column")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()