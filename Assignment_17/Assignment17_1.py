import schedule,time

def Display():
    print("Jai Ganesh")
             
def main():
      
      schedule.every(2).seconds.do(Display)
      
      while(True):
          schedule.run_pending()
          time.sleep(1)
        
if __name__=="__main__":
    main()