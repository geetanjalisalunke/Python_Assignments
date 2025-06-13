import os,sys

def main():
    print("Enter File Name")    
    Filename1=input()
    print("Enter the search String")
    S_string=input()
    
    ret1=os.path.exists(Filename1)
    
    if (ret1==True):
        
        fd1=open(Filename1,'r',encoding='utf-8', errors='ignore')
        data=fd1.read()
        #print(lines)
        word=data.split()
        cnt=0
        for char in word:
            if char==S_string:
                cnt=cnt+1
        print(cnt)
        
       
    else:
        print("There is no such file")

if __name__=="__main__":
    main()
    