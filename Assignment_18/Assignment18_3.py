import os,sys

def main():
        
    Filename=sys.argv[1]
    
    ret=os.path.exists(Filename)
    
    if (ret==True):
        print("File is present in the current directory")
        fd=open(Filename,'r',encoding='utf-8')
        data=fd.read()
        fd1=open("Demo.txt",'x')
        fd1.write(data)
        print("File content copied successfully")
       
    else:
        print("There is no such file")

if __name__=="__main__":
    main()