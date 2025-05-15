def cnt_digit(no1):
    cnt=0
    new_num=str(abs(no1))
    for val in new_num:
        cnt=cnt+1
    return cnt
    
    
def main():
    
    print("Enter the number")
    val1=int(input())
    ans=cnt_digit(val1)
    print(" Number of Digits are :",ans)
    
if __name__=="__main__":
    main()
