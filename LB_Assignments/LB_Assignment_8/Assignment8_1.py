def DisplayEven(lst):
    for num in lst:
        if num%2==0:
            print(num,end=" ")
   
    
def main():
    a=[]
    print("Enter Number of Element")
    value1=int(input())
    for i in range(value1):
        a.append(int(input()))
    
    DisplayEven(a)


if __name__=="__main__":
    main()