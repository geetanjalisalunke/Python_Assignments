import schedule,time,datetime

def Display():
    fd=open("Marvellous.txt",'a')
    fd.write("Current Time of file: "+str(datetime.datetime.now())+"\n")
    fd.close()
    print("Time written successfully")
             
def main():
      
      schedule.every(5).minutes.do(Display)
      print("Application is waiting.........")
      
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()