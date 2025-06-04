def DisplayReverse(lst):
    for i in range(9,-1,-1):
        print(lst[i],end=" ")
   
    
def main():
    a=[]
    print("Enter 10 Numbers")
    for i in range(10):
        a.append(int(input()))
    
    DisplayReverse(a)


if __name__=="__main__":
    main()