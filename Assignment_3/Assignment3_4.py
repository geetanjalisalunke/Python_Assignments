def list_freq(b,no):
    cnt=0
    for val in b:
        if val==no:
            cnt=cnt+1
    return cnt
    
    
def main():
    a=[]
    print("Enter the number")
    val1=int(input())
    print("Enter the numbers in list")
    for i in range(val1):
        a.append(int(input()))
    print("Enter the number to be searched")
    val2=int(input())
    ans=list_freq(a,val2)
    print("Frequency of given number is :",ans)
    
if __name__=="__main__":
    main()
