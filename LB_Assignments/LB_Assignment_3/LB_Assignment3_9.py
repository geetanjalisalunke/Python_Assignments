def SumRange(no1,no2):
    sum=0
    for i in range(no1,no2+1):
        sum=sum+i
    return sum
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    print("Enter Second Number")
    value2=int(input())
    
    ret=SumRange(value1,value2)
    print("Sum of given range is:",ret)
    
if __name__=="__main__":
    main()