def Pattern(no):
    
    for i in range (no):
        if i%2==0:
            print(chr(ord('A')+i),end=" ")
        else:
            print(chr(ord('a')+i),end=" ")
       
def main():
    
    print("Enter Number")
    a=int(input())
   
    Pattern(a)
    
    
if __name__=="__main__":
    main()