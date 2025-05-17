def main():
    print("Enter the number")
    no=int(input())
    
    sqr=lambda no:no**2
    ans=sqr(no)
    print("Square :",ans)
    
    cube=lambda no:no**3
    ans=cube(no)
    print("Square :",ans)
    
if __name__=="__main__":
    main()
    