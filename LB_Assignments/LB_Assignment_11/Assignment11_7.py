def ArrayCountVowels(lst):
    a=['a','e','i','o','u','A','E','I','O','U']
    cnt=0
    for num in lst:
        if num in a:
            cnt=cnt+1
    print(cnt)
    
def main():
    a=[]
    print("Enter Number")
    value1=int(input())
    
    for i in range(value1):
        a.append(input())
    
    ArrayCountVowels(a)
    
if __name__=="__main__":
    main()