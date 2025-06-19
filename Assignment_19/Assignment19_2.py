import sys,os
def main():
    
    dir_name=sys.argv[1]
    inp_extension=sys.argv[2]
    
    for Foldername,subfoldername,filename in os.walk(dir_name):
        
        print(Foldername)
        
        for subf in subfoldername:
            print(subf)
            
        for f_name in filename:
            name,extension= os.path.splitext(f_name)
            if extension==inp_extension:
                print(f_name.replace(extension,".doc"))
        

if __name__=="__main__":
    main()