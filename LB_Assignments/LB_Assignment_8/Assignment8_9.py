def Minimum(lst):
    min=lst[0]
    for num in lst:
        if num<min:
            min=num
    return min
           
        
def main():
    a=[]
    print("Enter 5 Numbers")
    for i in range(5):
        a.append(int(input()))
    ret=Minimum(a)
    print(ret)
    
if __name__=="__main__":
    main()