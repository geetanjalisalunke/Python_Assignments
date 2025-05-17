def main():
    a=[]
    print("Enter the number")
    no=int(input())
    
    for i in range(no):
        a.append(int(input()))
    
    ans=list(map(lambda no:no*2,a))
    print("Double List",ans)
    
if __name__=="__main__":
    main()
    