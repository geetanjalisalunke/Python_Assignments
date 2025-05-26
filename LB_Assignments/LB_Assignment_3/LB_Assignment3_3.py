def DisplayComFactorLarge(no1,no2):
    max=0
    for i in range(1,no1+1):
        if no1%i==0 and no2%i==0:
            max=i
    return max

def main():
    
    print("Enter First Number")
    no1=int(input())
    print("Enter Second Number")
    no2=int(input())
    
    ret=DisplayComFactorLarge(no1,no2)
    print(ret)
    
if __name__=="__main__":
    main()