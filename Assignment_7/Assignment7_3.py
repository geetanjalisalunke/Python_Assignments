def main():
    a=[]
    print("Enter the number")
    no=int(input())
    
    for i in range(no):
        a.append(int(input()))
    
    ans=list(filter(lambda no:no%2==0,a))
    print("Filtered List",ans)
    
if __name__=="__main__":
    main()
    