def ArrayReplace(lst):
    
    for num in lst:
        if num>='A' and num<='Z':
            num=chr(ord(num)+32)
            print(num,end=" ")
        else:
            print(num,end=" ")
    
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(input())
    
    ArrayReplace(a)
    
if __name__=="__main__":
    main()