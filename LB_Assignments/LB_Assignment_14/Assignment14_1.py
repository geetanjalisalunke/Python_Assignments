def WordCount(str1):
    temp=str1.split()
    return (len(temp))
    
       
def main():
    
    print("Enter String")
    a=input()
   
    ret=WordCount(a)
    print(ret)
    
if __name__=="__main__":
    main()