class BookAccount:
    ROI=10.5
    def __init__(self,A,B):
        self.Name=A
        self.Amount=B
    
    def Display(self):
        print(self.Name)
        print(self.Amount)
    
    def Deposit(self,A):
        self.Amount=self.Amount+A
    
    def Withdraw(self,A):
        self.Amount=self.Amount-A
    
    def CalculateInterest(self):
        self.Amount*BookAccount.ROI
    
def main():
    
    obj1=BookAccount("Geetanjali",10000)
    obj2=BookAccount("Vinod",20000)
    
    obj1.Deposit(5000)
    obj1.Withdraw(3000)
    obj1.Display()
    
    obj2.Withdraw(5000)
    obj2.Deposit(10000)
    obj2.Display()
    
if __name__=="__main__":    
    main()