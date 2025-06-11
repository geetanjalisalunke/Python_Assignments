import os,json,csv
             
def main():
    
    flag1=os.path.exists("Data.txt")
    
    if flag1==True:
        
        fd=open("Data.txt","r")
        fd2=open("Data_new.txt","x")
        data=fd.readlines()  #return list of lines
        for line in data:
            data_new=line.replace(" ","")
            fd2.write(data_new)
        print(data)
        print("File contents written successfully")
        
    else:
        print("File does not exist")   
        
    
        
        
if __name__=="__main__":
    main()