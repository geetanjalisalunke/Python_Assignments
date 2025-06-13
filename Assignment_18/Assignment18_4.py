import os,sys

def main():
        
    Filename1=sys.argv[1]
    Filename2=sys.argv[2]
    
    ret1=os.path.exists(Filename1)
    ret2=os.path.exists(Filename2)
    
    if (ret1==True and ret2==True):
        
        fd1=open(Filename1,'r',encoding='utf-8', errors='ignore')
        data1=fd1.read()
        fd2=open(Filename2,'r',encoding='utf-8', errors='ignore')
        data2=fd2.read()
        
        if data1==data2:
            print("Both files are equal")
        else:
            print("Both files are not equal")
       
    else:
        print("There is no such file")

if __name__=="__main__":
    main()
    