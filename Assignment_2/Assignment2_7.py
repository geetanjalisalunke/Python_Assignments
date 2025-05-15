def display(no1):
    for i in range(1,no1+1):
        for j in range(1,no1+1):
            print(j,end=" ")
        print("")
    
            
def main():
    
    print("Enter the number")
    val1=int(input())
    display(val1)
    
if __name__=="__main__":
    main()
