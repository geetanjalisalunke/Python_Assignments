import os
             
def main():
    
    print("Enter the name of file")
    File_name=input()
    flag=os.path.exists(File_name)
    
    if flag==True:
        fd=open(File_name,"r")
        data=fd.read()
        print("Content of file:",data)
        fd.close()
    else:
        print("File is does not exist in current Directory")
        


if __name__=="__main__":
    main()