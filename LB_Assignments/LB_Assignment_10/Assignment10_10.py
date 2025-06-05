def ChkPallindrome(lst1):
    a=[]
    for i in range(len(lst1)-1,-1,-1):
        a.append(lst1[i])
    for i in range(0,len(a)):
        if lst1[i]!=a[i]:
            return False
        else:
            return True
           
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    ret=ChkPallindrome(a)
    print(ret)
    
    
if __name__=="__main__":
    main()