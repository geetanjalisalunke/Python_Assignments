def Pattern(row,col):
    cnt=1
    for i in range(1,row+1):
        for j in range(1,col+1):
            if i>=j:
                print(cnt,end=" ")
                cnt=cnt+1
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