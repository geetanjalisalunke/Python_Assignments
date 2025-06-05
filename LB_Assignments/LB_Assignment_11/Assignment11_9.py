def Diffrence(lst):
    C_cnt=0
    S_cnt=0
    
    for ch in lst:
        if ch>='a' and ch<='z':
            S_cnt=S_cnt+1
        elif ch>='A' and ch<='Z':
            C_cnt=C_cnt+1
            
    print(C_cnt-S_cnt)
    
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(input())
    
    
    Diffrence(a)
    
if __name__=="__main__":
    main()