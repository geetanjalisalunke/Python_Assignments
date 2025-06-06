def Pattern(row,col):
    for i in range(0,row):
        for j in range(col-1,-1,-1):
            print(chr(ord("1")+i),end=" ")
            
        print()
        
def main():
    
    print("Enter row")
    a=int(input())
    print("Enter column")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()