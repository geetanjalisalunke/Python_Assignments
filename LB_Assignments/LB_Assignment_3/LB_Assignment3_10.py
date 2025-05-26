def DisplayRangeRev(no1,no2):
    a=[]
    for i in range(no2,no1-1,-1):
        a.append(i)
    return a
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    print("Enter Second Number")
    value2=int(input())
    
    ret=DisplayRangeRev(value1,value2)
    print("Sum of given range is:",ret)
    
if __name__=="__main__":
    main()