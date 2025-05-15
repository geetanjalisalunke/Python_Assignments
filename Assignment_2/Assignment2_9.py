def cnt_digit(no1):
    sum=0
    new_num=str(abs(no1))
    for val in new_num:
        sum=sum+int(val)
    return sum
    
    
def main():
    
    print("Enter the number")
    val1=int(input())
    ans=cnt_digit(val1)
    print("Addition of number is :",ans)
    
if __name__=="__main__":
    main()
