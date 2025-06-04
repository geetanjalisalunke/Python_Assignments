def SImpleIntrest(no1,no2,no3):
   return no1*no2*no3
    
def main():
    
    print("Enter Amount")
    value1=int(input())
    print("Enter Time")
    value2=int(input())
    print("Enter rate")
    value3=float(input())
    ret=SImpleIntrest(value1,value2,value3)
    print(ret)


if __name__=="__main__":
    main()