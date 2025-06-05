def WordCount(str1):
    a=[]
    
    temp=str1.split()
    for word in temp:
        a.append(len(word))
    max=a[0]
    for i in a:
        if i>max:
            max=i
    return max
    
       
def main():
    
    print("Enter String")
    a=input()
   
    ret=WordCount(a)
    print(ret)
    
if __name__=="__main__":
    main()