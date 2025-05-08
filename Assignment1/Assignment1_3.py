def Add(no1,no2):
    res=no1+no2
    return res

if __name__=="__main__":
    print("Enter the number")
    value1=int(input())
    print("Enter the number")
    value2=int(input())
    ans=Add(value1,value2)
    print("Addition is:",ans)
