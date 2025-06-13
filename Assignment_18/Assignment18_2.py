import os

def main():
        
    print("Enter the name of file that you want to read")
    Filename=input()
    
    ret=os.path.exists(Filename)
    
    if (ret==True):
        print("File is present in the current directory")
        fd=open(Filename,'r',encoding='utf-8')
        data=fd.read()
        print(data)
       
    else:
        print("There is no such file")

if __name__=="__main__":
    main()