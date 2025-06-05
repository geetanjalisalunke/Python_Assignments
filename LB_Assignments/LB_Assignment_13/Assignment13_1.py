def Display(str1):
    res=''
    for i in range(0,len(str1)):
        res=res+str1[i]
    print(res)
        
def main():
    
    print("Enter String")
    a=input()
    
    Display(a)
    
if __name__=="__main__":
    main()