def Display(no):
    
    if no<0:
        print("Please enter valid number")
    else:
        for i in range(0,no):
            print("*",end=" ")

if __name__=="__main__":
    print("Enter the number")
    value1=int(input())
    Display(value1)
    
