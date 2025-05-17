def Chk(no1):
   return no1%2==0

def main():
    
    print("Enter the Number")
    no=int(input())
    ans=Chk(no)
    if ans==True:
        print(f"{no} is Even")
    else:
        print(f"{no} is Odd")
    
if __name__=="__main__":
    main()
    