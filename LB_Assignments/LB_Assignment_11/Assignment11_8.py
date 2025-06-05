def Search(lst,ch):
    
    cnt=0
    for num in lst:
        if ch>='a' and ch<='z':
            if num==ch or num==chr(ord(ch)-32):
                cnt=cnt+1
        elif ch>='A' and ch<='Z':
            if num==ch or num==chr(ord(ch)+32):
                cnt=cnt+1
    print(cnt)
    
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(input())
    print("Enter the character")
    ch=input()
    
    Search(a,ch)
    
if __name__=="__main__":
    main()