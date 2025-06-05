def Pattern(no):
    
    for i in range (no):
        print(chr(ord('A')+i),end=" ")
            
       
def main():
    
    print("Enter Number")
    a=int(input())
   
    Pattern(a)
    
    
if __name__=="__main__":
    main()