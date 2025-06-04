def Power(no1,no2):
    return no1**no2

def main():
    
    print("Enter the First Number")
    value1=int(input())
    print("Enter the First Number")
    value2=int(input())
    ret=Power(value1,value2)
    print(ret)


if __name__=="__main__":
    main()