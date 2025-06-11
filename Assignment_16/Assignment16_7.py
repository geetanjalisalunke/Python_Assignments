import os,json,csv
             
def main():
    
    flag1=os.path.exists("marks.txt")
    
    if flag1==False:
        
        fd=open("marks.txt","x")
        for i in range (5):
            fd.write(input()+"\n")
    else:
        print("File exists")   
        
    fd=open("marks.txt","r")
    data=csv.reader(fd)
    #print(data)
    for row in data:
        #print(row)
        for word in row:
            words=word.split()
            #print(words)
            if int(words[1])>90:
                print(words)
            
    fd.close()     
        
        
if __name__=="__main__":
    main()