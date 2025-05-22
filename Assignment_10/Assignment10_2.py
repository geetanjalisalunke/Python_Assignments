def main():
    print("Enter the First Number")
    no1=int(input())
    
    print("Enter the Second Number")
    no2=int(input())
    
    mult=lambda no1,no2:no1*no2
    ret=mult(no1,no2)
    print(ret)

if __name__=="__main__":
    main()