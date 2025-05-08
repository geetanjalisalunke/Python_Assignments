def Chk(no):
    if no>0:
        print("Positive Number")
    elif no<0:
        print("Negative Number")
    else:
        print("Zero")

if __name__=="__main__":
    print("Enter the number")
    value1=int(input())
    Chk(value1)
