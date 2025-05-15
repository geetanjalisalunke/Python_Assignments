def display(no1):
    for i in range(no1):
        for j in range(no1):
            print("*",end=" ")
        print("")
def main():
    
    print("Enter the number")
    val1=int(input())
    display(val1)
    
if __name__=="__main__":
    main()
