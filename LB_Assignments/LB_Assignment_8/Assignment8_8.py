def Maximum(lst):
    max=lst[0]
    for num in lst:
        if num>max:
            max=num
    return max
           
        
def main():
    a=[]
    print("Enter 5 Numbers")
    for i in range(5):
        a.append(int(input()))
    ret=Maximum(a)
    print(ret)
    
if __name__=="__main__":
    main()