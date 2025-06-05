def ArrayCapital(lst):
    cnt=0
    for ch in lst:
        if ch>='A' and ch<='Z':
            cnt=cnt+1
    return cnt
    
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(input())
    
    ret=ArrayCapital(a)
    print(ret)

    
    
if __name__=="__main__":
    main()