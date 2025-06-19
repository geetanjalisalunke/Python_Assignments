import sys,os,hashlib

def CalculateChecksum(path,Blocksize=1024):
    a=[]
    for Foldername,sub_folders,files in os.walk(path):
        
        
        for file in files:
            path=os.path.join(Foldername,file)
            fobj=open(path,"rb")    
            hobj=hashlib.md5()
            
            buffer=fobj.read(Blocksize)
            while(len(buffer)>0):
                hobj.update(buffer)
                buffer=fobj.read(Blocksize)
            print("File Name :",path)        
            print("Checksum is :",hobj.hexdigest)
               
    
def main():
    dir_name=sys.argv[1]
    CalculateChecksum(dir_name)

if __name__=="__main__":
    main()