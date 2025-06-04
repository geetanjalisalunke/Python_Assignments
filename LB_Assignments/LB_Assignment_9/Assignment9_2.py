def EvenOddReplace(lst):
    
    for num in lst:
        if num%2==0:
            num=0
        else:
            num=1
            
        print(num,end=" ")
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    for i in range(value1):
        a.append(int(input()))
    EvenOddReplace(a)
    
    
if __name__=="__main__":
    main()