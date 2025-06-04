def DisplayDivisible(lst,no):
    for num in lst:
        if num%no==0:
            print(num)
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    print("Enter the number")
    value2=int(input())
    DisplayDivisible(a,value2)
    
    
if __name__=="__main__":
    main()