import sys,os,shutil
def main():
    
    dir_name1=sys.argv[1]
    dir_name2=sys.argv[2]
    os.mkdir(dir_name2)
    for Foldername,subfoldername,filename in os.walk(dir_name1):
        relative_path = os.path.relpath(Foldername, dir_name1)
        target_folder = os.path.join(dir_name2, relative_path)
        print("Relative path is ",relative_path)
        print("target path is",target_folder)

        for subf in subfoldername:
            path=f"{dir_name2}/{subf}"
            os.makedirs(path)
            print("Folder created",path)
        for file in filename:
            src_file = os.path.join(Foldername, file)
            tgt_file = os.path.join(target_folder, file)
            fd1=open(src_file,'r')
            fd2=open(tgt_file,'x')
            data=fd1.read()
            fd2.write(data)
            print("source file",src_file)
            print("target file",tgt_file)

if __name__=="__main__":
    main()
    