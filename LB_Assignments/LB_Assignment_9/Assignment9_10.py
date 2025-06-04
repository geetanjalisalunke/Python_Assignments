def ChkSorted(lst):
    
    for i in range(len(lst)):
        if lst[i]<lst[i+1]:
            return True
        else:
            return False
        
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    ret=ChkSorted(a)
    print(ret)
    
    
if __name__=="__main__":
    main()