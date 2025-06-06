def Pattern(str1):
    
    for i in range(0,len(str1)):
        for j in range(0,len(str1)):
            print(str1[j],end=" ")
        print()
       
def main():
    
    print("Enter String")
    a=input()
   
    Pattern(a)
    
    
if __name__=="__main__":
    main()