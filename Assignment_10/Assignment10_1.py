def main():
    print("Enter the number")
    no1=int(input())
    
    power=lambda no:no**2
    ret=power(no1)
    print(ret)

if __name__=="__main__":
    main()