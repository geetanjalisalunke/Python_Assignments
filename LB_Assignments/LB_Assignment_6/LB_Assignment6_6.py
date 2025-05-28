def Pattern(no,char):
    
    for i in range(no):
        print(char,end=" ")
        
def main():
    
    print("Enter Number")
    value1=int(input())
    print("Enter character")
    ch=input()
    
    Pattern(value1,ch)
    
    
if __name__=="__main__":
    main()