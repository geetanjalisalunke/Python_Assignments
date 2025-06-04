def ArrayCompare(lst1,lst2):
    
    if len(lst1)!=len(lst2):
        return -1
    for i in range(len(lst1)):
        if lst1[i]!=lst2[i]:
            return False
        else:
            return True
        
        
def main():
    a=[]
    b=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
        
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        b.append(int(input()))
    
    ret=ArrayCompare(a,b)
    print(ret)
    
    
if __name__=="__main__":
    main()