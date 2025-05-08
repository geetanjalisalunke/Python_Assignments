def Chk_Divisible_5(no):
    if no%5==0:
        return True
    else:
        return False

if __name__=="__main__":
    print("Enter the number")
    value1=int(input())
    ans=Chk_Divisible_5(value1)
    print(ans)
