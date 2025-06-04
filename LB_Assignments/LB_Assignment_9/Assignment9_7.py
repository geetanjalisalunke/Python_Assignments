def MaxDigit(lst):
    my_dict={}
    for num in lst:
        while(num>0):
            val=num%10
            if val in my_dict:
                my_dict[val]=my_dict[val]+1
            else:
                my_dict[val]=1
            num=num//10
    print(my_dict)
    max=0
    key=0
    for i,j in my_dict.items():
        if max<j:
            max=j
            key=i
    return key
        
        
        
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(int(input()))
    
    ret=MaxDigit(a)
    print(ret)
    
    
if __name__=="__main__":
    main()