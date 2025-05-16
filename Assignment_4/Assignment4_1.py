def main():
    
    print("Enter the number")
    val1=int(input())
    
    power=lambda val1:val1**2
    ans=power(val1)
    print("Power of given number is :",ans)
    
if __name__=="__main__":
    main()
