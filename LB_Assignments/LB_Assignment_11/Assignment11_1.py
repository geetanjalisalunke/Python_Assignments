def ReverseArray(lst):
    
    for i in range(len(lst)):
        a=[]
        while(lst[i]>0):
            val=lst[i]%10
            a.append(str(val))
            lst[i]=lst[i]//10
        lst[i]="".join(a)
    print(lst)  
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    ReverseArray(a)

    
    
if __name__=="__main__":
    main()