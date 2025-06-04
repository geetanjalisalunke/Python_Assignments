def PrimeRange(no1,no2):
    
    for num in range(no1,no2+1):
        cnt=0
        for i in range(1,num+1):
            if num%i==0:
                cnt=cnt+1
        if cnt==2:
            print(num)
    
    
def main():
    
    print("Enter First Number")
    value1=int(input())
    print("Enter Second Number")
    value2=int(input())
    
    PrimeRange(value1,value2)
    
if __name__=="__main__":
    main()