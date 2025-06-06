def Pattern(lst,no):
    
    for i in range(1,no+1):
        if i%2==0:
           for j in range(no-1,-1,-1):
               if j%2!=0:
                   print("00",end=" ")
               else:
                    print(lst[j],end=" ") 
            
        else:
            for j in range(no):
                if j%2!=0:
                   print("00",end=" ")
                else:
                    print(lst[j],end=" ")
               
            
        print()
    
        
def main():
    a=[]
    print("Enter Number")
    value=int(input())
    
    for i in range(value):
        a.append(int(input()))
        
    Pattern(a,value)
    
    
if __name__=="__main__":
    main()