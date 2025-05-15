def Add_fact(no1):
    sum=0
    for val in range(1,int((no1/2)+1)):
        if no1%val==0:
            sum=sum+val
    return sum
            
        
def main():
    
    print("Enter the number")
    val1=int(input())
    ans=Add_fact(val1)
    print("Addition of Factors is :",ans)
    
if __name__=="__main__":
    main()
