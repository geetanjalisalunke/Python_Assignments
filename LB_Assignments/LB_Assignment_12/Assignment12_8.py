def Display(ch1):
    if  (ch1>='a' and ch1<='z'):
        for i in range(ord(ch1),96,-1):
            print(chr(i),end=" ")
    if  (ch1>='A' and ch1<='Z'):
        for i in range(ord(ch1),91,1):
            print(chr(i),end=" ")
    
        
def main():
    
    print("Enter Character")
    a=input()
    
    Display(a)
    
if __name__=="__main__":
    main()