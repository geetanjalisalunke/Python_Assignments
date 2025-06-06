def Pattern(no):
    a=[]
    cnt=0
    while(no>0):
        val=no%10
        a.append(val)
        cnt=cnt+1
        no=no//10
        
    for i in range(cnt):
        for j in range(cnt):
            if i>=j:
                print(a[j],end=" ")
        print()
        
def main():
    
    print("Enter String")
    a=int(input())
   
    Pattern(a)
    
    
if __name__=="__main__":
    main()