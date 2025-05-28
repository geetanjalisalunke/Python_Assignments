def Pattern(no):
    
    for i in range(no):
        print("*",end=" ")
    for i in range(no):
        print("#",end=" ")


def main():
    
    print("Enter First Number")
    value1=int(input())
    
    Pattern(value1)
    
if __name__=="__main__":
    main()