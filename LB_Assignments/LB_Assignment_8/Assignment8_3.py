def AddEven(lst):
    sum=0
    for num in lst:
        if num%2==0:
            sum=sum+num
    return sum
    
def main():
    a=[]
    print("Enter 10 Numbers")
    for i in range(10):
        a.append(int(input()))
    
    ret=AddEven(a)
    print(ret)


if __name__=="__main__":
    main()