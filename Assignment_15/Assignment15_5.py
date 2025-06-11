import os,sys
             
def main():
    File_name1=sys.argv[1]
    S_String=sys.argv[2]
    flag1=os.path.exists(File_name1)
    
    if flag1==True:
        fd=open(File_name1,"r")
        data=fd.read()
        cnt=0
        words=data.split()
        for i in words:
            if S_String==i:
                cnt=cnt+1
        print(cnt)
    else:
        print("File does not exists")
        
        
if __name__=="__main__":
    main()