class BankAccount:
   
    def __init__(self,A,B,C):
        self.Name=A
        self.Acc_No=B
        self.Balance=C
        
    def Display_Bal(self):
        print(self.Balance)
        
    def Deposit(self,A):
        self.Balance=self.Balance+A
    
    def Withdraw(self,A):
        self.Balance=self.Balance-A
    
def main():
    
    obj1=BankAccount("Geetanjali",101,10000)
    obj1.Deposit(5000)
    obj1.Display_Bal()
    
    obj2=BankAccount("Vinod",102,20000)
    obj2.Deposit(10000)
    obj2.Withdraw(5000)
    obj2.Display_Bal()
 
if __name__=="__main__":    
    main()