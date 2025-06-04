def EvenOddDiff(lst):
    esum=0
    osumm=0
    for num in lst:
        if num%2==0:
            esum=esum+num
        else:
            osumm=osumm+num
    print(esum-osumm,end=" ")
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    for i in range(value1):
        a.append(int(input()))
    EvenOddDiff(a)
    
    
if __name__=="__main__":
    main()