def Avg(no1,no2,no3):
    return (no1+no2+no3)/3

def main():
    
    print("Enter First Number")
    no1=int(input())
    print("Enter Second Number")
    no2=int(input())
    print("Enter Third Number")
    no3=int(input())
    
    ret=Avg(no1,no2,no3)
    print(ret)
    
if __name__=="__main__":
    main()