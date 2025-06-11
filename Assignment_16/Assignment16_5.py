import os
             
def main():
    
    flag1=os.path.exists("Number.txt")
    
    if flag1==True:
        fd=open("Number.txt","r")
        data=fd.readlines()
        #print(data)
        for line in data:
            word=line.split()
            if len(word)>5:
                print(line)
        fd.close()
        
    else:
        print("File exists")    
        
if __name__=="__main__":
    main()