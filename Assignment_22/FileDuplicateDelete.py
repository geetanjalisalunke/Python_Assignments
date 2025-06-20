import sys
import FileOp 
import schedule ,time  

def main():
    
    Border='-'*80
    print(Border)
    print("-----------------------Marvellous Automation-----------------------")
    print(Border)
    
    if (len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform Directory Cleaning.")
            print("This is the Directory Automation script")

        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory TimeInterval MailID")
            print("Please provide valid absolute path.")
        
    elif (len(sys.argv) == 4):
        
        schedule.every(int(sys.argv[2])).minutes.do(FileOp.Deletedup)
        while (True):
            schedule.run_pending()
            time.sleep(1)
        
    else:
        
        print("Invalid number of command line arguments.")
        print("Use the given flags as : ")
        print("--h : used to display the HELP.")
        print("--u : Used to display the USAGE.")

    print(Border)
    print("-------------------Thank you for using our script------------------")
    print("-----------------------Marvellous Infosystems----------------------")
    print(Border)
        

if __name__=="__main__":
    main()