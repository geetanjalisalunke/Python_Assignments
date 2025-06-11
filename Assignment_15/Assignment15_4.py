import os,sys
             
def main():
    File_name1=sys.argv[1]
    File_name2=sys.argv[2]
    flag1=os.path.exists(File_name1)
    flag2=os.path.exists(File_name2)
    
    if flag1==True and flag2==True :
        
        fd1=open(File_name1,"r")
        fd2=open(File_name2,"r")
        data1=fd1.read()
        data2=fd2.read()
        
        if data1==data2:
            print( "Success")
        else:
            print( "Failure")
    else:
        print("File does not exists")
        
        
if __name__=="__main__":
    main()