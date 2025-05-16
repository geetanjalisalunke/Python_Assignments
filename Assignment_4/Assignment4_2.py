def main():
    print("Enter the First Number")
    no1=int(input())
    print("Enter the Second Number")
    no2=int(input())
    
    mult=lambda x,y:x*y
    ans=mult(no1,no2)
    print("Multiplication is :",ans)

if __name__=="__main__":
    main()