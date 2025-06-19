import sys,os,shutil
def main():
    
    src_dir=sys.argv[1]
    trg_dir=sys.argv[2]
    inp_extension=sys.argv[3]
    
    os.mkdir(trg_dir)
    
    for Foldername,subfoldername,filename in os.walk(src_dir):
        print("Folder name :",Foldername)

        for subf in subfoldername:
            print("Subfolder",subf)
            path=os.path.join(Foldername,subf)
            print("SubFolder created",path)
        for file in filename:
            
            print("File",file)
            src_file = os.path.join(Foldername, file)
            trg_file = os.path.join(trg_dir, file)
            print("File Name",src_file)
            name,extension =os.path.splitext(file)
            if extension==inp_extension:
                print(extension)
                shutil.copyfile(src_file,trg_file)
                print("File Copied Successfully")
            

if __name__=="__main__":
    main()
    