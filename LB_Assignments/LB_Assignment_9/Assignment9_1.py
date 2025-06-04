def Increase(lst):
    
    for num in lst:
        if num%3==0 and num%5==0:
            num=num+2
        elif num%3==0:
            num=num+1
        print(num)
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    for i in range(value1):
        a.append(int(input()))
    Increase(a)
    
    
if __name__=="__main__":
    main()