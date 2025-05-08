def Chksum(no):
    if no%2==0:
        print("Given number is Even")
    else:
        print("Given number is Odd")

if __name__=="__main__":
    print("Enter the number")
    value1=int(input())
    Chksum(value1)
