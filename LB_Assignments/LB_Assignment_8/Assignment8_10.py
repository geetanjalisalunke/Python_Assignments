def DisplayNearest(lst):
    sub=[]
    for num in lst:
        sub.append(abs(num-90))
    print(sub)
    min=sub[0]
    for val in sub:
        if val<min:
            min=val
    print(min+90)
           
        
def main():
    a=[]
    print("Enter 5 Numbers")
    for i in range(5):
        a.append(int(input()))
    DisplayNearest(a)
    
    
if __name__=="__main__":
    main()