def main():
    a=[]
    print("Enter Number")
    no=int(input())
    for i in range (no):
       a.append(int(input()))
    
    max=a[0]
    for val in a:
        if val>max:
            max=val
    print("Maximum number is ",max)
        
   
    
if __name__=="__main__":
    main()
    