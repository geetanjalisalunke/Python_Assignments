def Pattern(row,col):
    for i in range(1,row+1):
            if i%2==0:
                for j in range(col-1,-1,-1):
                    print(chr(ord("1")+j),end=" ")
                
            else:
                for j in range(col):
                    print(chr(ord("1")+j),end=" ")
            print()
        
def main():
    
    print("Enter row")
    a=int(input())
    print("Enter column")
    b=int(input())
   
    Pattern(a,b)
    
    
if __name__=="__main__":
    main()