def Frequency(no):
    my_dic={}
    i=0
    while(no>0):
        val=no%10
        if val in my_dic:
            my_dic[val]=my_dic[val]+1
        else:
            my_dic[val]=1
        
        no=no//10
        i=i+1
    print(my_dic)
    
def main():
    
    print("Enter Number")
    value1=int(input())
    
    Frequency(value1)


if __name__=="__main__":
    main()