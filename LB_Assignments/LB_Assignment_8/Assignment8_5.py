def PrintPrime(lst):
    
    for num in lst:
        cnt=0
        for i in range(1,num+1):
            if num%i==0:
                cnt=cnt+1
        if cnt==2:
            print(num)
        
    
def main():
    a=[]
    print("Enter 8 Numbers")
    for i in range(8):
        a.append(int(input()))
    PrintPrime(a)
    
if __name__=="__main__":
    main()