import os,sys
             
def main():
    File_name=sys.argv[1]
    flag=os.path.exists(File_name)
    
    if flag==True:
        fd1=open(File_name,'r')
        data=fd1.read()
        fd2=open("Demo.txt",'x')
        fd2.write(data)
        print("Data copied successfully")
        fd1.close()
        fd2.close()
        
    else:
        print("File does not exists")
        
        
if __name__=="__main__":
    main()