def CopyArrayRev(lst1):
    a=[]
    for i in range(len(lst1)-1,-1,-1):
        a.append(lst1[i])
    print(a)
           
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    CopyArrayRev(a)
    
    
if __name__=="__main__":
    main()