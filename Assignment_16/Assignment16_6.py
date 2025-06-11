import os
             
def main():
    
    flag1=os.path.exists("Number.txt")
    
    if flag1==True:
        fd1=open("Number.txt","r")
        fd2=open("target.txt","w")
        data=fd1.read()
        fd2.write(data)
        print("File Copied successfully")
        fd1.close()
        fd2.close()
        
    else:
        print("File exists")    
        
if __name__=="__main__":
    main()